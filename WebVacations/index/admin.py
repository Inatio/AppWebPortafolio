from django.contrib import admin


from index.models_new_3 import (Departamento, Reserva, Cargo, Contacto, 
                            Comuna, Tour, TipoTour, Pago)


# Register your models here.
admin.site.register(Departamento)
admin.site.register(Reserva)
admin.site.register(Cargo)
admin.site.register(Contacto)
admin.site.register(Comuna)
admin.site.register(Tour)
admin.site.register(TipoTour)
admin.site.register(Pago)

