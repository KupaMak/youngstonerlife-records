from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(UserAlbum)
admin.site.register(ManagerAuth)
admin.site.register(Studio)
admin.site.register(StudioSession)
admin.site.register(UserPayroll)
admin.site.register(ShowsTours)

