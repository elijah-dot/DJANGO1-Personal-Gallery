from django.test import TestCase
from .models import Photo, Category
# Create your tests here.

class CategoryTestCase(TestCase):
     
    def setUp(self):
        self.category = Category(category = 'Person')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
        
    def test_save_categories(self):
        self.category.save_category()
        all_categories = Category.objects.all()
        self.assertTrue(len(all_categories) > 0)
        
    def test_search_category(self):
        self.category.save_category()
        images = Category.objects.filter(category__icontains='person')
        self.assertTrue(self.category, images)
