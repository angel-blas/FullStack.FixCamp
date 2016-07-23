from django.shortcuts import render, HttpResponse

from django.views.generic import View
# Create your views here.

class Sabado(View):
	def get(self,request):
		#return HttpResponse('Te saludo humano')
		return render(request,'hola.html')

class Otra(View):
	def get(self,request):
		return HttpResponse('Yo soy otra ruta')
