from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework_extensions.mixins import PaginateByMaxMixin
# Create your views here.


class PostViewSet(PaginateByMaxMixin, viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    max_paginate = 10
    
    @action(detail=False, methods=['get', 'post'], name='Listar/Crear Publicaciones', permission_classes=[IsAuthenticated, DjangoObjectPermissions])
    def list_posts(self, request):
        if request.method == 'GET':
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
            data = {'ok': True, 'num_posts': len(serializer.data), 'posts': serializer.data}
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
    
    @action(detail=True, methods=['get', 'put', 'delete'], name='Consultar/Borrar/Editar Publicación', permission_classes=[IsAuthenticated, DjangoObjectPermissions])
    def retrieve_post(self, request, pk):
        queryset = Post.objects.all()
        try:
            post = Post.objects.get(pk=pk)
        except:
            data={'ok': False, 'msg': 'Post does not exist'}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'GET':
            serializer = PostSerializer( post )
            data = {'ok': True, 'data': serializer.data}
            return Response(data, status.HTTP_200_OK)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = PostSerializer(post, data=data)
            if serializer.is_valid():
                serializer.save()
                data = {'ok': True, 'msg': 'Correctly modified', 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            data = {'ok': False, 'msg': 'Could not edit the data', 'errors': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            post.delete()
            data={'ok': True, 'msg': 'Correctly deleted'}
            return Response(data, status.HTTP_202_ACCEPTED)
        else:
            data={'ok': False, 'msg': 'Method not allowed'}

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['get', 'post'], name='Listar/Crear Categorias', permission_classes=[IsAuthenticated, DjangoObjectPermissions])
    def categories_view(self, request):
        if request.method == 'GET':
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
            data = {'ok': True, 'num_cat': len(serializer.data), 'categories': serializer.data}
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

    @action(detail=True, methods=['get', 'put', 'delete'], name='Consultar/Borrar/Editar Categoria', permission_classes=[IsAuthenticated, DjangoObjectPermissions])
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
        else:
            category.delete()
            data={'ok': True, 'msg': 'Correctly deleted'}
            return Response(data, status.HTTP_202_ACCEPTED)


class CommentViewSet(viewsets.ViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get', 'post'], name='Listar/Crear Comentarios', permission_classes=[IsAuthenticated, DjangoObjectPermissions])
    def comments_view(self, request):
        if request.method == 'GET':
            queryset = Comment.objects.all()
            serializer = CommentSerializer(queryset, many=True)
            data = {'ok': True, 'num_co': len(serializer.data), 'comments': serializer.data}
            return Response(data)
        else:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                comment = serializer.save()
                if comment:
                    data = {'ok': True, 'data': serializer.data}
                    return Response(data, status.HTTP_200_OK)
                else:
                    data = {'ok': False, 'msg': serializer.errors}
                    return Response(data, status.HTTP_400_BAD_REQUEST)
            else:
                data = {'ok': False, 'msg': serializer.errors}
                return Response(data, status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'put', 'delete'], name='Consultar/Borrar/Editar Categoria', permission_classes=[IsAuthenticated, DjangoObjectPermissions])
    def retrieve_comments(self, request, pk):
        queryset = Comment.objects.all()
        try:
            comment = Comment.objects.get(pk=pk)
        except:
            data={'ok': False, 'msg': 'Comment does not exist'}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'GET':
            serializer = CommentSerializer( comment )
            data = {'ok': True, 'data': serializer.data}
            return Response(data, status.HTTP_200_OK)
        elif request.method=='PUT':
            data = JSONParser().parse(request)
            serializer = CommentSerializer(comment, data=data)
            if serializer.is_valid():
                serializer.save()
                data = {'ok': True, 'msg': 'Correctly modified', 'data': serializer.data}
                return Response(data, status.HTTP_200_OK)
            data = {'ok': False, 'msg': 'Could not edit the data', 'errors': serializer.errors}
            return Response(data, status.HTTP_400_BAD_REQUEST)
        else:
            comment.delete()
            data={'ok': True, 'msg': 'Correctly deleted'}
            return Response(data, status.HTTP_202_ACCEPTED)



