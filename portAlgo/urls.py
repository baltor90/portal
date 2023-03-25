"""portAlgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proje.views import *


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',index),
    path('index.html',index),
    path('SATIN-AL.html',satinal),
    path('yenideneme.html',deneme),
    path('KULLANICI.html',kullanici_panel),
    path('giris-kayit.html',giriskayit),
    path('kayitOl',kayitOL),
    path('u613',panelyon),
    path('uyeYon',panelyon),
    path('res',resimvideo),   
]
