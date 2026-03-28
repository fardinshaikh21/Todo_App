from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "description", "priority", "created_at")
    list_filter = ("title","completed", "priority", "created_at")
    search_fields = ("title","completed", "created_at")

admin.site.register(Task,TaskAdmin)
admin.site.site_header = "Todo App Admin"
admin.site.site_title = "Todo App Admin Portal"
admin.site.index_title = "Welcome to the Todo App Admin Portal"
#admin.site.site_url = None
