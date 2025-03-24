from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import MenuItem, Booking

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_get_menu(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)

    def test_create_booking(self):
        data = {"table_number": 5, "date": "2025-05-20", "time": "18:00", "guests": 4}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, 201)
