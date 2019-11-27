from django.shortcuts import render
import geoip2.database
import random
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import datetime
from django.db.models import Count


#from django.contrib.gis.utils import GeoIP
#from django.contrib.gis.geoip import GeoIP
# Create your views here.
def home(request):
    return render(request,"appname/home.html")

def code_generator(request):
    

    code=random.randint(111111,999999)
    url=request.POST.get('urlbox','')
    date=datetime.date.today()

    data=Urlcode()
    data.code=code
    data.url=url
    data.create_date=date
    data.save()
    msg="Your code is created. And the code is:"+str(code)
    return render(request,'appname/home.html',{'msg':msg})


def redirecturl(request,code):
    
    if code[-1]=="+":
        code=code[0:6]
        dd=Clientdetail.objects.filter(code=code).count()
        

        detail=Clientdetail.objects.filter(code = code).values('date').annotate(event_count = Count('id'))
        return render(request,'appname/detail.html',{'detail':detail,'dd':dd,"code":code})

    else:
        data=Urlcode.objects.filter(code=code).values('url')
        url=data[0]['url']
        
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            
        else:
            ip = request.META.get('REMOTE_ADDR')
            
        os=request.user_agent.os.family
        browser=request.user_agent.browser.family
        

        redear=geoip2.database.Reader('./GeoLite2-Country_20191126/GeoLite2-Country.mmdb')
        try:
            country=redear.country(ip)
        except:
            country="Local Area"    
        redear.close()
        date=datetime.date.today()
        time=datetime.datetime.now().time()

        cd=Clientdetail()
        cd.code=code
        cd.ip=ip
        cd.os=os
        cd.browser=browser
        cd.date=date
        cd.time=time
        cd.country=country
        cd.save()
        
        return HttpResponseRedirect("https://google.com/")


def Dashboard(request):
    url_table=Urlcode.objects.all()

    cd=Clientdetail.objects.all()
    return render(request,'appname/dashboard.html',{'url_table':url_table,'cd':cd})



