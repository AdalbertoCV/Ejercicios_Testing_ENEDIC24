import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = calculadora()

    def tearDown(self):
        pass

    def test_sumar_dos_mas_dos(self):
        resultado = self.calc.sumar(2,2)
        self.assertEqual(4, resultado)

    def test_sumar_dos_mas_tres(self):
        resultado = self.calc.sumar(2,3)
        self.assertEqual(5, resultado)

    def test_sumar_diez_mas_tres(self):
        resultado = self.calc.sumar(10,3)
        self.assertEqual(13, resultado)

    def test_sumar_true_mas_tres(self):
        resultado = self.calc.sumar(True,3)
        self.assertEqual('No se permiten booleanos', resultado)

    def test_sumar_menosdos_mas_menos3(self):
        resultado = self.calc.sumar(-2,-3)
        self.assertEqual('Sólo numeros positivos', resultado)

    def test_sumar_uno_mas_nuevepuntocinco(self):
        resultado = self.calc.sumar(1,9.5)
        self.assertEqual('Sólo numeros enteros', resultado)

    def test_sumar_lista_mas_nueve(self):
        resultado = self.calc.sumar([],9)
        self.assertEqual('Sólo numeros, no listas', resultado)

    def test_restar_ocho_menos_dos(self):
        resultado = self.calc.restar(8,2)
        self.assertEqual(6, resultado)

    def test_restar_menostres_menos_dos(self):
        resultado = self.calc.restar(-3,2)
        self.assertEqual(-5, resultado)

    def test_restar_hola_menos_dos(self):
        resultado = self.calc.restar('hola',2)
        self.assertEqual('No se permiten cadenas de texto', resultado)

    def test_restar_lista_menos_dos(self):
        resultado = self.calc.restar([],2)
        self.assertEqual('No se permiten listas', resultado)
    
    def test_restar_docepuntocuatro_menos_dos(self):
        resultado = self.calc.restar(12.4,2)
        self.assertEqual('No se permiten decimales', resultado)

    def test_restar_diccionario_menos_tres(self):
        resultado = self.calc.restar({},3)
        self.assertEqual('Elemento no valido para la operacion', resultado)

    def test_restar_true_menos_tres(self):
        resultado = self.calc.restar(True,3)
        self.assertEqual('No se permiten booleanos', resultado)

    def test_multiplicar_ocho_por_dos(self):
        resultado = self.calc.multiplicar(8,2)
        self.assertEqual(16, resultado)

    def test_multiplicar_menostres_por_dos(self):
        resultado = self.calc.multiplicar(-3,2)
        self.assertEqual(-6, resultado)

    def test_multiplicar_hola_por_dos(self):
        resultado = self.calc.multiplicar('hola',2)
        self.assertEqual('No se permiten cadenas de texto', resultado)

    def test_multiplicar_lista_por_dos(self):
        resultado = self.calc.multiplicar([],2)
        self.assertEqual('No se permiten listas', resultado)

    def test_multiplicar_docepuntocuatro_por_dos(self):
        resultado = self.calc.multiplicar(12.4,2)
        self.assertEqual('No se permiten decimales', resultado)

    def test_multiplicar_diccionario_por_tres(self):
        resultado = self.calc.multiplicar({},3)
        self.assertEqual('Elemento no valido para la operacion', resultado)

    def test_multiplicar_true_por_tres(self):
        resultado = self.calc.multiplicar(True,3)
        self.assertEqual('No se permiten booleanos', resultado)

    def test_dividir_uno_entre_dos(self):
        resultado = self.calc.dividir(1,2)
        self.assertEqual(0.5,resultado)

    def test_dividir_diez_entre_tres(self):
        resultado = self.calc.dividir(10,3)
        self.assertEqual(3.33,resultado)

    def test_dividir_veinte_entre_cero(self):
        resultado = self.calc.dividir(20,0)
        self.assertEqual('No se puede dividir entre cero',resultado)

    def test_dividir_y_entre_dos(self):
        resultado = self.calc.dividir('y',2)
        self.assertEqual('No se permiten cadenas de texto',resultado)

    def test_dividir_lista_entre_dos(self):
        resultado = self.calc.dividir([],2)
        self.assertEqual('No se permiten listas',resultado)

    def test_dividir_ochopuntocuatro_entre_dos(self):
        resultado = self.calc.dividir(8.4,2)
        self.assertEqual('No se permiten decimales',resultado)

    def test_dividir_diccionario_entre_tres(self):
        resultado = self.calc.dividir({},3)
        self.assertEqual('Elemento no valido para la operacion',resultado)

    def test_dividir_true_entre_tres(self):
        resultado = self.calc.dividir(True,3)
        self.assertEqual('No se permiten booleanos',resultado)

    def test_raiz_cuadrada_de_cuatro(self):
        resultado = self.calc.sqrt(4,2)
        self.assertEqual(2,resultado)

    def test_raiz_tercera_de_ocho(self):
        resultado = self.calc.sqrt(8,3)
        self.assertEqual(2,resultado)

    def test_raiz_cuarta_de_once(self):
        resultado = self.calc.sqrt(11,4)
        self.assertEqual(1.82,resultado)

    def test_raiz_decimal(self):
        resultado = self.calc.sqrt(2.3,2)
        self.assertEqual('No se permiten decimales',resultado)

    def test_raiz_negativa(self):
        resultado = self.calc.sqrt(-1,2)
        self.assertEqual('No se permiten raíces negativas',resultado)

    def test_raiz_booleano(self):
        resultado = self.calc.sqrt(True,2)
        self.assertEqual('No se permiten booleanos',resultado)

    def test_raiz_cadena(self):
        resultado = self.calc.sqrt('y',2)
        self.assertEqual('No se permiten cadenas de texto',resultado)

    def test_raiz_lista(self):
        resultado = self.calc.sqrt([],2)
        self.assertEqual('No se permiten listas',resultado)

    def test_raiz_diccionario(self):
        resultado = self.calc.sqrt({},2)
        self.assertEqual('Elemento no valido para la operacion',resultado)

    def test_potencia_dos_ala_tres(self):
        resultado = self.calc.potencia(2,3)
        self.assertEqual(8,resultado)

    def test_potencia_cuatro_cuadrado(self):
        resultado = self.calc.potencia(4,2)
        self.assertEqual(16,resultado)

    def test_potencia_decimal(self):
        resultado = self.calc.potencia(2.3,3)
        self.assertEqual('No se permiten decimales',resultado)

    def test_potencia_negativa(self):
        resultado = self.calc.potencia(-1,3)
        self.assertEqual('No se permiten numeros negativos',resultado)

    def test_potencia_booleana(self):
        resultado = self.calc.potencia(True,3)
        self.assertEqual('No se permiten booleanos',resultado)

    def test_potencia_cadena(self):
        resultado = self.calc.potencia('y',3)
        self.assertEqual('No se permiten cadenas de texto',resultado)

    def test_potencia_lista(self):
        resultado = self.calc.potencia([],3)
        self.assertEqual('No se permiten listas',resultado)

    def test_potencia_diccionario(self):
        resultado = self.calc.potencia({},3)
        self.assertEqual('Elemento no valido para la operacion',resultado)

    def test_resta_true_menos_tres(self):
        resultado = self.calc.restar(True,3)
        self.assertEqual('No se permiten booleanos',resultado)

    def test_multiplicacion_true_por_tres(self):
        resultado = self.calc.multiplicar(True,3)
        self.assertEqual('No se permiten booleanos',resultado)

    def test_raiz_booleana(self):
        resultado = self.calc.sqrt(True,3)
        self.assertEqual('No se permiten booleanos',resultado)

    def test_division_exacta(self):
        resultado = self.calc.dividir(1,1)
        self.assertEqual(1, resultado)

if __name__ == '__main__': #pragma: no cover
    unittest.main()