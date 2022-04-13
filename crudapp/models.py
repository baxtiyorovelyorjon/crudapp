from django.db import models

# Create your models here.

class UserAddModel(models.Model):
    name = models.CharField(max_length=50,verbose_name="Ism")
    user_name = models.CharField(max_length=50,verbose_name="Foydalanuvchi_nomi")
    email = models.EmailField()
    images = models.ImageField(upload_to='static/img')
    def __str__(self):
        return self.name
















# class UserModel(models.Model):
#     first_name = models.CharField(max_length=50,verbose_name="Ism:")
#     last_name = models.CharField(max_length=50,verbose_name="Familiya:")
#     phone = models.IntegerField(verbose_name='Tel:')
#     email = models.EmailField(verbose_name="Email:")
#     age = models.IntegerField(verbose_name="yoshi:")
#
#     def __str__(self):
#         return self.last_name
#
# class MusicModel(models.Model):
#     name = models.CharField(max_length=50,verbose_name='Ism',null=True,blank=True)
#     def __str__(self):
#         return self.name
#
#
# class AlbumModel(models.Model):
#     name = models.ForeignKey(MusicModel,on_delete=models.CASCADE,verbose_name="guruh_nomi",null=True,blank=True)
#
#
#     def __str__(self):
#         return self.name