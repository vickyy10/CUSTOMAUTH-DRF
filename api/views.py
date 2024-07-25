from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializer import PersonSerializer
from rest_framework.permissions import IsAuthenticated
from .CustomAuth import CustomAuthentication
# Create your views here.


class PersonModelViewset(viewsets.ModelViewSet):

    queryset=Person.objects.all()
    serializer_class=PersonSerializer

    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]
