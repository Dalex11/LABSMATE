from django.test import TestCase
from rest_framework.test import APIClient
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from orders.models import order
from django.contrib.auth.hashers import make_password

# Create your tests here.
class paymentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_payment(self):
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
        payment_data = {
            "date": "2023-08-28T16:17:00Z",
            "method": "Efectivo",
            "pay": 1500000
        }
        response = self.client.post('/payment/payment/', payment_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_retrieve_payment_list(self):
        payment.objects.create(date= "2023-08-28T16:17:00Z",
                                method= "Efectivo",
                                pay= 414243
                                )
        payment.objects.create(date= "2023-08-28T16:17:00Z",
                                method= "Efectivo",
                                pay= 414249
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
        response = self.client.get('/payment/payment/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_update_payment(self):
        payment.objects.create(date= "2023-08-28T16:17:00Z",
                                method= "Efectivo",
                                pay= 414249
                                )
        payment.objects.create(date= "2023-08-28T16:17:00Z",
                                method= "Efectivo",
                                pay= 414249
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
        payment_data = {
            "date": "2023-08-28T16:17:00Z",
            "method": "Carrera 1 calle 1",
            "pay": 414246
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/payment/payment/1/', payment_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_order_payment_list(self):
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
        payment_ship = payment.objects.create(date= "2023-08-28T16:17:00Z",
                                method= "Efectivo",
                                pay= 414249
                                )
        order_payment.objects.create(id_order= order_ship,
                                id_payment= payment_ship
                                )
        order_payment.objects.create(id_order= order_ship,
                                id_payment= payment_ship
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.get('/payment/order_payment/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_update_order_payment(self):
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
        payment_ship = payment.objects.create(date= "2023-08-28T16:17:00Z",
                                method= "Efectivo",
                                pay= 414249
                                )
        order_payment.objects.create(id_order= order_ship,
                                id_payment= payment_ship
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        order_payment_data = {
            "id_order": 1,
            "id_payment": 1
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/payment/payment/1/', order_payment_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)