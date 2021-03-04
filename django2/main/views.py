from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import Patient, xapi, xapiRaw
from .forms import *
from django.contrib import messages
import matplotlib.pyplot as pl

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = xapiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            choice = ""
            score = 0
            success = False
            response = 0
            if (form.cleaned_data['g']):
                choice+="Gorilla"
                response+=1
            if (form.cleaned_data['d']):
                response+=2
                if ("G" in choice):
                    choice +=", "
                else:
                    choice += "Dolphin"
            if (form.cleaned_data['f']):
                if (0 < response <= 3):
                    response = 4
                    choice +=", Fox"
                else:
                    choice += "Fox"
                    score = 1
                    success = True
                    response=3

            statement = '''{"actor":{"account":{"name":"Jonah",”mbox”:”sparkedscience0@gmail.com,"homePage":"http://sperkedscience.com"},"objectType":"Agent"}, "verb":{"id":"testMC","display":{"en-US":"answered"}}, "object":{"id":"testMC","objectType":"Activity","definition":{"extensions":{"http://h5p.org/x-api/h5p-local-content-id":testMC},"name":{"en-US":"testMC"}}"interactionType":"choice","correctResponsesPattern":"3","choices":[{"id":"1","description":{"en-US":"Gorilla\\n"}},{"id":"2","description":{"en-US":"Dolphin\\n"}},{"id":"3","description":{"en-US":"Fox\\n"}}]}, "context":{"contextActivities":{"category":[{"id":"[LinkToLibrary]”,"objectType":"Activity"}]}}, "result":{"score":{"min":0,"max":1,"raw":'''+str(score)+'''},"completion":[completion],"success":'''+str(success)+''',"response":"'''+choice+'''"}}'''
            raw = xapiRaw(raw=statement)
            raw.save()
            
            xa = xapi(uuid="1", interactionType='answered', objectLink='testMC', localId = 1, objectName='testMC',correct='Fox', answers='[{"id":"0","description":{"en-US":"Dolphin"}},{"id":"1","description":{"en-US":"Gorilla"}},{"id":"2","description":{"en-US":"Fox"}}]', description='What is the best animal?', categoryId='test', minScore=0, maxScore=1, raw=0, scaled=0, completion=True, success=success, response = response)
            xa.save()
            # redirect to a new URL:
            return HttpResponseRedirect("http://sparkedscience.com/stats")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = xapiForm()
    return render(request, 'main/index.html', {'form':form})

def sucess(request):
    return render(request, 'main/sucess.html')
        
def stats(request):
    size = len(xapi.objects.all())
    test = 0
    correct = 0
    incorrect = 0
    dolphin = 0
    gorilla = 0
    fox = 0
    multiple = 0
    for x in xapi.objects.all():
        if (x.response == 1):
            dolphin+=1
            incorrect+=1
        elif (x.response == 2):
            gorilla+=1
            incorrect+=1
        elif (x.response == 3):
            fox+=1
            correct+=1
        elif (x.response > 3):
            incorrect+=1
            multiple+=1
    dolphin = str(dolphin / size * 100)[:5]+'%'
    gorilla = str(gorilla / size * 100)[:5]+'%'
    fox = str(fox / size * 100)[:5]+'%'
    multiple = str(multiple/size*100)[:5]+'%'
    
    labels = 'Correct','Incorrect'
    sizes = [correct, incorrect]
    colors = ['lightskyblue', 'lightcoral']
    explode = (.15, 0)
    pl.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    pl.axis('equal')
    pl.savefig('/home/sparkeds/django2/static/main/plot3.png')
    return render(request, 'main/stats.html', {'data':correct,'dolphin':dolphin, 'gorilla':gorilla, 'fox':fox, 'multiple':multiple}) 
    
def video(request):
    return render(request, 'main/video.html')
    

def scanner(request):
    return render(request, 'main/scanner.html')
    