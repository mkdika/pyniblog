from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


class Category(models.Model):

  category_name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.category_name

  class Meta:
    db_table = 'tb_category' # custom database table name


class Tag(models.Model):

  tag_name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.tag_name

  class Meta:
    db_table = 'tb_tag' # custom database table name


class Post(models.Model):

  permalink   = models.CharField(max_length=255, unique=True)
  title       = models.CharField(max_length=255)
  post_date   = models.DateTimeField()
  post_body   = RichTextField()
  release     = models.BooleanField(default=False)
  user        = models.ForeignKey(User,on_delete=models.CASCADE)
  category    = models.ForeignKey(Category,on_delete=models.PROTECT)
  tags        = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'tb_post'


class PostComment(models.Model):

  name          = models.CharField(max_length=50)
  email         = models.CharField(max_length=100,blank=True)
  comment_body  = RichTextField()
  comment_date  = models.DateTimeField(default=datetime.now)
  post          = models.ForeignKey(Post,on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.post} (by: {self.name})"

  class Meta:
    db_table = 'tb_post_comment' 
