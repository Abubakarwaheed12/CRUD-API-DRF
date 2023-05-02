from django.shortcuts import render
from app.models import Todo
from app.serializers import TodoSerializer
import io 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import  JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def todoAPI(request):
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
    
    
    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(stream)
        python_data = JSONParser().parse(stream)
        
        serializer = TodoSerializer(data = python_data , partial = True )  
         
        