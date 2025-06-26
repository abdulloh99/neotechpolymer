from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Slider(models.Model):
    rasm = models.ImageField(upload_to="image/")
    Text_tepa = models.TextField(max_length=40)
    Text_katta = models.TextField('Katta Yozuv bolib chiqadi',max_length=40)
    Text_pas = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Bosh Sahifa slideri rasmi va yozuvi"

class shortdesc(models.Model):
    img = models.ImageField(upload_to='image/')
    name = models.TextField(max_length=900)
    
    class Meta:
        verbose_name_plural = "Bosh Sahifa qisqa tanishtiruv yozuv va rasm"

class Product(models.Model):
    name = models.CharField("Mahsulot nomi",max_length=50)
    slug = models.SlugField("URL uchun slug", unique=True, blank=True)
    description = models.TextField("Batafsil malumot",max_length=2000)
    picture = models.ImageField("900x650 o'lchamda surat tavsiya etiladi!",upload_to='product/')
    time = models.TextField("Qurish muddati",max_length=30)
    made = models.TextField("Miqdoi kg",max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Maxsulotlar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
    
class hamkor(models.Model):
    img = models.ImageField(upload_to='hamkorlar/')
    
    class Meta:
        verbose_name_plural = "Hamkorlar"

class aboutus(models.Model):
    img = models.ImageField("961X601 o'lcham tavsiya etiladi",upload_to='image/')
    title = models.TextField("kompaniya nomi",max_length=50)
    desc = models.TextField("Korxona tarixi yoki haqida",max_length=5000)
    # imagebgvideo = models.ImageField("Video orqa foni 1300X550 tavsiya etiladi",upload_to="bg/",blank=True,null=True)
    # video_file = models.FileField("Video fayl", upload_to='videos/',blank=True,null=True)
    class Meta:
        verbose_name_plural = "Korxona haqida rasm va tarixi uchun"

class Yangiliklar(models.Model):
    titl = models.CharField('Sarlavha', max_length=100)
    slug = models.SlugField("URL uchun slug", unique=True, blank=True)
    img = models.ImageField("talab etiladi 850x500 dan yuqori o'lcham", upload_to='nweses/')
    desc = models.TextField('Tavsif 1-surat pasida chiqadi', max_length=10000)
    img2 = models.ImageField("talab etiladi 850x500 dan yuqori o'lcham", upload_to='backgraund/', blank=True)
    desc2 = models.TextField('Tavsif 2 surat pasida chiqadi', max_length=10000, blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titl

    class Meta:
        verbose_name_plural = "Yangiliklar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titl)
        super().save(*args, **kwargs)

    def get_absolute2_url(self):
        return reverse('blog-details',  kwargs={'slug': self.slug})

class Contact(models.Model):
    address = models.TextField(max_length=200)
    Tel = models.TextField('TEl NOMER',max_length=40)
    Tel2 = models.TextField("TEl NOMER2 agar bo'lsa",max_length=40,blank=True)
    facebook = models.TextField(max_length=50)
    insta = models.TextField(max_length=50)
    telegram = models.TextField(max_length=50)
    mail = models.TextField(max_length=50)
    Ishvaqti = models.TextField(max_length=50)
    maps = models.TextField(max_length=500)


    class Meta:
        verbose_name_plural = "KONTAKT INFO"
