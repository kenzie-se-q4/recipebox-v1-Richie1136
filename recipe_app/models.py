from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=50)
  bio = models.TextField()


class Recipe(models.Model):
  title = models.CharField(max_length=30)
  description = models.TextField()
  time_required = models.CharField(max_length=40)
  instructions = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)