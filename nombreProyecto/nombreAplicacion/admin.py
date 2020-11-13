from django.contrib import admin
from .models import Marca
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
	list_display		= ['nombre', 'activo']
	list_display_links	= ['nombre', 'activo']
	list_filter			= ['nombre']
	search_fields		= ['nombre']

admin.site.register(Marca, MarcaAdmin)