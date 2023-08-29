from django.test import TestCase
from rest_framework.test import APIClient
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your tests here.
class orderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_order(self):
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
        order_data = {
            "date": "2023-08-28T16:17:00Z",
            "id_user": 1,
            "code": 147852369
        }
        response = self.client.post('/order/order/', order_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_retrieve_order_list(self):
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
        order.objects.create(date= "2023-08-28T16:17:00Z",
                                id_user= usuario,
                                code= 414243
                                )
        order.objects.create(date= "2023-08-28T16:17:00Z",
                                id_user= usuario,
                                code= 414244
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.get('/order/order/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_update_order(self):
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
        order.objects.create(date= "2023-08-28T16:17:00Z",
                                id_user= Usuario,
                                code= 414245
                                )
        order.objects.create(date= "2023-08-28T16:17:00Z",
                                id_user= Usuario,
                                code= 414246
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        order_data = {
            "date": "2023-08-28T16:17:00Z",
            "id_user": 1,
            "code": 147852370
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/order/order/1/', order_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_order_product_list(self):
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
        order_ship = order.objects.create(
                date = "2023-08-28T16:17:00Z",
                code = 48778784,
                id_user = usuario,
                )
        product_ship = product.objects.create(name= "name product",
                                description= "description product",
                                code= 414249,
                                price= 1500000
                                )
        order_product.objects.create(id_order= order_ship,
                                     quantity= 2,
                                id_product= product_ship
                                )
        order_product.objects.create(id_order= order_ship,
                                     quantity= 2,
                                id_product= product_ship
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.get('/order/order_product/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_update_order_product(self):
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
        order_ship = order.objects.create(
                date = "2023-08-28T16:17:00Z",
                code = 48778784,
                id_user = usuario,
                )
        product_ship = product.objects.create(name= "name product",
                                description= "description product",
                                code= 414249,
                                price= 1500000
                                )
        order_product.objects.create(id_order= order_ship,
                                     quantity= 2,
                                id_product= product_ship
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        order_product_data = {
            "id_order": 1,
            "quantity": 5,
            "id_product": 1
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/order/order_product/1/', order_product_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)