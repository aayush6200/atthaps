from urllib import request
from django.shortcuts import render
from.models import Post
from django.views.generic import DetailView,ListView
from bs4 import BeautifulSoup
import requests
from googletrans import Translator, constants
from pprint import pprint
import gtts
from playsound import playsound
import os

def trans(request):
    
    if request.method=="POST":
        l=request.POST['to-be']
        translator=Translator()
        translated_text = translator.translate(l,dest='es')
        mytext=translated_text.text
        key={
            "val": l,
            "keys":mytext,

        }
        return render(request,"myApp/home.html",context=key)




'''def sub(*args):
    result_place=Element('output') 
    translator = Translator()
    translated_text = translator.translate(Element('lang-from').value,dest='hi')
    mytext=translated_text.text
    result_place.write(f"<p> the translation of {Element('lang-from').value} is {mytext}")'''




'''class HomeView(ListView):
    model=Post
    template_name="myApp/timeline.html"'''