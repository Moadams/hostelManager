from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, time
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save,pre_save
from decimal import  Decimal
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 13)
    hostel_managed = models.CharField(max_length = 200)
    profile_picture = models.ImageField(upload_to = 'profile_pics', default = 'profile_pics/avatar3.jpeg')

    def __str__(self):
        return self.user.username

class Room(models.Model):
    ROOM_TYPE = (
        ('One in One','One in One'),
        ('Two in One','Two in One'),
        ('Three in One','Three in One'),
        ('Four in One','Four in One'),
    )
    room_number = models.CharField(max_length = 5)
    block = models.CharField(max_length = 50, blank = True)
    room_type = models.CharField(max_length = 12, choices = ROOM_TYPE)
    spaces_available = models.PositiveIntegerField(default = 0)
    price_per_bed = models.DecimalField(default = 0.00,max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Room {self.room_number} ({self.room_type})'


class Worker(models.Model):
    name = models.CharField(max_length = 50)
    position = models.CharField(max_length = 100)
    salary = models.DecimalField(default = 0.00, decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name


class Occupant(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    student_number = models.CharField(max_length = 8, blank = True)
    phone = models.CharField(max_length = 13)
    email = models.EmailField()
    room_occupied = models.ForeignKey(Room,on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=7,decimal_places=2,default = 0.00)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_balance(self):
        if self.amount_paid < self.room_occupied.price_per_bed:
            balance = Decimal(self.room_occupied.price_per_bed) - Decimal(self.amount_paid)
        else:
            balance = 0 
        return balance

@receiver(post_delete,sender = Occupant)
def delete_occupant(sender,instance,**kwargs):
    room = instance.room_occupied
    room.spaces_available += 1
    room.save()


@receiver(pre_save,sender = Occupant)
def save_occupant(sender, instance, **kwargs):
    room = instance.room_occupied
    occupants = Occupant.objects.all()
    print(occupants)
    if instance in occupants:
        print('It is inside')
    elif instance not in occupants:
        print("It is not in")
        room.spaces_available -= 1
    room.save()