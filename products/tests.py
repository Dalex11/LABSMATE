from django.test import TestCase
from rest_framework.test import APIClient
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from orders.models import order
from django.contrib.auth.hashers import make_password

# Create your tests here.
class productAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        Usuario = User.objects.create(
                password = make_password("prueba"),
                is_superuser = False,
                username = "prueba",
                first_name = "prueba",
                last_name = "prueba",
                email = "prueba@prueba.com",
                is_staff = False,
                is_active = True
                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        product_data = {
            "name": "Product test",
            "description": "Description test",
            "code": 159357456,
            "price": 1500000
        }
        response = self.client.post('/product/product/', product_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_retrieve_product_list(self):
        product.objects.create(name= "Product test",
                                description= "Description test",
                                code= 159357457,
                                price= 1500000
                                )
        product.objects.create(name= "Product test",
                                description= "Description test",
                                code= 159357458,
                                price= 1500000
                                )
        usuario = User.objects.create(
                password = make_password("prueba"),
                is_superuser = False,
                username = "prueba",
                first_name = "prueba",
                last_name = "prueba",
                email = "prueba@prueba.com",
                is_staff = False,
                is_active = True
                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.get('/product/product/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_update_product(self):
        product.objects.create(name= "Product test",
                                description= "Description test",
                                code= 159357459,
                                price= 1500000
                                )
        product.objects.create(name= "Product test",
                                description= "Description test",
                                code= 159357460,
                                price= 1500000
                                )
        Usuario = User.objects.create(
                password = make_password("prueba"),
                is_superuser = False,
                username = "prueba",
                first_name = "prueba",
                last_name = "prueba",
                email = "prueba@prueba.com",
                is_staff = False,
                is_active = True
                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        product_data = {
            "name": "Product test",
            "description": "Description test",
            "code": 159357461,
            "price": 1500000
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/product/product/1/', product_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)