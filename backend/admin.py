from django.contrib import admin
from backend.models import *

# Register your models here.


class GenericModelAdmin(admin.ModelAdmin):

    list_display = ('nombre',)
    search_fields = ['nombre']


admin.site.register(Usuario, GenericModelAdmin)
admin.site.register(Marca, GenericModelAdmin)
admin.site.register(Estilo, GenericModelAdmin)
admin.site.register(Color, GenericModelAdmin)
admin.site.register(Region, GenericModelAdmin)
admin.site.register(Aro, GenericModelAdmin)
admin.site.register(Bicicleta)
admin.site.register(Transferencia)