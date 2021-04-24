from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, data):
        post = Post.objects.create(
            title=data['title'],
            author=data['author'],
            body=data['body'],
            category=data['category'],
            status=data['status'])
        post.save()
        return post
        
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
    def create(self, data):
        post = Category.objects.create(
            name=data['name'],
            description=data['description']
        )
        post.save()
        return post
    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.save()
        return instance