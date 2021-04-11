from django.contrib import admin
from crm.models import UserInfo
# Register your models here.


@admin.register(UserInfo)
class CrmAdmin(admin.ModelAdmin):
    list_display = [x for x in list(UserInfo._meta._forward_fields_map.keys())]
    list_per_page = 10
    search_fields = ['username', 'phone']
    actions_on_top = False
    actions_on_bottom = True