from django.db import models
from django.db.models import F, Sum, FloatField
from django.contrib.auth import get_user_model
from tienda.models import Producto

# Create your models here.

User = get_user_model()

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)  # type: ignore

    @property
    def total(self):
        return self.lineapedido_set.aggregate( # type: ignore
            total = Sum(F('precio') * F('cantidad'),
                        output_field=FloatField()
                    )
        )['total']

class ItemPedido(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.cantidad} unidades de {self.producto_id.nombre}"

    class Meta:
        verbose_name = 'ItemPedido'
        verbose_name_plural = 'ItemsPedido'
        ordering=['id']

