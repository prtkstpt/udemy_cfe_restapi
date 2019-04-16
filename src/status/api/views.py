import json
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404
from status.models import Status
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        valid_json = json.loads(json_data)
        is_valid = True
    except:
        is_valid = False
    return is_valid
    
    
class StatusAPIDetailView(
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            generics.RetrieveAPIView):
    permission_classes      = []
    authentication_classes  = []
    queryset                = Status.objects.all()
    serializer_class        = StatusSerializer
    lookup_field            = 'id' 
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class StatusAPIView(    
        mixins.CreateModelMixin,        
        generics.ListAPIView):
    
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer
    passed_id = None
    
    
    def get_queryset(self):
        request = self.request
        print('userrrrrr', request.user)
        qs = Status.objects.all()
        query = request.GET.get('q')
        
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
    # def get(self, request, *args, **kwargs):
    #     url_passed_id   = request.GET.get('id', None)
    #     json_data       = {}
    #     body_           = request.body
        
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
            
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)

    
    


    # def put(self, request, *args, **kwargs):
    #     url_passed_id   = request.GET.get('id', None)
    #     json_data       = {}
    #     body_           = request.body
        
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
            
    #     requested_id = request.data.get('id', None)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or requested_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    
    
    # def patch(self, request, *args, **kwargs):
    #     url_passed_id   = request.GET.get('id', None)
    #     json_data       = {}
    #     body_           = request.body
        
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
            
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     url_passed_id   = request.GET.get('id', None)
    #     json_data       = {}
    #     body_           = request.body
        
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
            
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.destroy(request, *args, **kwargs)
    
    
    
# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
    
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         return Response({})
    
    
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

