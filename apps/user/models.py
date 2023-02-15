from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', 
    null=True, blank=True)
    is_confirm_email = models.BooleanField(default = False) 


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self) -> str:
        return f'EmailVerification for{self.user.email}'
    
    def send_mail_verification(self):
        link = f'/user/email_verification/{self.user.email}/{self.code}'
        verification_link = f'127.0.0.1:8000/{link}'
        subject = f'Подтверждение почты{self.user.email}'
        message = f'Для подтверждение почты перейдите по ссылке{verification_link}'
        send_mail(
            subject,
            message,
            'xdedq@yandex.ru',
            recipient_list=[self.user.email],
            fail_silently=False,
        )
    def is_expiration(self) -> bool:
        return True if timezone.now() < self.expiration else False