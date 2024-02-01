from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todo.models import Todo
from todo.serializers import TodoModelSerializer

class Todoviewset(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

# Create your views here.
