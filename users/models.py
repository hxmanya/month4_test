from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    phone_number = models.CharField(max_length=14)
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=10, choices=GENDER, default='Male')
    club = models.CharField(max_length=100, default='Клуб не определен')
    
    def save(self, *args, **kwargs):
        if self.age < 5:
            self.club  = 'Вы слишком малы'
        elif 5 <= self.age <=10:
            self.club = 'Детский клуб'
        elif 11 <= self.age <=18:
            self.club = 'Подростковый'
        elif 19 <= self.age <=45:
            self.club = 'Взрослый'
        else:
            self.club = 'Ваш возраст составляет больше 45 вы не подходите'
        
        super().save(*args, **kwargs)
    
   