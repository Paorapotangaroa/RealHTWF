from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "author"

class Story(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "story"

class Paragraph(models.Model):
    text = models.CharField(max_length=2000)
    story = models.ForeignKey(Story,on_delete=models.CASCADE)

    def __str__(self):
        return self.story.title + " Paragraph " + str(self.id)
    
    class Meta:
        db_table = "paragraph"
    

class Comment(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=2000)
    story = models.ForeignKey(Story,on_delete=models.CASCADE)

    def __str__(self):
        return self.story.title + " Paragraph " + str(self.id)
    
    class Meta:
        db_table = "comment"
