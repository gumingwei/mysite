from django.db import models
from django.contrib import admin


# Create your models here.
class BlogPost(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_body = models.TextField()
    blog_timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_body', 'blog_timestamp')


admin.site.register(BlogPost, BlogPostAdmin)
