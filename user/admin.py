from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MyNotification)
admin.site.register(UserAuth)
admin.site.register(MyPayroll)
admin.site.register(MyStudioSession)