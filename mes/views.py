from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import PROJECT

class index(View):
	model = PROJECT
	template_name = 'MES_INDEX.html'
	def get(self,request):
		return render(request,self.template_name)
