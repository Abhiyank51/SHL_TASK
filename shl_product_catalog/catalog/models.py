from django.db import models

JOB_FAMILY_CHOICES = [
    ('Business', 'Business'),
    ('Clerical', 'Clerical'),
    ('Contact Center', 'Contact Center'),
    ('Customer Service', 'Customer Service'),
    ('Information Technology', 'Information Technology'),
    ('Safety', 'Safety'),
    ('Sales', 'Sales'),
]

JOB_LEVEL_CHOICES = [
    ('Director', 'Director'),
    ('Entry-Level', 'Entry-Level'),
    ('Executive', 'Executive'),
    ('Front Line Manager', 'Front Line Manager'),
    ('General Population', 'General Population'),
    ('Graduate', 'Graduate'),
    ('Manager', 'Manager'),
    ('Mid-Professional', 'Mid-Professional'),
    ('Professional Individual Contributor', 'Professional Individual Contributor'),
    ('Supervisor', 'Supervisor'),
]

INDUSTRY_CHOICES = [
    ('Banking/Finance', 'Banking/Finance'),
    ('Healthcare', 'Healthcare'),
    ('Hospitality', 'Hospitality'),
    ('Insurance', 'Insurance'),
    ('Manufacturing', 'Manufacturing'),
    ('Oil & Gas', 'Oil & Gas'),
    ('Retail', 'Retail'),
    ('Telecommunications', 'Telecommunications'),
]

LANGUAGE_CHOICES = [
    ('English', 'English'),
    ('Spanish', 'Spanish'),
    ('French', 'French'),
    ('German', 'German'),
    ('Chinese', 'Chinese'),
    ('Hindi', 'Hindi'),
    ('Arabic', 'Arabic'),
]

class Assessment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    job_family = models.CharField(max_length=50, choices=JOB_FAMILY_CHOICES, blank=True)
    job_level = models.CharField(max_length=50, choices=JOB_LEVEL_CHOICES, blank=True)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, blank=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, blank=True)
    skills = models.CharField(max_length=200)  # Comma-separated skills
    description = models.TextField()
    task_file = models.FileField(upload_to='tasks/', blank=True, null=True)
    google_form_link = models.URLField(blank=True)

    def __str__(self):
        return self.name