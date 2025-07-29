from django.shortcuts import render
from .models import Venta
from collections import Counter

# Inventario por usuario
INVENTARIO = {
    "diego": {
        "milo": 10,
        "maracuya": 10,
        "limon": 7,
        "mora": 5,
        "lulo": 5,
    },
    "sahara": {
        "milo": 11,
        "maracuya": 10,
        "limon": 7,
        "mora": 5,
        "lulo": 5,
    }
}

def registrar_venta(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        sabor = request.POST["sabor"]
        cantidad = int(request.POST["cantidad"])

        Venta.objects.create(usuario=usuario, sabor=sabor, cantidad=cantidad)

        # Obtener todas las ventas de ese usuario desde la base de datos real
        ventas_usuario = Venta.objects.filter(usuario=usuario)

        # Contar postres vendidos por sabor
        vendidos = Counter()
        for venta in ventas_usuario:
            vendidos[venta.sabor] += venta.cantidad

        inventario_usuario = INVENTARIO.get(usuario, {})
        faltan = {
            sabor: inventario_usuario.get(sabor, 0) - vendidos.get(sabor, 0)
            for sabor in inventario_usuario
        }

        dinero = sum(vendidos[s] * 7000 for s in inventario_usuario)

        return render(request, "ventas/gracias.html", {
            "usuario": usuario,
            "vendidos": vendidos,
            "faltan": faltan,
            "dinero": dinero
        })

    return render(request, "ventas/registro.html")
