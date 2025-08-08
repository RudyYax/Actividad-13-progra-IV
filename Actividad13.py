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
        self.repartidores = []

    def agregar_repartidor(self, repartidor):
        if any(r.nombre.lower() == repartidor.nombre.lower() for r in self.repartidores):
            print(f"Error: Ya existe un repartidor con el nombre '{repartidor.nombre}'. No se agrega.")
            return False
        if not repartidor.nombre.strip():
            print("Error: El nombre no puede estar vacío.")
            return False
        if not isinstance(repartidor.paquetes, int) or repartidor.paquetes < 0:
            print("Error: La cantidad de paquetes debe ser un entero positivo.")
            return False
        if not repartidor.zona.strip():
            print("Error: La zona no puede estar vacía.")
            return False
        self.repartidores.append(repartidor)
        return True

    def ordenar_por_paquetes(self):
        self._quick_sort(0, len(self.repartidores) - 1)