from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        return Response({})
    
class StatusAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
    
class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    
    
class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    #lookup_field = 'id' 
    
class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    
    # def put(self, request, id, *args, **kwargs):
    #     return super().put(request, id, *args, **kwargs)
    
    
class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

