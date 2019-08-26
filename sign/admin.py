from django.contrib import admin
from sign.models import warehouse
# Register your models here.

class warehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'member', 'dbl', 'status', 'create_time']
    search_fields = ['name'] # 搜索栏
admin.site.register(warehouse,warehouseAdmin)