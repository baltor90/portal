from django.db import models


# Create your models here.
class lisans_kod(models.Model):
    lisans=models.CharField(("Lisans Kodu"),max_length=150)
    
class kullanici(models.Model):
    
    isim=models.CharField(("adı"),max_length=50)
    soyad=models.CharField(("soy adı"),max_length=50)
    email=models.EmailField(("email"),max_length=50)
    username=models.CharField(("kullanıcı adı"),max_length=50)
    telno=models.CharField(("telefon no"),max_length=50)
    odeme=models.BooleanField(("ödeme yaptı"))
    lisans=models.CharField(("lisans kodu"),max_length=50)
class portalgo(models.Model):
    dosya=models.FileField(("protalgo yükleme dosyası"),upload_to=None,max_length=200)

class sayfaDuzenleme(models.Model):
    anayazi=models.CharField(("yazılacak yazı"),max_length=200)
    
class menuDuzen(models.Model):
    menu=models.CharField(("menü adı"),max_length=20)
class geciciKullanici(models.Model):
    isim=models.CharField(("adı"),max_length=50)
    soyad=models.CharField(("soy adı"),max_length=50)
    email=models.EmailField(("email"),max_length=50)
    username=models.CharField(("kullanıcı adı"),max_length=50)
    telno=models.CharField(("telefon no"),max_length=50)
    odeme=models.BooleanField(("onaylandı"))
class kullaniciPaneli(models.Model):
    
    email=models.CharField(("email"),max_length=50)
    kullaniciadi=models.CharField(("kullanıcı adı"),max_length=50)
    parola=models.CharField(("parola"),max_length=25)

    