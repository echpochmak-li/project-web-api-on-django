from django.shortcuts import render
from .models import*
from django.views.generic import ListView
from rest_framework import viewsets
from .serializers import*
# Create your views here.

class Index_views(ListView):
    template_name = 'index.html'
    model = Serials
    ordering = ('-id')
    
class SerialsApi(viewsets.ModelViewSet):
    queryset = Serials.objects.all()
    serializer_class = SerialsSerializer
