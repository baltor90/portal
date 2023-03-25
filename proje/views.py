from django.shortcuts import render
from .models import *
from django import forms

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def satinal(request):
    
    return render(request,'SATIN-AL.html')
def deneme(request):
       isimi= kullanici.objects.get(id="1")
       filitre=kullanici.objects.get(isim="ahmet")
       kullan=kullanici.objects.all()
       yazi="yazi buraya gelecek"
       if request.method=="POST":
           yen=request.POST
           yazi=yen["gonderi"]
                  
           
           
       selam="merhaba"
       
       
       
      
       context={"yazamk":yazi,
        "isim":isimi,
        "fil":filitre,"kullan":kullan}
       return render(request,"yenideneme.html",context)
    
def kullanici_panel(request):
    
    return render(request,"KULLANICI.html")
def giriskayit(request):
    
        
    return render(request,"giris-kayit.html")
def kayitAlindi(request):
    
    return render("kayitAlindi.html")
def kayitOL(request):
    name=request.POST
    print(name)
    return render(request,"kayitAlindi.html")


def panelyon(request):
    
    isimi= kullanici.objects.get(id="1")
    filitre=kullanici.objects.get(isim="ahmet")
    kullan=kullanici.objects.all()
    uyelik=""
    if request.method=="POST":
        yeni=request.POST
        uyeYonet=yeni['yenilik']
        if uyeYonet=='uyeyonet':
        
            uyelik=kullanici.objects.all()
        
        
    
    a=0
   
    for i in kullan:
        uyesayisi=a
        a=a+1
    context={
        "kullan":kullan,"uyesayisi":uyesayisi,"uyelik":uyelik,
    }
    return render(request,"yonetim-panel.html",context)
# def uyeYon(request):
    
#     uyelik=kullanici.objects.all()
    
#     context={"uyelik":uyelik,
        
#     }
#     return render(request,"yonetim-panel.html",context)
def resimvideo(request):
    
    
    return render(request,"resim-video-yon.html")