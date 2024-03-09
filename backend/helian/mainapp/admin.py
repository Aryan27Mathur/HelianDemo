from django.contrib import admin
from .models import User, Company, ETF, DumbUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    userdisplay = ('name', 'email')

admin.site.register(User, UserAdmin)
admin.site.register(Company)
admin.site.register(ETF)
admin.site.register(DumbUser)