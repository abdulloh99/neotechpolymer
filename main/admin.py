from django.contrib import admin
from .models import *

admin.site.register(Slider)
admin.site.register(shortdesc)
admin.site.register(aboutus)
@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('titl','time')
    prepopulated_fields = {"slug": ("titl",)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'time', 'made')
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(hamkor)
admin.site.register(Contact)
