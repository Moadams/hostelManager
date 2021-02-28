from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Creating a BaseForm that assigns all the fields in the form to the form-control class

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'





# Creating a Form used to create a new user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

# Creating a form to add a new worker
class WorkerForm(BaseForm,ModelForm):
    class Meta:
        model = Worker
        fields = [
            'name',
            'position',
            'salary'
        ]

# Creating a form to add a new occupant
class OccupantForm(BaseForm,ModelForm):
    class Meta:
        model = Occupant
        fields = [
            'first_name',
            'last_name',
            'student_number',
            'phone',
            'email',
            'room_occupied',
            'amount_paid'
        ]


# Creating a form to add a new room
class RoomForm(BaseForm,ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_number',
            'room_type',
            'block',
            'spaces_available',
            'price_per_bed'
        ]