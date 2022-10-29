from rest_framework import viewsets
from .models import Response
from .serializer import ResponseSerializer

class ResponseViewset(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    http_method_names = ['get']