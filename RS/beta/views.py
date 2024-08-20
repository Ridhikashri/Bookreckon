from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class betacls(APIView):
    def post(self,request):
        value=request.data.get('value')
        
        return Response("Hello Buddy")


# Create your views here.
