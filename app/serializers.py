from app.models import Todo
from rest_framework import serializers


 # Validators 
def start_with_r(value):
    if value[0]!= 'R':
        raise serializers.ValidationError('value must be start R') 

class TodoSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200 , validators=[start_with_r])
    status=serializers.CharField(max_length=200)    
    
    
    
    def create(self , validated_data):
        return Todo.objects.create(**validated_data) 
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.status = validated_data.get('status' , instance.status )
        
        instance.save()
        return instance 
    
    # Field Level Validation
    
    def validate_status(self, value):
        if value != 'DONE' and value != 'PENDING' and  value != 'TRASH' and value != 'DOING':  
            raise serializers.ValidationError('Status is not correct')
        return value
    
    # Object Level Validation
    
    def validate(self, data):
        nm=data.get('name')
        stat=data.get('status')
        
        if not nm[0].isupper():
            raise serializers.ValidationError('First letter of name must be capital ..')
        
        if not stat.upper():
            raise serializers.ValidationError('status must be in capital case ...!!')
        
        return data
    
    

    
        