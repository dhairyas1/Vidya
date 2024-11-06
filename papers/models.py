from django.db import models
import cloudinary
import cloudinary.uploader
from django.contrib.auth.models import User
from django.conf import settings

class ResearchPaper(models.Model):
  title = models.CharField(max_length = 300)
  author = models.CharField(max_length = 200)
  abstract = models.TextField()
  file = models.FileField(upload_to = "papers/")
  created_at= models.DateTimeField(auto_now_add= True)
  upvotes = models.PositiveIntegerField(default=0)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if self.file:
      uploaded_file = cloudinary.uploader.upload(self.file, resource_type= "raw")
      self.file= uploaded_file['url']
      print(self.file)
    super().save(*args,**kwargs)


class Comment(models.Model ):
  paper = models.ForeignKey(ResearchPaper, related_name='comments',   on_delete=models.CASCADE)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

