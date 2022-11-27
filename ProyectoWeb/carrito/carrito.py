class Carrito:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session

        carrito = self.session.get("carrito")

        if not carrito:
            carrito = self.session["carrito"] = {}
        #else:

        self.carrito = carrito


    def agregar(self, producto):
        print(self.carrito)
        if str(producto.id) not in self.carrito.keys():
            self.carrito[str(producto.id)] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "imagen": producto.imagen.url,
                "cantidad": 1,
            }
        else:
            carrito = self.carrito[str(producto.id)]
            carrito["cantidad"] += 1
            carrito["precio"] += producto.precio

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        if str(producto.id) in self.carrito.keys():
            del self.carrito[str(producto.id)]
            self.guardar_carrito()

    def restar_producto(self, producto):
        if self.carrito[str(producto.id)]["cantidad"] == 1:
            self.eliminar(producto)
        else:
            carrito = self.carrito[str(producto.id)]
            carrito["cantidad"] -= 1
            carrito["precio"] -= producto.precio

        self.guardar_carrito()

    def vaciar(self):
        self.session["carrito"] = {}
        self.session.modified = True
