from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import update_last_login

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    id = request.data.get('id')
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    generation = request.data.get('generation')
    gender = request.data.get('gender')
    
    serializer = UserSerializer(data=request.data)
    serializer.id = id
    serializer.email = email
    serializer.name = name
    serializer.generation = generation
    serializer.gender = gender

    if serializer.is_valid(raise_exception=True):
        # raise_exception=True는 is_valid 체크에서 에러가 날때 ValidationError를 일으킴
        user = serializer.save()
        user.set_password(password)
        user.save()

        user = authenticate(request, id=id, password=password)
        if user is not None:
            django_login(request, user)
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)
            return Response({'refresh_token': str(refresh), 
            'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    id = request.data.get('id')
    password = request.data.get('password')

    user = authenticate(id=id, password=password)
    if user is None:
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny]) 
def refresh(request):
    refresh = request.data.get("refresh")

    if refresh is None:
        return Response({"message":"Refresh token을 입력하세요."})

    refresh_token = RefreshToken(refresh)
    access_token = str(refresh_token.access_token)
    return Response({"access token":access_token}, status=status.HTTP_200_OK)

