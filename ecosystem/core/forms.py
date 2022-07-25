from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    firstname= forms.CharField(label=' First Name' ,widget=forms.TextInput(attrs={'placeholder':"John",'class':'form-control'}))
    lastname= forms.CharField(label='Last Name' ,widget=forms.TextInput(attrs={'placeholder':"Doe",'class':'form-control'}))

    myemail= forms.EmailField(label='Email' ,widget=forms.EmailInput(attrs={'placeholder':"Enter your email",'class':'form-control'}))
    phone= forms.IntegerField(label='Phone Number' ,widget=forms.NumberInput(attrs={'placeholder':"enter phone number",'class':'form-control'}))
    message= forms.CharField(label='Message' ,widget=forms.TextInput(attrs={'placeholder':"Enter a message",'class':'form-control','size': 10, 'title': 'Message'}))
    class Meta:
        model= Message
        fields = '__all__'
    

    

