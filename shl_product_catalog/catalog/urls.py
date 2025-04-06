from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path('create/', views.create_assessment, name='create_assessment'),
    path('try/<int:assessment_id>/', views.try_assessment, name='try_assessment'),
    path('recommendations/', views.recommendation_result, name='recommendation_result'),
]