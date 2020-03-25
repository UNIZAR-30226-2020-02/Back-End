from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse

from .serializer import *
from .models import *

# Create your views here.

@api_view(['POST'])
def CrearCarpeta(request):

    if request.method == "POST":
        serializer = CarpetaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            Response(serializer.data)

        else:

            Response(status=status.HTTP_400_BAD_REQUEST)

