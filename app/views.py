from django.shortcuts import render
from app.models import Todo
from app.serializers import TodoSerializer
import io 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import  JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def todoAPI(request):
    
    
    # GET
    if request.method=='GET':
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        
        id =python_data.get('id', None)
        
        if id is not None:
            todo=Todo.objects.get(pk=id)
            serializer=TodoSerializer(todo)
            return JsonResponse(serializer.data) 
        
        all_data=Todo.objects.all()
        serializer=TodoSerializer(all_data , many = True )        
        return JsonResponse(serializer.data , safe = False )
    
    
    
    
    # INSERT
    if request.method == 'POST':
        data=request.body
        stream=io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        
        serializer = TodoSerializer(data = python_data)
        
        if serializer.is_valid():
            serializer.save()
            
            res = {'msg' : 'your data saved successfully ....!!!!' }
            
            return JsonResponse(res)
        
        return JsonResponse(serializer.errors)
    
    
    
    
    # EDIT
    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        
        todo_d = Todo.objects.get(id = id)
        
        serializer = TodoSerializer( todo_d , data = python_data , partial = True )  
        
        if serializer.is_valid():
            serializer.save()
            
            res = {'msg' : 'updated successfully'}
            
            json_response = json.dumps(res)
            
            return JsonResponse(json_response , safe=False)
        
        return JsonResponse(serializer.errors , safe=False)
    
    
    
    # DELETE
    if request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        todo_d = Todo.objects.get(id = id).delete()
        res = {'msg' : 'deleted successfully'}
        json_response = json.dumps(res)
        
        return JsonResponse(json_response , safe=False)
        