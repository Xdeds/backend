from django.db import models

# Create your models here.
class Category(models.Model):
        title = models.CharField(max_length=255, verbose_name='Название')

        def __str__(self) -> str:
              return self.title
        
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='product_image', verbose_name='Изображение')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
