from django.test import TestCase
from django.urls import reverse
from .models import Product, PythonType, Review
from django.contrib.auth.models import User

# Create your tests here.
class PythonTypeTest(TestCase):
    def test_string(self):
        type=PythonType(pythontypename='laptop')
        self.assertEqual(str(type),type.pythontypename)
    
    def test_table(self):
        self.assertEqual(str(PythonType._meta.db_table),'pythontype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=PythonType(pythontypename='tablet')
        self.prod=Product(productname='Ipad',pythontype=self.type, productprice=800.00)

    def test_string(self):
        self.assertEqual(str(self.prod),self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.pythontype),'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(),40.00)

#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=PythonType.objects.create(pythontypename='laptop')
        self.prod=Product.objects.create(productname='product1', pythontype=self.type, user=self.u, 
        productprice=500.00,productentrydate='2019-04-02', productdescription="some kind of laptop")

    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetails', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_number_of_reviews(self):
        reviews=Review.objects.filter(product=self.prod).count()
        self.assertEqual(reviews, 2)
