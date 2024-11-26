from django.urls import path
from .views import HomePageView, ResumeView, SkillsView, ContactView, ProjectsView

app_name = 'resume'  # Add this line to define the namespace

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]