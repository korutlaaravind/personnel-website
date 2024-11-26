from django.contrib import admin
from .models import Experience, Education, Skills, Projects, Profile

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date']
    search_fields = ['title', 'company', 'description']
    list_filter = ['company', 'start_date']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date']
    search_fields = ['institution', 'degree']
    list_filter = ['institution']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
    search_fields = ['name']
    list_filter = ['level']

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies']
    search_fields = ['title', 'description', 'technologies']
    list_filter = ['technologies']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'location']