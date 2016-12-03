from django.contrib import admin
from django.db import models
from django import forms

# Register your models here.
##########################################################################
<<<<<<< HEAD
from .models import FAQ, Noticia, Trabalho, Dia, Endereco
=======
from .models import FAQ, Noticia, Trabalho, Dias, Endereco, Tags
>>>>>>> yanvictords-master

class FAQAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(
                       attrs={'rows': 5,
                              'cols': 40})}
    }

admin.site.register(FAQ, FAQAdmin)
##########################################################################
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(
                       attrs={'rows': 5,
                              'cols': 40})}
    }

admin.site.register(Noticia, NoticiaAdmin)
##########################################################################
admin.site.register(Trabalho)
admin.site.register(Dia)
admin.site.register(Endereco)
admin.site.register(Tags)
