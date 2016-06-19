from hello.models import Contact
from rest_framework import serializers

class ContactSerialzier(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('pk','first_name','last_name','email','address','phone_number')