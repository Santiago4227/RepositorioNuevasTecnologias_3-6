from vehi import Vehiculo

class Moto(Vehiculo):

    freno = "abs"

    def __init__(self,marca,modelo,color,categoria):
        super().__init__(marca,modelo,color)
        self.categoria = categoria
        
    def verVehiculo(self):
        super(Moto, self).verVehiculo()
        print(f"Categoria {self.categoria}\n Tipo freno: {self.freno}")

mt09 = Moto("Yamaha",2023,"gris raton","scooter")

mt09.verVehiculo()