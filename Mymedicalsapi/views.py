from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from.serializers import medicineSerializers
from Mymedicals.models import medicine
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from.serializers import medicineSerializers


# Create your views here.


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def simpleapi(request):
    return Response({'text': 'Hello world, This is your first api call'},status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)    


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def medicinedetails(request):
    details = medicine.objects.all()
    serializer = medicineSerializers(details,many=True)
    return Response(serializer.data,status=HTTP_200_OK)    


class CreateTodoAPIView(CreateAPIView):
    
    queryset = medicine.objects.all()
    serializer_class = medicineSerializers

class UpdateTodoAPIView(UpdateAPIView):
    
    queryset = medicine.objects.all()
    serializer_class = medicineSerializers

class DeleteTodoAPIView(DestroyAPIView):
    
    queryset = medicine.objects.all()
    serializer_class = medicineSerializers    