from django.test import TestCase
from django.contrib.auth.models import User
from .models import Listing, Realtor

class ListingTests(TestCase):
    def setUp(self):
        # Создаем пользователя и риэлтора, чтобы использовать их в тестах
        user = User.objects.create_user(username="testuser", password="password")
        realtor = Realtor.objects.create(user=user, phone="123456789", description="Test Realtor")

        # Создание объявления
        self.listing = Listing.objects.create(
            realtor=realtor,
            title="Test Listing",
            description="This is a test listing.",
            price=100.00,
            city="Test City",
            address="Test Address",
            bedrooms=2,
            bathrooms=1,
            area=50.0,
            main_photo="path/to/photo.jpg"  # Убедитесь, что тестовый путь до фото существует
        )

    def test_listing_create(self):
        # Проверка, что созданное объявление корректно
        listing = self.listing
        self.assertEqual(listing.title, "Test Listing")
        self.assertEqual(listing.price, 100.00)
        self.assertEqual(listing.city, "Test City")
        self.assertEqual(listing.address, "Test Address")
        self.assertEqual(listing.bedrooms, 2)
        self.assertEqual(listing.bathrooms, 1)
        self.assertEqual(listing.area, 50.0)
        self.assertTrue(listing.realtor)  # Проверка связи с риэлтором

    def test_listing_str(self):
        # Тест метода __str__ для модели Listing
        self.assertEqual(str(self.listing), "Test Listing")
