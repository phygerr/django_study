# Register your models here.
from django.contrib import admin
from django import forms
from models import Person,Account
#configuration display
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age']
    #add search function in admin
    search_fields = ['name','age']
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','password','email','phone']
# register
admin.site.register(Person,PersonAdmin)
admin.site.register(Account,AccountAdmin)