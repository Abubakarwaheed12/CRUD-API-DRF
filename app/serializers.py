from app.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    status=serializers.CharField(max_length=200)    
    
    
    
    def create(self , validated_data):
        return Todo.objects.create(**validated_data) 
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.status = validated_data.get('status' , instance.status )
        
        instance.save()
        
        return instance 