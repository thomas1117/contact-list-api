from rest_framework import generics
from contact.models import Contact
from contact.serializers import ContactSerialzier

class ContactList(generics.ListCreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerialzier

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerialzier


