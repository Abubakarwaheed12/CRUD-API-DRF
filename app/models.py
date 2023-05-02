from django.db import models

# Create your models here.
class BaseModel(models.Model):
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        
class Todo(BaseModel):
    class status_choices(models.TextChoices):
     # Actual value ↓      # ↓ Displayed on Django Admin  
        PENDING = 'PENDING', 'PENDING'
        DOING = 'DOING', 'DOING'
        DONE = 'DONE', 'DONE'
        TRASH = 'TRASH', 'TRASH'
        
    
    name=models.CharField(max_length=200)
    status=models.CharField(choices=status_choices.choices , max_length=200)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='My Todo'