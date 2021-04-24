from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer, PasswordSendSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .token import getToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AccountViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], permission_classes = [AllowAny])
    def login(self, request):
        log_serializer = LoginSerializer(data=request.data)
        if log_serializer.is_valid():
            user = get_user_model().objects.get(email=request.data['email'])
            data = {'ok': True, 'user': log_serializer.data, 'uid': user.uid, 'token': getToken( request.data, 'token')}
            return Response(data, status.HTTP_200_OK)
        data={'ok': False, 'msg': log_serializer.errors, }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], name='Change Password', permission_classes = [IsAuthenticated])
    def password_change(self, request, *args, **kwargs):
        serializer_class = PasswordChangeSerializer(data=request.data)
        if serializer_class.is_valid():
            if not self.request.user.check_password(serializer_class.data.get('old_password')):
                return Response({'old_password': 'Wrong Password'},status=status.HTTP_400_BAD_REQUEST)
            self.request.user.set_password(serializer_class.data.get('new_password'))
            self.request.user.save()
            
            return Response({'ok': True, 'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response({'ok': False, 'msg': 'An error has ocurred'}, status=status.HTTP_400_BAD_REQUEST)  
     
    @action(detail=False, methods=['post'], permission_classes = [AllowAny])
    def register(self, request):
        reg_serializer = UserSerializer(data=request.data)
        if reg_serializer.is_valid():
            user = reg_serializer.save()
            if user:
                data={'ok': True, 'msg': 'Sign Up completed'}
                return Response(data, status.HTTP_200_OK)
        data={'ok': False, 'msg': reg_serializer.errors, }    
        return Response(data, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], permission_classes = [AllowAny], name='Enviar email')
    def sendEmail(self, request):
        sendEmail_serializer = PasswordSendSerializer(data=request.data)
        if sendEmail_serializer.is_valid():
            try:
                user=get_user_model().objects.get(email=request.data['email'])
                if user:
                    data={'ok': True, 'msg': 'Email sent'}
                    return Response(data, status.HTTP_200_OK)
            except:
                data={'ok': False, 'msg': 'Email does not exist'}
                return Response(data, status.HTTP_400_BAD_REQUEST)
        data={'ok': False, 'msg': sendEmail_serializer.errors, }    
        return Response(data, status.HTTP_400_BAD_REQUEST) 
    
 
        

