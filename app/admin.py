from django.contrib import admin

# Register your models here.
from app.models import Styles, Requisition
admin.site.register(Styles)
admin.site.register(Requisition)