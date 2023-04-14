from django.contrib import admin
from mysite.tasks.models import Task, Diet


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    pass
