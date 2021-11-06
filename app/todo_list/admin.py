from django.contrib import admin

#Models 
from todo_list.models import Task

@admin.register(Task)
class TaskAdminModel(admin.ModelAdmin):
    """Admin model for task """
    list_display = ('name','planned','user','completed',)
    list_filter = ('planned','completed',)
    prepopulated_fields ={'slug':('name',)}