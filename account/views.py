from django.shortcuts import render
from rest_framework import viewsets

from account.serializers import UserSerializer
from account.models import User

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(id=self.request.user.id)
