from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from grocery.models import Category, Product, Favorite


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

class DetailPageTestCase(TestCase):
    def setUp(self):
        categ = Category.objects.create(name='pate')
        impossible = Product.objects.create(name='nutella', nutrigrade='a', image='url.htt', url='url.htt', nutrient='url.htt', category=categ)
        self.product = Product.objects.get(name='nutella')

    # test that detail page returns 200 if the item exists
    def test_detail_page_returns_200(self):
        
        product = self.product.id
        response = self.client.get(reverse('detail', args=(product,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns 404 if the item exists
    def test_detail_page_returns_404(self):
        product = self.product.id + 1000
        response = self.client.get(reverse('detail', args=(product,)))
        self.assertEqual(response.status_code, 404)