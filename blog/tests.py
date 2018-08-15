from django.test import TestCase
from hamcrest import *
import unittest
from unittest.mock import MagicMock
from django.contrib.auth.models import User
from .models import Category, Tag, Post, PostComment

class CategoryTest(TestCase):
  def setUp(self):
    Category.objects.create(category_name="java")

  def test_category_name(self):
    java = Category.objects.get(category_name="java")
    assert_that(str(java),equal_to("java"))


class TagTest(TestCase):
  def setUp(self):
    Tag.objects.create(tag_name="tutorial")

  def test_tag_name(self):
    tutorial = Tag.objects.get(tag_name="tutorial")
    assert_that(str(tutorial),equal_to("tutorial"))


class PostTest(TestCase):
  def setUp(self):
    category = Category.objects.create(category_name="java")
    user = User.objects.create(username="maikel")
    Post.objects.create(title="Hello World", category=category,user=user)

  def test_post_title(self):
    hello_world = Post.objects.get(title="Hello World")
    assert_that(str(hello_world),equal_to("Hello World"))


class PostCommentTest(TestCase):
  def setUp(self):
    category = Category.objects.create(category_name="java")
    user = User.objects.create(username="maikel")
    post = Post.objects.create(title="Hello World", category=category,user=user)
  
    PostComment.objects.create(name="maikel",comment_body="test",post=post)

  def test_post_comment_name(self):
    post_comment = PostComment.objects.get(name="maikel")
    assert_that(str(post_comment), equal_to("Hello World (by: maikel)"))
