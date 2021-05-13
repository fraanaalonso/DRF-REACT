from rest_framework import serializers
from .models import Skill, Project


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
    
    def create(self, data):
        skill = Skill.objects.create(
            name = data['name'],
            progresion = data['progresion']
        )

        skill.save()
        return skill
    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.progresion = data.get('progresion', instance.progresion)
        
        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, data):
        project = Project.objects.create(
            name = data['name'],
            code_url = data['code_url'],
            host_url = data['host_url']
        )

        project.save()
        return project

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.code_url = data.get('code_url', instance.code_url)
        instance.host_url = data.get('host_url', instance.host_url)
        
        instance.save()
        return instance       