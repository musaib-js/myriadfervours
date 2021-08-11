from django.contrib import admin
from .models import Post
from .models import BlogComment

admin.site.register((BlogComment))

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)