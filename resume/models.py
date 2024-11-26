from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Skills(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    git_url = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField()
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    email = models.EmailField(default='korutla.a@northeastern.edu')
    phone = models.CharField(max_length=20, default='+1 (207) 210-9705')
    location = models.CharField(max_length=100, default='Boston, MA, USA')

    def __str__(self):
        return "Profile"
