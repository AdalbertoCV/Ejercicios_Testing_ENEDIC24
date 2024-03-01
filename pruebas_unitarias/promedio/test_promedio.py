from promedio import promedio
import unittest

class Test_promedio(unittest.TestCase):
    def setUp(self):
        self.p = promedio()

    def tearDown(self):
        pass

    def test_promedio_enteros(self):
        resultado = self.p.calcular(10,10,10)
        self.assertEqual(10.0, resultado)

    def test_promedio_decimales(self):
        resultado = self.p.calcular(9,9.5,7)
        self.assertEqual(8.5, resultado)

    def test_promedio_enteros_2(self):
        resultado = self.p.calcular(5,6,6)
        self.assertEqual(5.67, resultado)

    def test_promedio_cadenas(self):
        resultado = self.p.calcular('a',10,10)
        self.assertEqual('No se aceptan cadenas de texto', resultado)

    def test_promedio_listas(self):
        resultado = self.p.calcular([],10,10)
        self.assertEqual('No se aceptan listas', resultado)

    def test_promedio_booleanos(self):
        resultado = self.p.calcular(10,True,10)
        self.assertEqual('No se aceptan booleanos', resultado)

    def test_promedios_negativos(self):
        resultado = self.p.calcular(-5,10,10)
        self.assertEqual('No se aceptan numeros negativos', resultado)

    def test_promedios_mayores_limite(self):
        resultado = self.p.calcular(10,20,10)
        self.assertEqual('La calificación máxima es 10', resultado)

    def test_promedios_elemento_no_valido(self):
        resultado = self.p.calcular(10,{},10)
        self.assertEqual('Elementos no válidos para el cálculo', resultado)

    def test_promedios_nulos(self):
        resultado = self.p.calcular(10,None,10)
        self.assertEqual('No se aceptan valores nulos', resultado)

if __name__ == '__main__': #pragma: no cover
    unittest.main()