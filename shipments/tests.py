from django.test import TestCase
from rest_framework.test import APIClient
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from orders.models import order
from django.contrib.auth.hashers import make_password

# Create your tests here.
class shipmentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_shipment(self):
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
        shipment_data = {
            "date": "2023-08-28T16:17:00Z",
            "address": "Carrera 1 calle 1",
            "city": "Cali",
            "department": "Valle",
            "country": "Colombia",
            "code": 414246,
            "state": "sent"
        }
        response = self.client.post('/shipment/shipment/', shipment_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_retrieve_shipment_list(self):
        shipment.objects.create(date= "2023-08-28T16:17:00Z",
                                address= "Carrera 1 calle 1",
                                city= "Cali",
                                department= "Valle",
                                country= "Colombia",
                                code= 414249,
                                state= "sent"
                                )
        shipment.objects.create(date= "2023-08-28T16:17:00Z",
                                address= "Carrera 1 calle 1",
                                city= "Cali",
                                department= "Valle",
                                country= "Colombia",
                                code= 414248,
                                state= "sent"
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
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.get('/shipment/shipment/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_update_shipment(self):
        shipment.objects.create(date= "2023-08-28T16:17:00Z",
                                address= "Carrera 1 calle 1",
                                city= "Cali",
                                department= "Valle",
                                country= "Colombia",
                                code= 414249,
                                state= "sent"
                                )
        shipment.objects.create(date= "2023-08-28T16:17:00Z",
                                address= "Carrera 1 calle 1",
                                city= "Cali",
                                department= "Valle",
                                country= "Colombia",
                                code= 414248,
                                state= "sent"
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
        shipment_data = {
            "date": "2023-08-28T16:17:00Z",
            "address": "Carrera 1 calle 1",
            "city": "Cali",
            "department": "Valle",
            "country": "Colombia",
            "code": 414246,
            "state": "sent"
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/shipment/shipment/1/', shipment_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 8)

    def test_retrieve_order_shipment_list(self):
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
        shipment_ship = shipment.objects.create(date= "2023-08-28T16:17:00Z",
                                address= "Carrera 1 calle 1",
                                city= "Cali",
                                department= "Valle",
                                country= "Colombia",
                                code= 414249,
                                state= "sent"
                                )
        order_shipment.objects.create(id_order= order_ship,
                                id_shipment= shipment_ship
                                )
        order_shipment.objects.create(id_order= order_ship,
                                id_shipment= shipment_ship
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.get('/shipment/order_shipment/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_order_shipment(self):
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
        shipment_ship = shipment.objects.create(date= "2023-08-28T16:17:00Z",
                                address= "Carrera 1 calle 1",
                                city= "Cali",
                                department= "Valle",
                                country= "Colombia",
                                code= 414249,
                                state= "sent"
                                )
        order_shipment.objects.create(id_order= order_ship,
                                id_shipment= shipment_ship
                                )
        login_data = {
            "username": "prueba",
            "password": "prueba",
        }
        order_shipment_data = {
            "id_order": 1,
            "id_shipment": 1
        }
        token = self.client.post("/sign/login/", login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['token'])
        response = self.client.put('/shipment/shipment/1/', order_shipment_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 8)