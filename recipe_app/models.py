from django.db import models

class Author(models.Model):
  name = models.CharField(max_length = 50)
  bio = models.TextField()


class Recipe(models.Model):
  title = models.CharField(max_length = 30)
  author = foreignkey
  description = models.TextField()
  time_required = models.CharField(max_length = 200)
  instructions = models.TextField()