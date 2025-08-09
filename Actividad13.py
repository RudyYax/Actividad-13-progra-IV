print("Actividad 13")
class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} paquetes - Zona: {self.zona}"

class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = {}

    def agregar_Repartidores(self):
        try:
            cantidad = int(input(("Ingrese la cantidad de repartidores que desea guardar")))
        except ValueError:
            print("Ingrese un numero entero")
            for i in range(cantidad):
                print(f"\n Ingrese los datos del repartidor {i + 1}:")
                while True:
                    nombre = input("Ingrese el Nombre del repartidor: ")
                    if nombre in self.repartidores:
                        print("Nombre repetido no puede repetirse")
                    else:
                        break
                    paquetes = int(input("Ingrese la cantidad de paquetes entregados"))
                    zona = input("Ingrese la zona donde repartio")
                    self.repartidores[nombre] = Repartidor(nombre, paquetes, zona)

    def quick_sort(self, resultado):
        if len(resultado) <= 1:
            return resultado

        pivote = resultado[0]
        menor = [x for x in resultado if x.paquetes < pivote.paquetes]
        iguales = [x for x in resultado if x.paquetes == pivote.paquetes]
        mayor = [x for x in resultado if x.paquetes > pivote.paquetes]

        return self.quick_sort(mayor) + iguales + self.quick_sort(menor)

    def Buscar_Repartidor(self, resultado):
        lista = list(self.repartidores.values())
        for i, repartidor in enumerate(lista):
            ordenada = self.







