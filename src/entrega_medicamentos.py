# entrega_medicamentos.py
class EntregaMedicamentos:
    def __init__(self):
        self.drones = []  # Lista de drones disponibles
    def agregar_dron(self, dron):
        self.drones.append(dron)
    def entregar_medicamento(self, paciente, medicamento):
        # Lógica para seleccionar un dron y programar la entrega al paciente.
        pass
if __name__ == "__main__":
    entrega = EntregaMedicamentos()
    dron1 = Dron("DronNumero1", "ModeloX1")
    entrega.agregar_dron(dron1)
    
