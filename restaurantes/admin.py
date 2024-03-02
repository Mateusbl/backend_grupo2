from django.contrib import admin
from restaurantes.models import Restaurantes
from restaurantes.models import cuisine

# Register your models here.
class RestaurantesAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'telephone', 'cuisine', 'working_hours')
    search_fields = ('name', 'cuisine')
    list_filter = ('cuisine', 'working_hours')
admin.site.register(Restaurantes, RestaurantesAdmin)
admin.site.register(cuisine, admin.ModelAdmin)

    
