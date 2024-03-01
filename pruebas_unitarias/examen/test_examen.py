from examen import numeros_a_letras
import unittest

class Test_promedio(unittest.TestCase):
    def setUp(self):
        self.c = numeros_a_letras()

    def tearDown(self):
        pass

    def test_unidades(self):
        resultado = self.c.convertir(9)
        self.assertEqual(resultado,'nueve')

    def test_decenas_cerrado(self):
        resultado = self.c.convertir(20)
        self.assertEqual(resultado,'veinte')

    def test_decenas_no_cerrado(self):
        resultado = self.c.convertir(48)
        self.assertEqual(resultado,'cuarenta y ocho')

    def test_centenas_cerrado(self):
        resultado = self.c.convertir(400)
        self.assertEqual(resultado,'cuatrocientos')

    def test_centenas_no_cerrado(self):
        resultado = self.c.convertir(451)
        self.assertEqual(resultado,'cuatrocientos cincuenta y uno')

    def test_miles_enteros(self):
        resultado = self.c.convertir(1000)
        self.assertEqual(resultado,'mil')

    def test_especiales(self):
        resultado = self.c.convertir(15)
        self.assertEqual(resultado,'quince')

    def test_miles_no_enteros(self):
        resultado = self.c.convertir(1250)
        self.assertEqual(resultado,'mil doscientos cincuenta')

    def test_cien_miles(self):
        resultado = self.c.convertir(100000)
        self.assertEqual(resultado,'cien mil')

    def test_cien_miles_no_cerrados(self):
        resultado = self.c.convertir(152500)
        self.assertEqual(resultado,'ciento cincuenta y dos mil quinientos')

    def test_millon(self):
        resultado = self.c.convertir(1000000)
        self.assertEqual(resultado,'un millón')

    def test_millon_con_miles(self):
        resultado = self.c.convertir(1540250)
        self.assertEqual(resultado,'un millón quinientos cuarenta mil doscientos cincuenta')

    def test_millones_miles_cientos_decenas_unidades(self):
        resultado = self.c.convertir(100567899)
        self.assertEqual(resultado,'cien millones quinientos sesenta y siete mil ochocientos noventa y nueve')

    def test_mil_millones(self):
        resultado = self.c.convertir(1000000000)
        self.assertEqual(resultado,'mil millones')

    def test_sobre_rango(self):
        resultado = self.c.convertir(1000000000000)
        self.assertEqual(resultado,'No se permiten numeros mayores a mil millones.')

    def test_cero(self):
        resultado = self.c.convertir(0)
        self.assertEqual(resultado,'cero')

    def test_numeros_negativos(self):
        resultado = self.c.convertir(-10)
        self.assertEqual(resultado,'Ingrese numeros positivos')

if __name__ == '__main__': #pragma: no cover
    unittest.main()

