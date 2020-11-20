from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from charts.serializers import ExampleModelSerializer


class ExampleModelView(ListCreateAPIView):
    serializer_class = ExampleModelSerializer

    def get(self, request, *args, **kwargs):
        return Response({'data': {'first_name': 'Klaus', 'last_name': 'Caka'}}, status=status.HTTP_200_OK)
