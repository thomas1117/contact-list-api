from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

numbersOnly = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')
minimumLength = MinLengthValidator(10,'It can only be 10 decimals')

class Contact(models.Model):
	first_name = models.CharField(max_length=52)
	last_name = models.CharField(max_length=50, blank=True)
	email = models.EmailField(max_length=50, blank=True)
	address = models.CharField(max_length=200, blank=True)
	phone_number = models.CharField(max_length=10, blank=True, validators=[numbersOnly,minimumLength])
