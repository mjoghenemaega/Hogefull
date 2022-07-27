from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic import View, CreateView

from ecosystem.newsletter.forms import JoinForm
from .forms import MessageForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    form =JoinForm(request.POST or None)
    mymessage =MessageForm(request.POST or None)
    success_url ='/'
    firstname= request.POST.get ('firstname')
    lastname= request.POST.get('lastname')
    myemail= request.POST.get('myemail')
    phone= request.POST.get('phone')
    message=request.POST.get('message')

    context ={
        'form':form,
        'mymessage':mymessage
    }
    
    
    if form.is_valid():
        email= form.save()
        template=render_to_string('newsletter.html',{'form': form})
        newsletter = EmailMessage(
        'Thank you Suscribing to our Newsletter',
        template,
        settings.EMAIL_HOST_USER,
        [email],
        message.attach_file('https://hogefinance.herokuapp.com/static/images/h2.jpg')
        
            
        )
        newsletter.fail_silently =False
        newsletter.send()

        return redirect('home')
    




     
    
 
    if mymessage.is_valid():
        mymessage= mymessage.save() 
        template=render_to_string('email.html',{'form': form,'firstname':firstname})
        
        register= EmailMessage(
            'Thanks for signing up',
            template,
            settings.EMAIL_HOST_USER,
            [myemail],
            
            
        )
        register.fail_silently =False
        register.send()

        return redirect('home')
      
      
    return render(request, 'home.html',context) 





def about(request):
    return render(request, 'about.html')    


def media(request):
    return render(request, 'media.html')     


def store(request):
    return render(request, 'store.html')    
