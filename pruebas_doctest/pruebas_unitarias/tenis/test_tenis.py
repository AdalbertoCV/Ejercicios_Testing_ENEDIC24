# Pruebas
import unittest
from tenis import tenis

class TestTenis(unittest.TestCase):
    def setUp(self):
        self.t = tenis()
        self.jugador1 = "Viky"
        self.jugador2 = "Adal"

    def tearDown(self):
        pass

    def test_inicio_partido(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        resultado = self.t.score()
        self.assertEqual(resultado, "0-0")

    def test_jugador1_anota_primero(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "15-0")

    def test_jugador2_anota_primero(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "0-15")

    def test_ambos_anotan(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "15-15")

    def test_ultimo_punto_jugador1(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "40-30")

    def test_ultimo_punto_jugador2(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "30-40")

    def test_jugador_dos_gana(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Adal Win")

    def test_jugador_uno_ventaja(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Ventaja Viky")

    def test_jugador_dos_ventaja(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Ventaja Adal")

    def test_jugador_uno_gana(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador1)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Viky Win")

    def test_empate(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Empate momentaneo")

    def test_victoria_rapida_p1(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador1)
        self.t.points(self.jugador1)
        self.t.points(self.jugador1)
        self.t.points(self.jugador1)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Viky Win")

    def test_victoria_rapida_p2(self):
        self.t.iniciar(self.jugador1, self.jugador2)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        self.t.points(self.jugador2)
        resultado1 = self.t.score()
        self.assertEqual(resultado1, "Adal Win")
        

if __name__ == '__main__': #pragma no cover
    unittest.main()