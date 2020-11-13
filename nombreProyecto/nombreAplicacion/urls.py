from django.urls import path
from . import views
# primra ruta para la aplicación
urlpatterns = [ 
	path('plantilla', views.plantilla, name='plantilla'),
	path('marca', views.marca, name='marca'),
	path('registro', views.registro, name='registro'),
	path('ajaxTestPlantilla', views.ajaxTestPlantilla, name='ajaxTestPlantilla'),
	path('ajaxTest', views.ajaxTest, name='ajaxTest'),
	path('marcaForm', views.marcaForm, name='marcaForm'),
	path('mail', views.mail, name='mail'),
]
# 127.0.0.1:8000/plantilla
# 127.0.0.1:8000/marca