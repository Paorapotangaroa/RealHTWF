from django.shortcuts import render
from .models import Author, Paragraph, Story, Comment

# Write story

# Create your views here.
def index(request):
    return render(request,"HTWFApp/index.html")

def stories(request):
    data = Story.objects.all()
    context={
        "data": data
    }
    return render(request,"HTWFApp/stories.html",context)

def background(request):
    return render(request,"HTWFApp/background.html")

def story(request,id):
    data = Paragraph.objects.filter(story=id)
    story = Story.objects.get(id=id)
    context={
        "data": data,
        "story": story
    }
    return render(request,"HTWFApp/story.html",context)