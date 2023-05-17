from django.contrib import admin

from DevsInfo.Developers.models import Developer


@admin.register(Developer)
class AdminDeveloper(admin.ModelAdmin):
    pass
