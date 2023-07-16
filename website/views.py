from django.shortcuts import render , HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm , NewsletterForm
from django.contrib import messages
# Create your views here.


def index_view(request):
    return render(request, 'website/index.html')
    
def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = 'unknown'
            instance.save()
            messages.add_message(request,messages.SUCCESS,'your ticket was successfully')
    else:
        messages.add_message(request,messages.ERROR,'Invalid ticket')
    form = ContactForm()
    return render(request, 'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')