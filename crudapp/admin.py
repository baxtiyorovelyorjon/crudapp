from django.contrib import admin
from .models import *
# Register your models here.
class UserAddModelAdmin(admin.ModelAdmin):
    list_display = ['name','user_name','email','images']
admin.site.register(UserAddModel,UserAddModelAdmin)










# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','age','phone','email']
#
# admin.site.register(UserModel,UserAdmin)
# admin.site.register(MusicModel)
# admin.site.register(AlbumModel)