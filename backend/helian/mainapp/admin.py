from django.contrib import admin
from .models import User, Company, ETF, DumbUser
# Register your models here.


admin.site.register(User)
admin.site.register(Company)
admin.site.register(ETF)
admin.site.register(DumbUser)