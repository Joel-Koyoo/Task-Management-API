from .serializers import TodoSerializer
from django.http import HttpResponse
from .models import Todo
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
