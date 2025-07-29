from django.db import models

class Venta(models.Model):
    USUARIO_CHOICES = [('diego', 'Diego'), ('sahara', 'Sahara')]
    SABORES = [
        ('milo', 'Milo'),
        ('maracuya', 'Maracuyá'),
        ('limon', 'Limón'),
        ('mora', 'Mora'),
        ('lulo', 'Lulo'),
    ]

    usuario = models.CharField(max_length=10, choices=USUARIO_CHOICES)
    sabor = models.CharField(max_length=10, choices=SABORES)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def total_dinero(self):
        return self.cantidad * 7000
