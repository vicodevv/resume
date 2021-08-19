from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact


def index(request):
    if request.method == 'POST':
        contact = Contact()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        message = request.POST.get('message')
        contact.first_name = first_name
        contact.last_name = last_name
        contact.message = message
        contact.save()
        return HttpResponse("<h1>Thank you for your message!, I'll get back to you shortly.</h1>")
    return render(request, 'base/index.html', {})