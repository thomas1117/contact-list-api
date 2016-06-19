from rest_framework import generics
from hello.models import Contact
from hello.serializers import ContactSerialzier

class ContactList(generics.ListCreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerialzier

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerialzier
# from django.shortcuts import render
# from django.http import HttpResponse

# from hello.models import Greeting

# # Create your views here.
# def index(request):
#     # return HttpResponse('Hello from Python!')
#     return render(request, 'index.html')


# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, 'db.html', {'greetings': greetings})

