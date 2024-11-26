from django.contrib import admin
from .models import User,Items,Canteen,Order
# Register your models here.
admin.site.register(User)
admin.site.register(Items)
admin.site.register(Canteen)
admin.site.register(Order)
