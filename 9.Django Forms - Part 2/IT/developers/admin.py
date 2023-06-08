'''

    Added admin panel to check the model objects

'''


from django.contrib import admin

from IT.developers.models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass
