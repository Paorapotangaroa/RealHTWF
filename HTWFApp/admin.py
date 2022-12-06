from django.contrib import admin
from .models import Author, Paragraph, Story, Comment

# Register your models here.

admin.site.register(Author)
admin.site.register(Paragraph)
admin.site.register(Story)
admin.site.register(Comment)