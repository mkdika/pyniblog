from django.test import TestCase
from hamcrest import *
import unittest
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category, Tag


class IndexTest(TestCase):

  def setUp(self):

    pass

  def test_index_page(self):

    response = self.client.get('/')
    assert_that(response.status_code, equal_to(200))

  def test_index_page_not_int(self):

    response = self.client.get(reverse('index')+'?page=abc')
    assert_that(response.status_code, equal_to(200))

  def test_index_page_empty(self):

    response = self.client.get(reverse('index'))
    assert_that(response.status_code, equal_to(200))

  def tearDown(self):

    pass    


class PostTest(TestCase):

  def setUp(self):

    category = Category.objects.create(category_name="java")
    user = User.objects.create(username="maikel")
    Post.objects.create(title="Hello World", category=category,user=user, permalink="hello-world")

  def test_post_page(self):

    response = self.client.get('/posts/hello-world')
    assert_that(response.status_code, equal_to(200))  


class AboutTest(TestCase):

  def setUp(self):

    pass

  def test_about_page(self):

    response = self.client.get('/about')
    assert_that(response.status_code, equal_to(200))  
    

class ArchiveTest(TestCase):

  def setUp(self):

    pass

  def test_archive_year(self):

    response = self.client.get('/archives/year')
    assert_that(response.status_code, equal_to(200))  


  def test_archive_categories(self):

    response = self.client.get('/archives/categories')
    assert_that(response.status_code, equal_to(200))  


class SearchTest(TestCase):

  def setUp(self):

    tag = Tag.objects.create(tag_name="tutorial")
    category = Category.objects.create(category_name="java")
    user = User.objects.create(username="maikel")
    post = Post.objects.create(title="Hello World", category=category,user=user,
                        permalink="hello-world")
    post.tags.create(tag_name="poc")                    

  def test_search_users(self):

    response = self.client.get('/posts/users/maikel')
    assert_that(response.status_code, equal_to(200))  

  def test_search_categories(self):  

    response = self.client.get('/posts/categories/java')
    assert_that(response.status_code, equal_to(200))  

  def test_search_tags(self):  

    response = self.client.get('/posts/tags/tutorial')
    assert_that(response.status_code, equal_to(200))  
