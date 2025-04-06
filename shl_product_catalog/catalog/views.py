from django.shortcuts import render, redirect
from .models import Assessment, JOB_FAMILY_CHOICES, JOB_LEVEL_CHOICES, INDUSTRY_CHOICES, LANGUAGE_CHOICES

def recommend_assessments(job_role, industry, skills):
    assessments = Assessment.objects.all()
    recommendations = []
    skills = [s.strip().lower() for s in skills.split(",") if s.strip()]
    for assessment in assessments:
        job_match = (assessment.job_level.lower() == job_role.lower() or 
                     assessment.job_level.lower() == "general population" or 
                     not job_role)
        industry_match = (assessment.industry.lower() == industry.lower() or 
                         not industry)
        assessment_skills = [s.strip().lower() for s in assessment.skills.split(",")]
        skill_match = any(skill.lower() in assessment_skills for skill in skills) if skills else True
        
        if job_match and industry_match and skill_match:
            recommendations.append({
                "name": assessment.name,
                "category": assessment.category,
                "description": assessment.description,
                "id": assessment.id,
                "skills": assessment.skills
            })
    return recommendations

def catalog_home(request):
    assessments = Assessment.objects.all()
    categories = sorted(set(a.category for a in assessments))

    keyword = request.GET.get('keyword', '')
    job_family = request.GET.get('job_family', '')
    job_level = request.GET.get('job_level', '')
    industry = request.GET.get('industry', '')
    language = request.GET.get('language', '')

    if keyword:
        assessments = assessments.filter(name__icontains=keyword)
    if job_family:
        assessments = assessments.filter(job_family=job_family)
    if job_level:
        assessments = assessments.filter(job_level=job_level)
    if industry:
        assessments = assessments.filter(industry=industry)
    if language:
        assessments = assessments.filter(language=language)

    recommended_assessments = []
    if request.method == "POST":
        job_role = request.POST.get("job_role", "").strip()
        industry = request.POST.get("industry", "").strip()
        skills = request.POST.get("skills", "").strip()
        recommended_assessments = recommend_assessments(job_role, industry, skills)
        # Store in session and redirect to recommendations page
        request.session['job_role'] = job_role
        request.session['industry'] = industry
        request.session['skills'] = skills
        return redirect('recommendation_result')

    return render(request, "catalog/catalog_home.html", {
        "assessments": assessments,
        "categories": categories,
        "job_families": [choice[0] for choice in JOB_FAMILY_CHOICES],
        "job_levels": [choice[0] for choice in JOB_LEVEL_CHOICES],
        "industries": [choice[0] for choice in INDUSTRY_CHOICES],
        "languages": [choice[0] for choice in LANGUAGE_CHOICES],
        "keyword": keyword,
        "selected_job_family": job_family,
        "selected_job_level": job_level,
        "selected_industry": industry,
        "selected_language": language,
        "recommended_assessments": recommended_assessments,
    })

def create_assessment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        job_family = request.POST.get("job_family")
        job_level = request.POST.get("job_level")
        industry = request.POST.get("industry")
        language = request.POST.get("language")
        skills = request.POST.get("skills")
        description = request.POST.get("description")
        task_file = request.FILES.get("task_file")
        google_form_link = request.POST.get("google_form_link")
        
        Assessment.objects.create(
            name=name,
            category=category,
            job_family=job_family,
            job_level=job_level,
            industry=industry,
            language=language,
            skills=skills,
            description=description,
            task_file=task_file,
            google_form_link=google_form_link
        )
        return redirect('catalog_home')
    
    return render(request, "catalog/create_assessment.html", {
        "job_families": [choice[0] for choice in JOB_FAMILY_CHOICES],
        "job_levels": [choice[0] for choice in JOB_LEVEL_CHOICES],
        "industries": [choice[0] for choice in INDUSTRY_CHOICES],
        "languages": [choice[0] for choice in LANGUAGE_CHOICES],
    })

def try_assessment(request, assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    return render(request, "catalog/try_assessment.html", {"assessment": assessment})

def recommendation_result(request):
    job_role = request.session.get('job_role', '')
    industry = request.session.get('industry', '')
    skills = request.session.get('skills', '').split(",")
    recommended_assessments = recommend_assessments(job_role, industry, ",".join(skills))
    return render(request, "catalog/recommendation_result.html", {
        "recommended_assessments": recommended_assessments,
        "job_role": job_role,
        "industry": industry,
        "skills": skills,
    })