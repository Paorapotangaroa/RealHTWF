from django.urls import path
from .views import index,background,stories,story
urlpatterns = [
    path("",index,name="index"),
    path("background",background,name="background"),
    path("stories",stories,name="stories"),
    path("story/<int:id>",story,name="story"),
]