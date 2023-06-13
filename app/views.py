from django.shortcuts import render
from app.models import Todo
from app.serializers import TodoSerializer
import io 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import  JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from django.views import  View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

# Api class view 
class TodoAPI(APIView):
    def get(self ,request , pk = None , format=None):
        id = pk
        print(id)
        if id is not None:
            todo=Todo.objects.get(id=id) if  Todo.objects.filter(id=id).exists() else None

            print( 'rodo obj' ,  todo)
            if todo != None:
                serializer=TodoSerializer(todo)
                return Response({'msg':'This is Get Request','todo':serializer.data } , status=status.HTTP_200_OK) 
            return Response({'msg':'User not found' } , status=status.HTTP_204_NO_CONTENT)

        todo=Todo.objects.all()
        serializer=TodoSerializer(todo , many=True)
        return Response({'msg':'This is Get Request','todo':serializer.data} , status=status.HTTP_200_OK) 
    
    
    def post(self,request):
        serializer=TodoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'msg':'data saved '} , status=status.HTTP_201_CREATED)
        
        return Response({'error':serializer.errors} ) 
        
        
    def put(self ,request , pk=None , format = None):
        id=pk
        print(id)
        todo = Todo.objects.get(id=id)
        
        serializer=TodoSerializer(todo , data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'msg':'data Put '})
        
        return Response({'error':serializer.errors}) 
    
    def patch(self ,request , pk=None , format = None):
        id=pk
        todo = Todo.objects.get(id=id)
        
        serializer=TodoSerializer(todo , data=request.data , partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({'msg':'data Patch'})
        
        return Response({'error':serializer.errors}) 
    
    
    def delete(self , request , pk =None , format=None):
        
        id = Todo.objects.get(id=pk).delete()       
        
        return Response({'msg':'deleted successfully .... !!!'})






# Crud with apiview
# @api_view(['POST','GET','PUT','PATCH','DELETE'])
# def TodoAPI(request , pk = None):
#     if request.method == 'GET':
#         id = pk
#         print(id)
#         if id is not None:
#             todo=Todo.objects.get(id=id)
#             serializer=TodoSerializer(todo)
#             return Response({'msg':'This is Get Request','todo':serializer.data } , status=status.HTTP_200_OK) 
        
#         todo=Todo.objects.all()
#         serializer=TodoSerializer(todo , many=True)
#         return Response({'msg':'This is Get Request','todo':serializer.data} , status=status.HTTP_200_OK) 
    
    
    
#     if request.method=='POST':
    
#         serializer=TodoSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response({'msg':'data saved '} , status=status.HTTP_201_CREATED)
        
#         return Response({'error':serializer.errors} ) 
    
    
    
    
#     if request.method=='PUT':
        
#         id=pk
#         print(id)
#         todo = Todo.objects.get(id=id)
        
#         serializer=TodoSerializer(todo , data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response({'msg':'data Put '})
        
#         return Response({'error':serializer.errors}) 
    
#     if request.method=='PATCH':
#         
#         id=pk
#         todo = Todo.objects.get(id=id)
        
#         serializer=TodoSerializer(todo , data=request.data , partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response({'msg':'data Patch'})
        
#         return Response({'error':serializer.errors}) 
    
    
#     if request.method=='DELETE':
        
#         id=pk
#         todo = Todo.objects.get(id=id).delete()
        
#         return Response({'msg':'Delete Successfully'}) 





# @csrf_exempt
# def todoAPI(request):
    
    
#     # GET
#     if request.method=='GET':
#         data=request.body
#         stream=io.BytesIO(data)
#         python_data=JSONParser().parse(stream)
        
#         id =python_data.get('id', None)
        
#         if id is not None:
#             todo=Todo.objects.get(pk=id)
#             serializer=TodoSerializer(todo)
#             return JsonResponse(serializer.data) 
        
#         all_data=Todo.objects.all()
#         serializer=TodoSerializer(all_data , many = True )        
#         return JsonResponse(serializer.data , safe = False )
    
    
    
    
#     # INSERT
#     if request.method == 'POST':
#         data=request.body
#         stream=io.BytesIO(data)
#         python_data = JSONParser().parse(stream)
        
#         serializer = TodoSerializer(data = python_data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             res = {'msg' : 'your data saved successfully ....!!!!' }
            
#             return JsonResponse(res)
        
#         return JsonResponse(serializer.errors)
    
    
    
    
#     # EDIT
#     if request.method == 'PUT':
#         data = request.body
#         stream = io.BytesIO(data)
#         python_data = JSONParser().parse(stream)
        
#         id = python_data.get('id')
        
#         todo_d = Todo.objects.get(id = id)
        
#         serializer = TodoSerializer( todo_d , data = python_data , partial = True )  
        
#         if serializer.is_valid():
#             serializer.save()
            
#             res = {'msg' : 'updated successfully'}
            
#             json_response = json.dumps(res)
            
#             return JsonResponse(json_response , safe=False)
        
#         return JsonResponse(serializer.errors , safe=False)
    
    
    
#     # DELETE
#     if request.method == 'DELETE':
#         data = request.body
#         stream = io.BytesIO(data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         todo_d = Todo.objects.get(id = id).delete()
#         res = {'msg' : 'deleted successfully'}
#         json_response = json.dumps(res)
        
#         return JsonResponse(json_response , safe=False)
        
   
        
# Class 
# @method_decorator(csrf_exempt , name = 'dispatch')
# class TodoAPI(View):
    # get  
    # def get(self, request , *args , **kwargs): 
    #     data=request.body
    #     stream=io.BytesIO(data)
    #     python_data=JSONParser().parse(stream)
        
    #     id =python_data.get('id', None)
        
    #     if id is not None:
    #         todo=Todo.objects.get(pk=id)
    #         serializer=TodoSerializer(todo)
            
    #         return JsonResponse(serializer.data) 
        
    #     all_data=Todo.objects.all()
    #     serializer=TodoSerializer(all_data , many = True ) 
               
    #     return JsonResponse(serializer.data , safe = False )
        
        
    # # post
    # def post(self, request , *args , **kwargs):
    #     data=request.body
    #     stream=io.BytesIO(data)
    #     python_data = JSONParser().parse(stream)
    #     serializer = TodoSerializer(data = python_data )
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg' : 'your data saved successfully ....!!!!' }
    #         return JsonResponse(res)
    #     return JsonResponse(serializer.errors)      
        
        
        
    # edit
    # def put(self, request , *args , **kwargs):
    #     data = request.body
    #     stream = io.BytesIO(data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id')
    #     todo_d = Todo.objects.get(id = id)
    #     serializer = TodoSerializer( todo_d , data = python_data , partial = True )  
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg' : 'updated successfully'}
    #         json_response = json.dumps(res)
    #         return JsonResponse(json_response , safe=False)
    #     return JsonResponse(serializer.errors , safe=False)
        
        
    # delete
    # def delete(self, request , *args , **kwargs):
    #     data = request.body
    #     stream = io.BytesIO(data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id')
    #     todo_d = Todo.objects.get(id = id).delete()
    #     res = {'msg' : 'deleted successfully'}
    #     json_response = json.dumps(res)
    #     return JsonResponse(json_response , safe=False)