import unittest

from calculadora import Calculadora
#Implementando travis CI

class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_es_igual_a_cero(self):
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_sumar_2_mas_2_igual_a_4(self):
        self.calc.suma(2,2)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_sumar_3_mas_3_igual_a_6(self):
        self.calc.suma(3,3)
        self.assertEquals(self.calc.obtener_resultado(), 6)

    def test_sumar_menos_1_mas_2_igual_a_1(self):
        self.calc.suma(-1,2)
        self.assertEquals(self.calc.obtener_resultado(), 1)

    def test_sumar_L_mas_2_igual_a_datos_incorrectos(self):
        self.calc.suma('L',2)
        self.assertEquals(self.calc.obtener_resultado(), 'datos incorrectos')

    def test_restar_3_menos_2_igual_a_1(self):
        self.calc.resta(3,2)
        self.assertEquals(self.calc.obtener_resultado(), 1)

    def test_restar_5_menos_6_igual_a_menos_1(self):
        self.calc.resta(5,6)
        self.assertEquals(self.calc.obtener_resultado(), -1)

    def test_restar_J_menos_6_igual_a_datos_incorrectos(self):
        self.calc.resta('J',6)
        self.assertEquals(self.calc.obtener_resultado(), 'datos incorrectos')

    def test_multiplicar_8_por_0_igual_a_0(self):
        self.calc.multiplicacion(8,0)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_multiplicar_2_por_2_igual_a_4(self):
        self.calc.multiplicacion(2,2)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_multiplicar_menos_3_por_menos_1_igual_a_3(self):
        self.calc.multiplicacion(-3,-1)
        self.assertEquals(self.calc.obtener_resultado(), 3)

    def test_multiplicar_T_por_3_igual_a_datos_incorrectos(self):
        self.calc.multiplicacion('T',3)
        self.assertEquals(self.calc.obtener_resultado(), 'datos incorrectos')

    def test_dividir_10_entre_2_igual_a_5(self):
        self.calc.division(10,2)
        self.assertEquals(self.calc.obtener_resultado(), 5)

    def test_dividir_8_entre_0_igual_a_No_sepuede_dividir(self):
        self.calc.division(8,0)
        self.assertEquals(self.calc.obtener_resultado(), 'no se puede dividir entre cero')

    def test_dividir_R_entre_8_igual_a_datos_incorrectos(self):
        self.calc.division('R',8)
        self.assertEquals(self.calc.obtener_resultado(), 'datos incorrectos')

    def test_potenciar_3_a_la_2_igual_a_9(self):
        self.calc.potencia(3,2)
        self.assertEquals(self.calc.obtener_resultado(), 9)

    def test_potenciar_9_a_la_0_igual_a_1(self):
        self.calc.potencia(9,0)
        self.assertEquals(self.calc.obtener_resultado(), 1)

    def test_potenciar_X_a_la_3_igual_a_datos_incorrectos(self):
        self.calc.potencia('X',3)
        self.assertEquals(self.calc.obtener_resultado(), 'datos incorrectos')

    def test_raiz_cuadrada_de_9_igual_a_3(self):
        self.calc.raiz2(9)
        self.assertEquals(self.calc.obtener_resultado(), 3)

    def test_raiz_cuadrada_de_16_igual_a_4(self):
        self.calc.raiz2(16)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_raiz_cuadrada_de_G_igual_a_datos_incorrectos(self):
        self.calc.raiz2('G')
        self.assertEquals(self.calc.obtener_resultado(), 'datos incorrectos')



if __name__== '__main__':
    unittest.main()