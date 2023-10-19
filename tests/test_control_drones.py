# test_control_drones.py
import unittest
from control_drones import Dron

class TestControlDrones(unittest.TestCase):
    def test_programar_ruta(self):
        dron = Dron("DronA", "ModeloX1")
        origen = "FarmaciaA"
        destino = "PacienteX"
        ruta_programada = dron.programar_ruta(origen, destino)
        expected_result = "Ruta programada desde FarmaciaA hasta PacienteX para el dron DronA (ModeloX1)."
        self.assertEqual(ruta_programada, expected_result)

if __name__ == "__main__":
    unittest.main()
