from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Patient,Investigation
from django.contrib.auth import authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    if request.method=='GET':
        return render(request,'login.html',{'not_authenticate':False})
    elif request.method=='POST':
        _email=request.POST.get('email')
        _password=request.POST.get('password')
        try:
            usernameAuth=User.objects.filter(email=_email)[0]
            user = authenticate(username=usernameAuth.username, password=_password)
            if user is not None:
                 return redirect('getDashboard/'+str(user.id))   
                
        except:
             return render(request,'login.html',{'not_authenticate':False})
          
def getDashboard(request,user_id):
         allInvest=[]
         patienid=Patient.objects.filter(patient=user_id).values('id')[0]
         for invest in Investigation.objects.filter(patient=patienid['id']):
                allInvest.append(invest)
         return render(request,'dashboard.html',{'authenticat':True,'user':user_id,'invests':allInvest})
          

def register(request):
    if request.method=='GET':
        return render(request,'register.html',{'userexist':False})
    elif request.method=='POST':
        
        _username=request.POST.get('name')
        _email=request.POST.get('email')
        _password=request.POST.get('password')
        if len(User.objects.filter(email=_email))>0 or len(User.objects.filter(username=_username))>0:
            return render(request,'register.html',{'userexist':True}) 
        print(len(User.objects.filter(email=_email)))
        p=User(email=_email,username=_username)
        p.set_password(_password)
        p.save()
        patientEntry=Patient(Name=_username,patient=p)
        patientEntry.save()
    # print(_username+" "+email+" "+" "+password)
        return render(request,'login.html')
def uploadInvestication(request):
    file=request.FILES['file']
    title=request.POST.get('title')
    user=request.POST.get('userid')
    userpat=Patient.objects.get(patient=user)
    p=Investigation(patient=userpat,InvestigationTitle=title,InvestigationFile=file,InvestigationDate=datetime.now())
    p.save()
    next = request.POST.get('', '/app/getDashboard/'+str(user))
    return HttpResponseRedirect(next)
    return HttpResponseRedirect('getDashboard/'+str(user))   
 