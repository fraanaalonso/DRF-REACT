

from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Skill, Project
from .serializers import SkillSerializer, ProjectSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

class SkillViewSet(viewsets.ViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    @action(detail=False, methods=['get'], name='List Skills')
    def list_skills(self, request):
        queryset = Skill.objects.all()
        serializer = SkillSerializer(queryset, many=True)
        data = {'ok': True, 'posts': serializer.data}
        return Response(data)

    @action(detail=False, methods=['post'], name='Create Skills', permission_classes=[IsAdminUser, IsAuthenticated ])
    def create_skills(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            skill = serializer.save()
            if skill:
                data = {'ok': True, 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            else:
                data = {'ok': False, 'msg': serializer.errors}
                return Response(data, status.HTTP_400_BAD_REQUEST)
        else:
            data = {'ok': False, 'msg': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)


    @action(detail = True, methods=['put', 'delete'], name='Delete / Edit Skill', permission_classes=[IsAdminUser, IsAuthenticated])
    def retrieve_skill(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
        except:
            data = {'ok': False, 'msg': 'Skill does not exists'}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SkillSerializer(skill, data=data)
            if serializer.is_valid():
                serializer.save()
                data = {'ok': True, 'msg': 'Correctly modified', 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            data = {'ok': False, 'msg': 'Could not edit the data', 'errors': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            skill.delete()
            data={'ok': True, 'msg': 'Correctly deleted'}
            return Response(data, status.HTTP_202_ACCEPTED)
        else:
            data={'ok': False, 'msg': 'Method not allowed'}           


class ProjectViewSet(viewsets.ViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=False, methods=['get'], name='List Projects')
    def list_projects(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        data = {'ok': True, 'posts': serializer.data}
        return Response(data)

    @action(detail=False, methods=['post'], name='Create Projects', permission_classes=[IsAdminUser, IsAuthenticated ])
    def create_project(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            if project:
                data = {'ok': True, 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            else:
                data = {'ok': False, 'msg': serializer.errors}
                return Response(data, status.HTTP_400_BAD_REQUEST)
        else:
            data = {'ok': False, 'msg': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)


    @action(detail = True, methods=['put', 'delete'], name='Delete / Edit Project', permission_classes=[IsAdminUser, IsAuthenticated])
    def retrieve_project(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except:
            data = {'ok': False, 'msg': 'Project does not exists'}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProjectSerializer(project, data=data)
            if serializer.is_valid():
                serializer.save()
                data = {'ok': True, 'msg': 'Correctly modified', 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            data = {'ok': False, 'msg': 'Could not edit the data', 'errors': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            project.delete()
            data={'ok': True, 'msg': 'Correctly deleted'}
            return Response(data, status.HTTP_202_ACCEPTED)
        else:
            data={'ok': False, 'msg': 'Method not allowed'}   