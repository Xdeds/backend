from django.contrib import admin
from apps.main.models import Product, Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)