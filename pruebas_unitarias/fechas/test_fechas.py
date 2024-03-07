from fechas import fechas
import unittest

class Test_promedio(unittest.TestCase):
    def setUp(self):
        self.f = fechas()

    def tearDown(self):
        pass

    def test_enero_dos_mil(self):
        resultado = self.f.convertir("10/1/2000")
        self.assertEqual('diez de enero año dos mil', resultado)

    def test_febrero_mil_ochocientos(self):
        resultado = self.f.convertir("15/2/2000")
        self.assertEqual('quince de febrero año dos mil', resultado)

    def test_marzo_dos_mil_doce(self):
        resultado = self.f.convertir("11/3/2012")
        self.assertEqual('once de marzo año dos mil doce', resultado)

    def test_abril_mil_novescientos_noventaynueve(self):
        resultado = self.f.convertir("21/4/2100")
        self.assertEqual('veinte y uno de abril año dos mil cien', resultado)

    def test_mayo_mil_novescientos_noventayocho(self):
        resultado = self.f.convertir("19/5/2000")
        self.assertEqual('diecinueve de mayo año dos mil', resultado)

    def test_junio_mil_cuarenta(self):
        resultado = self.f.convertir("19/6/2040")
        self.assertEqual('diecinueve de junio año dos mil cuarenta', resultado)

    def test_julio_dosmil_cuarenta(self):
        resultado = self.f.convertir("20/7/2040")
        self.assertEqual('veinte de julio año dos mil cuarenta', resultado)

    def test_agosto_dosmil_cuarenta(self):
        resultado = self.f.convertir("20/8/2040")
        self.assertEqual('veinte de agosto año dos mil cuarenta', resultado)

    def test_septiembre_dosmil_catorce(self):
        resultado = self.f.convertir("1/9/2014")
        self.assertEqual('uno de septiembre año dos mil catorce', resultado)

    def test_octubre_dosmil_catorce(self):
        resultado = self.f.convertir("2/10/2014")
        self.assertEqual('dos de octubre año dos mil catorce', resultado)

    def test_noviembre_dosmil_dos(self):
        resultado = self.f.convertir("2/11/2002")
        self.assertEqual('dos de noviembre año dos mil dos', resultado)

    def test_diciembre_dosmil_uno(self):
        resultado = self.f.convertir("31/12/2001")
        self.assertEqual('treinta y uno de diciembre año dos mil uno', resultado)

    def test_limite_día(self):
        resultado = self.f.convertir("33/11/1000")
        self.assertEqual('día fuera de rango', resultado)

    def test_limite_mes(self):
        resultado = self.f.convertir("30/13/1000")
        self.assertEqual('mes fuera de rango', resultado)

    def test_limite_anio(self):
        resultado = self.f.convertir("30/12/1000000000000")
        self.assertEqual('año fuera de rango', resultado)

    def test_foramto_incorrecto(self):
        resultado = self.f.convertir("30/13/hola")
        self.assertEqual('formato de fecha incorrecto', resultado)

if __name__ == '__main__': #pragma: no cover
    unittest.main()