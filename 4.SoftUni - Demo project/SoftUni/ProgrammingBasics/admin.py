from django.contrib import admin
from SoftUni.ProgrammingBasics.models import Lecture


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    pass
