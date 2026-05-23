from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import authenticate, get_user_model
from .serializer import RegisterSerializer, UserSerializer

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def extract_token_from_header(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return None
    return auth_header.split(' ')[1]


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "detail": "Muvaffaqiyatli ro'yxatdan o'tdingiz. Kirish uchun login qiling."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({
                "detail": "Username va password majburiy!"
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:                                        # ← o'zgartirildi
            return Response({
                "detail": "Username yoki parol xato!"
            }, status=status.HTTP_401_UNAUTHORIZED)

        tokens = get_tokens_for_user(user)
        return Response({
            "user": UserSerializer(user).data,
            "tokens": tokens,
            "detail": "Tizimga muvaffaqiyatli kirildi."
        }, status=status.HTTP_200_OK)


class RefreshTokenAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = extract_token_from_header(request)
        if not refresh_token:
            return Response({
                "detail": "Refresh token Authorization Headers ichida Bearer bo'lib kelishi shart!"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            return Response({
                "access": str(token.access_token),
                "refresh": str(token)
            }, status=status.HTTP_200_OK)
        except TokenError:
            return Response({
                "detail": "Token yaroqsiz yoki muddati o'tgan!"
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({
                "detail": "Refresh token Authorization Headers ichida Bearer bo'lib kelishi shart!"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                "detail": "Tizimdan muvaffaqiyatli chiqildi."
            }, status=status.HTTP_200_OK)
        except TokenError:
            return Response({
                "detail": "Token xato yoki allaqachon o'chirilgan!"
            }, status=status.HTTP_400_BAD_REQUEST)