from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    uid = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES= (
        ('draft', 'Draft'),
        ('published','Published'),
    )
    uid = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(_("Estado"), max_length=10, choices=STATUS_CHOICES, default='draft')
    
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    uid = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=150)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        