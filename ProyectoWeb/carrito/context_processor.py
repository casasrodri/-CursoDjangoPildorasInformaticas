def importe_total_carrito(request):

    carrito = request.session.get("carrito")
    if not carrito:
        request.session["carrito"] = {}




    total = 0

    if True or request.user.is_authenticated:
        for value in request.session["carrito"].values():
            total += value["precio"]

    return {"importe_total_carrito": total}
