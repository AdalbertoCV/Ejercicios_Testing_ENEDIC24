from edades import edades
import unittest

class Test_promedio(unittest.TestCase):
    def setUp(self):
        self.e = edades()

    def tearDown(self):
        pass

    def test_no_existes(self):
        resultado = self.e.mensaje(-5)
        self.assertEqual('No existes', resultado)

    def test_no_existes_2(self):
        resultado = self.e.mensaje(-1)
        self.assertEqual('No existes', resultado)

    def test_eres_ninio(self):
        resultado = self.e.mensaje(0)
        self.assertEqual('Eres niño', resultado)

    def test_eres_ninio_2(self):
        resultado = self.e.mensaje(5)
        self.assertEqual('Eres niño', resultado)

    def test_eres_adolescente(self):
        resultado = self.e.mensaje(13)
        self.assertEqual('Eres adolescente', resultado)

    def test_eres_adolescente_2(self):
        resultado = self.e.mensaje(17)
        self.assertEqual('Eres adolescente', resultado)

    def test_eres_Adulto(self):
        resultado = self.e.mensaje(30)
        self.assertEqual('Eres adulto', resultado)

    def test_eres_Adulto_2(self):
        resultado = self.e.mensaje(64)
        self.assertEqual('Eres adulto', resultado)

    def test_Eres_adulto_mayor(self):
        resultado = self.e.mensaje(119)
        self.assertEqual('Eres adulto mayor', resultado)

    def test_Eres_adulto_mayor_2(self):
        resultado = self.e.mensaje(80)
        self.assertEqual('Eres adulto mayor', resultado)

    def test_mumm_ra(self):
        resultado = self.e.mensaje(150)
        self.assertEqual('Eres Mumm-Ra', resultado)

    def test_mumm_ra_2(self):
        resultado = self.e.mensaje(1000)
        self.assertEqual('Eres Mumm-Ra', resultado)

    def test_edad_cadena(self):
        resultado = self.e.mensaje('hola')
        self.assertEqual('No se permiten cadenas', resultado)

    def test_edad_decimal(self):
        resultado = self.e.mensaje(12.4)
        self.assertEqual('Solo numeros enteros', resultado)

    def test_edad_true(self):
        resultado = self.e.mensaje(True)
        self.assertEqual('No se permiten booleanos', resultado)

    def test_edad_lista(self):
        resultado = self.e.mensaje([])
        self.assertEqual('No se permiten listas', resultado)
        
    def test_edad_diccionario(self):
        resultado = self.e.mensaje({})
        self.assertEqual('Elemento proporcionado no válido', resultado)

if __name__ == '__main__': #pragma: no cover
    unittest.main()
