from django.db import models

# Create your models here.

class HardSkill(models.Model):
    LEVEL_CHOICES = [
        ('TR', 'Trainee'),
        ('JN', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
    ]
    title = models.CharField(max_length=150)
    level = models.CharField(choices=LEVEL_CHOICES, default='TR', max_length=2)
    
    
    def __str__(self):
        return self.title


class SoftSkill(models.Model):
    title = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=3000, blank=True)
    tools = models.ManyToManyField(HardSkill, related_name='projects', blank=True)
    url = models.URLField(blank=True)
    repository_url = models.URLField(blank=True)
    created = models.DateField(auto_now=True)
    
    
    class Meta:
        ordering = ['-created']
        
        
    def __str__(self):
        return self.title
        

class Experience(models.Model):
    title = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    description = models.TextField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    education = models.CharField(max_length=300, blank=True)
    info_about_person = models.TextField(max_length=4000, blank=True)
    
    
    def __str__(self):
        return self.first_name