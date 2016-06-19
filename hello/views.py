from rest_framework import generics
from hello.models import Contact
from hello.serializers import ContactSerialzier

class ContactList(generics.ListCreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerialzier

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerialzier


