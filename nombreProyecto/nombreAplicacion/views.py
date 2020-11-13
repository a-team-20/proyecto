from django.shortcuts import render
from nombreAplicacion.models import Marca
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core import serializers
from django.http import JsonResponse
from .forms import MarcaForm

# Create your views here.

def mail(request):
	#from django.core.mail import send_mail
#	send_mail(    'Subject here',    'Here is the message.',    'sistemadeenviodecorreos@gmail.com',    ['patricioyanez@live.cl'],
 #   fail_silently=False,)
return render(request, 'mail.html', {})
	
def plantilla(request):
	return render(request, 'plantillaEjemplo.html', {})

def marcaForm(request):
	#from .forms import MarcaForm
	form = MarcaForm()
	lista = {}
	if request.method == "POST":
		if 'btnGrabar' in request.POST:	
			form = MarcaForm(request.POST)
			if form.is_valid():
				form.save()
		elif 'btnListar' in request.POST:
			lista = Marca.objects.all()
	
	contexto = {'lista':lista,'form': form}
	return render(request, 'marcaForm.html', contexto)	
	
	
def ajaxTestPlantilla(request):
	return render(request, 'ajaxTest.html', {})	
def ajaxTest(request):
	#from django.http import JsonResponse
	#return JsonResponse({'content': {'mensaje': 'Mensaje..'}})
	
	#from django.core import serializers
	#from django.http import JsonResponse	
	#lista = Marca.objects.all()
	#return JsonResponse(serializers.serialize('json', lista))
	lista = Marca.objects.all().values()
	return JsonResponse(list(lista), safe=False)
	

def registro(request):
	#from django.contrib.auth.models import User
	#from django.contrib.auth.hashers import make_password
	if request.method == "POST":
		nombre	= request.POST["txtNombre"]
		correo	= request.POST["txtCorreo"]
		clave	= request.POST["txtClave"]
		User.objects.create(username=nombre, email=correo, password=make_password(clave))
		
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	return render(request, 'registro.html', {})	
	
def marca(request):
	if not request.user.is_authenticated:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	mensaje = ""
	lista = {}
	item = {}
	# detecta si hay una solicitud
	if request.method == "POST":
		# captura los valores entregados por los usuarios
		id		= int("0" + request.POST["txtId"]) # convertir a int
		nombre	= request.POST["txtNombre"]
		activo	= request.POST.get("chkActivo") == "1" # False or True
		
		#detecta que boton presiono el usuarios
		if 'btnGrabar' in request.POST:			
			if id < 1: # un nuevo registro
				Marca.objects.create(nombre = nombre, activo = activo) #registra los datos
			else:
				item = Marca.objects.get(pk = id)
				item.nombre = nombre
				item.activo = activo
				item.save() #guarda los cambios
				item = {}
				
			mensaje = "Datos guardados"
		elif 'btnBuscar' in request.POST:
			try:
				item = Marca.objects.get(pk = id)
			except:			
				mensaje = "Registro no encontrado"
				item = {}
				
			
		elif 'btnListar' in request.POST:
			lista = Marca.objects.all()
			
		elif 'btnEliminar' in request.POST:
			item = Marca.objects.get(pk = id) #obtiene el registro según id
			
			if isinstance(item, Marca):
				item.delete()
				mensaje = "Registro eliminado"
				item = {}
	# context es la información que se envia a la plantilla para procesar
	contexto = {'mensaje': mensaje, 'lista':lista, 'item':item}
	
	return render(request, 'marca.html', contexto)