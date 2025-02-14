from django.db import models
from django.contrib.auth.models import User

# Модель для продавцов/риэлторов
class Realtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Привязка к пользователю Django
    phone = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to='realtors/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

# Модель недвижимости
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)  # Связь с риэлтором
    title = models.CharField(max_length=200)  
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.FloatField(help_text="Площадь в квадратных метрах")
    main_photo = models.ImageField(upload_to='listings/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listings/%Y/%m/%d/')

    def __str__(self):
        return f"Фото для {self.listing.title}"

# Модель комментариев
class Comment(models.Model):
    listing = models.ForeignKey(Listing, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user.username}"
