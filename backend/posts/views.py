from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
# Create your views here.


class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=False, methods=['get', 'post'], name='Listar/Crear Publicaciones', permission_classes=[IsAuthenticated])
    def list_posts(self, request):
        if request.method == 'GET':
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
            data = {'ok': True, 'posts': serializer.data}
            return Response(data)
        else:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                post = serializer.save()
                if post:
                    data = {'ok': True, 'data': serializer.data}
                    return Response(data, status.HTTP_200_OK)
                else:
                    data = {'ok': False, 'msg': serializer.errors}
                    return Response(data, status.HTTP_400_BAD_REQUEST)
            else:
                data = {'ok': False, 'msg': serializer.errors}
                return Response(data, status.HTTP_400_BAD_REQUEST)
    
   

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['get', 'post'], name='Listar/Crear Categorias', permission_classes=[IsAuthenticated])
    def categories_view(self, request):
        if request.method == 'GET':
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
            data = {'ok': True, 'categories': serializer.data}
            return Response(data)
        else:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                category = serializer.save()
                if category:
                    data = {'ok': True, 'data': serializer.data}
                    return Response(data, status.HTTP_200_OK)
                else:
                    data = {'ok': False, 'msg': serializer.errors}
                    return Response(data, status.HTTP_400_BAD_REQUEST)
            else:
                data = {'ok': False, 'msg': serializer.errors}
                return Response(data, status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'put', 'delete'], name='Consultar/Borrar/Editar Categoria', permission_classes=[IsAuthenticated])
    def retrieve_category(self, request, pk):
        queryset = Category.objects.all()
        try:
            category = Category.objects.get(pk=pk)
        except:
            data={'ok': False, 'msg': 'Category does not exist'}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'GET':
            serializer = CategorySerializer( category )
            data = {'ok': True, 'data': serializer.data}
            return Response(data, status.HTTP_200_OK)
        elif request.method=='PUT':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid():
                serializer.save()
                data = {'ok': True, 'msg': 'Correctly modified', 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            data = {'ok': False, 'msg': 'Could not edit the data', 'errors': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)
