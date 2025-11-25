from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)
    bio = models.TextField(max_length=500, verbose_name='Биография', blank=True)
    location = models.CharField(max_length=100, verbose_name='Местоположение', blank=True)
    interests = models.CharField(max_length=255, verbose_name='Интересы', blank=True)

    def __str__(self):
        return f'Профиль {self.user.username}'

class Match(models.Model):
    user1 = models.ForeignKey(User, related_name='matches_as_user1', on_delete=models.CASCADE, verbose_name='Пользователь 1')
    user2 = models.ForeignKey(User, related_name='matches_as_user2', on_delete=models.CASCADE, verbose_name='Пользователь 2')
    matched_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата совпадения')
    is_mutual = models.BooleanField(default=False, verbose_name='Взаимное совпадение')

    def __str__(self):
        return f'Совпадение между {self.user1} и {self.user2}'

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, verbose_name='Отправитель')
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, verbose_name='Получатель')
    content = models.TextField(verbose_name='Сообщение')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')

    def __str__(self):
        return f'Сообщение от {self.sender} к {self.receiver}'