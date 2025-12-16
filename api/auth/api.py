from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer


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