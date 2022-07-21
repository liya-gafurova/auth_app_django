from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

DATA = [
    {'name': "cat", 'color': "red"},
    {'name': "cat", 'color': "red"},
    {'name': "cat", 'color': "red"}
]

class TestDataSerializer(serializers.Serializer):
    name = CharField()
    color = CharField()

class TestView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = TestDataSerializer

    def get_object(self):
        return DATA[0]

    def get(self, request, *args, **kwargs):
        return super(TestView, self).get(request, *args, **kwargs)