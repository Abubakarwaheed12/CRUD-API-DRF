from django.contrib import admin
from app.models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=['id' , 'name' , 'status' , 'updated_at' , 'created_at']