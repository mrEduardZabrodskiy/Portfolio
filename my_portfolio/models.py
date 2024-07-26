from django.db import models

# Create your models here.

class HardSkill(models.Model):
    LEVEL_CHOICES = [
        ('TR', 'Trainee'),
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
    ]
    is_language = models.BooleanField(default=False)
    title = models.CharField(max_length=150)
    level = models.CharField(choices=LEVEL_CHOICES, default='TR', max_length=2)
    logo = models.ImageField(upload_to='static/images', blank=True)
    
    
    def __str__(self):
        return self.title


class SoftSkill(models.Model):
    LEVEL_CHOICES = [
        ('A1', 'Elementary'),
        ('A2', 'Pre-intermediate'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficiency'),
        ('NA', 'Native'),
        
    ]
    is_language = models.BooleanField(default=False)
    level = models.CharField(choices=LEVEL_CHOICES, default='A1', max_length=2, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=3000, blank=True)
    tools = models.ManyToManyField(HardSkill, related_name='projects', blank=True)
    url = models.URLField(blank=True)
    repository_url = models.URLField(blank=True)
    created = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='static/images', blank=True)
    project_logo = models.ImageField(upload_to='static/images', blank=True)
    
    
    class Meta:
        ordering = ['-created']
        
        
    def __str__(self):
        return self.title
        

class Experience(models.Model):
    title = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    description = models.TextField(max_length=2000, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    in_tech = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    education_grade = models.CharField(max_length=100, blank=True)
    education_specialization = models.CharField(max_length=100, blank=True)
    info_about_person = models.TextField(max_length=4000, blank=True)
    
    
    def __str__(self):
        return self.first_name