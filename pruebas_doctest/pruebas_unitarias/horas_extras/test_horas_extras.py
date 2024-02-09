import unittest
from horas_extras import horas_extra

class Test_horas_extras(unittest.TestCase):
    def setUp(self):
        self.h = horas_extra()

    def tearDown(self):
        pass

    def test_horas_normales(self):
        resultado = self.h.calcular(30, 100)
        self.assertEqual(3000, resultado)

    def test_horas_normales_limite(self):
        resultado = self.h.calcular(40, 50)
        self.assertEqual(2000, resultado)

    def test_horas_extra_dobles(self):
        resultado = self.h.calcular(45, 80)
        self.assertEqual(4000, resultado)

    def test_horas_extra_dobles_limite(self):
        resultado = self.h.calcular(48,100)
        self.assertEqual(5600, resultado)

    def test_horas_extra_triples(self):
        resultado = self.h.calcular(50,100)
        self.assertEqual(6200, resultado)

    def test_horas_extra_triples_2(self):
        resultado = self.h.calcular(100,60)
        self.assertEqual(12720, resultado)

    def test_horas_cadena(self):
        resultado = self.h.calcular('x',60)
        self.assertEqual('No se aceptan cadenas', resultado)

    def test_total_cadena(self):
        resultado = self.h.calcular(10,'60a')
        self.assertEqual('No se aceptan cadenas', resultado)

    def test_horas_decimal(self):
        resultado  = self.h.calcular(9.5,100)
        self.assertEqual('No se aceptan decimales', resultado)

    def test_total_decimal(self):
        resultado  = self.h.calcular(9,100.5)
        self.assertEqual(904.5, resultado)

    def test_horas_boolean(self):
        resultado  = self.h.calcular(True,100)
        self.assertEqual('No se aceptan booleanos', resultado)

    def test_total_boolean(self):
        resultado  = self.h.calcular(10,True)
        self.assertEqual('No se aceptan booleanos', resultado)

    def test_horas_nonumerico(self):
        resultado  = self.h.calcular([],100)
        self.assertEqual('Formato no válido', resultado)

    def test_total_nonumerico(self):
        resultado  = self.h.calcular(10,{})
        self.assertEqual('Formato no válido', resultado)

if __name__ == '__main__':
    unittest.main()