# control_drones.py

class Dron:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

    def programar_ruta(self, origen, destino):
        ruta = f"Ruta programada desde {origen} hasta {destino} para el dron {self.nombre} ({self.modelo})."
        return ruta

if __name__ == "__main__":
    dron1 = Dron("DronA", "ModeloX1")
    origen = "FarmaciaA"
    destino = "PacienteX"
    ruta_programada = dron1.programar_ruta(origen, destino)
    print(ruta_programada)
