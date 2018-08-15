from django.test import TestCase
from .models import Category, Tag

class CategoryTest(TestCase):
  def setUp(self):
    Category.objects.create(category_name="java")

  def test_category_name(self):
    java = Category.objects.get(category_name="java")
    self.assertEqual(java.category_name,"java")


class TagTest(TestCase):
  def setUp(self):
    Tag.objects.create(tag_name="tutorial")

  def test_tag_name(self):
    tutorial = Tag.objects.get(tag_name="tutorial")
    self.assertEqual(tutorial.tag_name,"tutorial")  