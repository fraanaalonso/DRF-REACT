from rest_framework import serializers
from .models import Post, Category, Comment


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

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.author = data.get('author', instance.author)
        instance.body = data.get('body', instance.body)
        instance.category = data.get('category', instance.category)
        instance.status = data.get('status', instance.status)
        instance.save()
        return instance
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, data):
        comment = Comment.objects.create(
            title=data['title'],
            author=data['author'],
            body=data['body'],
            post=data['post']
        )
        comment.save()
        return comment

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.author = data.get('author', instance.author)
        instance.body = data.get('body', instance.body)
        instance.post = data.get('post', instance.post)
        instance.save()
        return instance



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
