from django.contrib import admin

# Register your models here.

from .models import Action


class ActionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Action, ActionAdmin)
