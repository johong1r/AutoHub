from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    FunctionChangePasswordSerializer,
    ProfileSerializer,
    SendMailSerializer,
    ResetPasswordConfirmSerializer,
    ResetPasswordRequestSerializer,
    ResetPasswordVerifySerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from accounts.models import PasswordResetCode
from django.contrib.auth import get_user_model
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


User = get_user_model()


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def reset_password_request(request):
    serializer = ResetPasswordRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = User.objects.get(email=serializer.validated_data['email'])
    reset_code = PasswordResetCode.create_code(user)

    print('RESET CODE:', reset_code.code)

    return Response({'detail': 'Reset code sent'}, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def reset_password_verify(request):
    serializer = ResetPasswordVerifySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = User.objects.get(email=serializer.validated_data['email'])
    code = serializer.validated_data['code']

    reset = PasswordResetCode.objects.filter(
        user=user,
        code=code,
        is_used=False
    ).first()

    if not reset or reset.is_expired():
        return Response(
            {'detail': 'Invalid or expired code'},
            status=400
        )
    
    return Response({'detail': 'Code is valide'}, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def reset_password_confirm(request):
    serializer = ResetPasswordConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = User.objects.get(email=serializer.validated_data['email'])
    code = serializer.validated_data['code']

    reset = PasswordResetCode.objects.filter(
        user=user,
        code=code,
        is_used=False
    ).first()

    if not reset or reset.is_expired():
        return Response(
            {'detail': 'Invalid or expired code'},
            status=400
        )
    
    user.set_password(serializer.validated_data['new_password'])
    user.save()

    reset.is_used = True
    reset.save()
    
    return Response({'detail': 'Password changed'}, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_email_send(request):
    serializer = SendMailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'Email sent successfully'}, status=200)


@api_view(['POST'])
def custom_login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data)


@api_view(['POST'])
def custom_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)   


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def custom_logout(request):
    Token.objects.filter(user=request.user.user).delete()
    return Response(status=204)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method =="GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    if request.method == ["PUT",'PATCH']:
        serializer = ProfileSerializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = FunctionChangePasswordSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=200)