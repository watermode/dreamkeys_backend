from django.contrib import admin
from .models import Realtor, Listing, ListingImage, Comment

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')  # Пример кастомизации столбцов в admin
    search_fields = ('first_name', 'last_name')

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'created_at')
    search_fields = ('title', 'location')

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ('listing', 'image')
    list_filter = ('listing',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('listing', 'author', 'text', 'created_at')
    search_fields = ('text', 'author__username')

admin.site.register(Realtor)
admin.site.register(Listing)
admin.site.register(ListingImage)
admin.site.register(Comment)
