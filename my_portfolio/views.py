from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Project, SoftSkill, HardSkill, Experience

# Create your views here.
def index(request):
    person = Person.objects.get(id=1)
    projects = Project.objects.all()
    soft_skills = SoftSkill.objects.all()
    hard_skills = HardSkill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'index.html', {
        'person': person,
        'projects': projects,
        'soft_skills': soft_skills,
        'hard_skills': hard_skills,
        'experiences': experiences})