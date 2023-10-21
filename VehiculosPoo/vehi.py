class Vehiculo:

    def __init__(self,marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def verVehiculo(self):
        print(f" Marca: {self.marca} \n Modelo: {self.modelo} \n Color: {self.color}")

Vehiculo1 = Vehiculo("Toyota", 2023, "Gris plata")
Vehiculo2 = Vehiculo("kawaszaki", 2026, "rosa petalo")

if __name__ == '__main__':
    print(Vehiculo1.marca)


Vehiculo1.marca = "Mercedez"

Vehiculo2.verVehiculo()
Vehiculo1.verVehiculo()
