# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_app.serializers import UserSerializer, GroupSerializer


def hello(request):
    return HttpResponse("Hello world ! 我是王尧")


def index(request):
    # return HttpResponse("Hello world ! home")
    return render(request, 'home.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StockInfoViewSet(viewsets.ModelViewSet)
    """
    API endpoint that allows groups to be viewed or edited.
    """
    stockinfoset =
    stockinfo =