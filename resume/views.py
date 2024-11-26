from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Experience, Education, Skills, Projects

class HomePageView(TemplateView):
    template_name = 'resume/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all().order_by('-start_date')[:2]
        context['skills'] = Skills.objects.all()[:6]
        context['projects'] = Projects.objects.all()[:3]
        return context

class ResumeView(TemplateView):
    template_name = 'resume/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all().order_by('-start_date')
        context['education'] = Education.objects.all().order_by('-start_date')
        context['skills'] = Skills.objects.all()
        context['projects'] = Projects.objects.all()
        return context

class SkillsView(ListView):
    model = Skills
    template_name = 'resume/skills.html'
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group skills by level
        context['advanced_skills'] = Skills.objects.filter(level='Advanced')
        context['intermediate_skills'] = Skills.objects.filter(level='Intermediate')
        context['basic_skills'] = Skills.objects.filter(level='Basic')
        return context

class ContactView(TemplateView):
    template_name = 'resume/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your contact information
        context['email'] = 'korutla.a@northeastern.edu'
        context['phone'] = '+1 (207) 210-9705'
        context['location'] = 'Boston, MA, USA'
        return context

class ProjectsView(TemplateView):
    template_name = 'resume/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Projects.objects.all()
        return context

class ProfileView(TemplateView):
    template_name = 'resume/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context