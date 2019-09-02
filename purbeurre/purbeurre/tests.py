""" Python testing file checking each page returns the correct response"""
from django.test import TestCase
from django.urls import reverse
# from django.contrib.auth.models import User
from grocery.models import Category, Product

# Homepage
class IndexPageTestCase(TestCase):
    """ Class Test that the function returns the home page with response 200 """
    def test_index_page(self):
        """ Test that the function returns the home page with response 200 """
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

# Detail page
class DetailPageTestCase(TestCase):
    """ Create an object and its instance """
    def setUp(self):
        categ = Category.objects.create(name='pate')
        product = Product.objects.create(name='nutella', nutrigrade='a', image='url.htt',\
        url='url.htt', nutrient='url.htt', category=categ)
        self.product = Product.objects.get(name='nutella')

    # test that detail page returns 200 if the item exists
    def test_detail_page_returns_200(self):
        """ Test that the function returns the detail page with response 200 """
        product = self.product.id
        response = self.client.get(reverse('detail', args=(product,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns 404 if the item exists
    def test_detail_page_returns_404(self):
        """ Test that the function returns the error page with response 404 """
        product = self.product.id + 1000
        response = self.client.get(reverse('detail', args=(product,)))
        self.assertEqual(response.status_code, 404)

# # favorite page
# class FavoritePageTestCase(TestCase):

#     def setUp(self):
#         User =
