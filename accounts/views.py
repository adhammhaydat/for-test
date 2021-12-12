from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework.views import APIView
import jwt
from django.conf import settings

from django.http import HttpResponsePermanentRedirect,Http404
import os


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


# class RegisterView(generics.GenericAPIView):

#     serializer_class = RegisterSerializer


#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         user = User.objects.get(email=user_data['email'])


#         return Response(user_data, status=status.HTTP_201_CREATED)



from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)



class RegisterView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



