from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_venta=models.PositiveIntegerField(primary_key=True)
    id_cliente=models.PositiveIntegerField()
    id_calzado=models.PositiveIntegerField()
    fecha_venta=models.DateField(null=False,blank=False)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    id_empleado=models.PositiveIntegerField()

    def __str__(self):
        return self.id_venta