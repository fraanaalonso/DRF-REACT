from django.contrib import admin
from .models import Skill, Project
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', )