import json
from django.views.generic import View
from django.http import HttpResponse 
from django.shortcuts import render

from cfeapi.mixins import HttpResponseMixin

from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel

from .utils import is_json
from .mixins import CSRFExemptMixin

class UpdateModelDetailApiView(HttpResponseMixin, CSRFExemptMixin, View):
    
    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    
    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        if obj is None:
            error_data = json.dumps({'message': 'Update not found'})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)
    
    
    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': 'Invalid data sent, please send using JSON.'})
            return self.render_to_response(error_data, status=400)
            
        # new_data = json.loads(request.body)
        data = json.dumps({'message': 'Not Allowed, please use the api/updates/ ENDPOINT'})
        return self.render_to_response(data)
    
    
    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': 'Invalid data sent, please send using JSON.'})
            return self.render_to_response(error_data, status=400)
        
        
        obj = self.get_object(id)
        if obj is None:
            error_data = json.dumps({'message': 'Update not found'})
            return self.render_to_response(error_data, status=404)
        
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
    
        for key, value in passed_data.items():
            data[key] = value    
    
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
            
        new_data = json.loads(request.body)
        json_data = json.dumps({'message': 'something'})
        return self.render_to_response(json_data)
    
    
    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        if obj is None:
            error_data = json.dumps({'message': 'Update not found'})
            return self.render_to_response(error_data, status=404)
        
        deleted_, item_deleted = obj.delete()
        print(deleted_) 
        if deleted_ == 1:
            json_data = json.dumps({'message': 'Successfully deleted.'})
            return self.render_to_response(json_data, status=200)
        
        error_data = json.dumps({'message': 'Could not delete item.'})
        return self.render_to_response(error_data, status=400)
        
    
class UpdateModelListApiView(HttpResponseMixin, CSRFExemptMixin, View):
    
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.filter(id__gte=2)
        json_data = qs.serialize()  
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': 'Invalid data sent, please send using JSON.'})
            return self.render_to_response(error_data, status=400)
            
        data = json.loads(request.body)
        
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        
        data = json.dumps({'message': 'Not Allowed'})
        return self.render_to_response(data, status=400)
    
    def delete(self, request, *args, **kwargs):
        data = json.dumps({'message': 'You can not delete an entire list'})
        return self.render_to_response(data, status=403)