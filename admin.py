from django.contrib import admin
from dairyapp.models import Products,Services,categories
# Register your models here.

search_fields = ('prd name')
admin.site.register (Products)
admin.site.register (Services)
admin.site.register (categories)
# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'product', 'quantity']
