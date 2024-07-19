from django.contrib import admin
from .models import Person, HardSkill, SoftSkill, Experience, Project

# Register your models here.
class ProjectSkills(admin.ModelAdmin):
    filter_horizontal = ('tools',)


admin.site.register(Person)
admin.site.register(HardSkill)
admin.site.register(SoftSkill)
admin.site.register(Experience)
admin.site.register(Project, ProjectSkills)


