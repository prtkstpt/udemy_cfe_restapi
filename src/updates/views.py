import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin

from .models import Update

def json_example_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)
        

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        
        return self.render_to_json_response(data)
    
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        
        json_data = obj.serialize()
        #json_data = serialize("json", [obj,], fields=('user', 'content'))
        
        return HttpResponse(json_data, content_type='application/json')    
    
    
class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        
        json_data = Update.objects.all().serialize()
        
        # json_data = serialize("json", qs, fields=('user', 'content'))
        return HttpResponse(json_data, content_type='application/json')    
    
    