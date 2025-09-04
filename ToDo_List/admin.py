from django.contrib import admin
from .models import Task 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'date_created', 'due_date')
    list_filter = ('status', 'due_date',)
    search_fields = ('title', 'description')
    ordering = ['date_created']

admin.site.register(Task, TaskAdmin)