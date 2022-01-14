# Importing Django Admin 
from django.contrib import admin

# Importing DB Models
from blog.models import Tag, Post

# Configuring Some Models

class postAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("title",)}
  list_display = ('slug', 'published_at')



# Registering models.

admin.site.register(Tag)
admin.site.register(Post, postAdmin)