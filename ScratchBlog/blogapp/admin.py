'''
Created on Oct 15, 2013

@author: toant
'''
from django.contrib import admin
from blogapp.models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
  
admin.site.register(Post, PostAdmin)