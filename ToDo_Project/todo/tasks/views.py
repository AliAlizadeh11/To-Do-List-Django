import django_filters
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Task
from .serializer import TodoSerializer

class TodoView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def update(self, request, *args, **kwargs):
        details = Task.objects.get(id=kwargs['pk'])
        serializer_data = TodoSerializer(
            details, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.updated_at = timezone.now()
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})


