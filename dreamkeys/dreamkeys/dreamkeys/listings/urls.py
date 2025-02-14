from django.urls import path
from .views import listing_list, listing_detail, listing_create, listing_update, listing_delete

urlpatterns = [
    path('', listing_list, name='listing_list'),  # Список объявлений
    path('<int:pk>/', listing_detail, name='listing_detail'),  # Детали одного объявления
    path('new/', listing_create, name='listing_create'),  # Страница для создания нового объявления
    path('<int:pk>/edit/', listing_update, name='listing_update'),  # Страница для редактирования объявления
    path('<int:pk>/delete/', listing_delete, name='listing_delete'),  # Страница для удаления объявления
]


