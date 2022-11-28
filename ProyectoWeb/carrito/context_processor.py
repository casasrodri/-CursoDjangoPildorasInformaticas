def importe_total_carrito(request):

    total = 0

    if request.user.is_authenticated:
        for value in request.session["carrito"].values():
            total += value["precio"]
    else:
        total = "Debes iniciar sesión."

    return {"importe_total_carrito": total}
