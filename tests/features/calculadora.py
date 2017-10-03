
class Calculadora():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        try:
            self.resultado = num1 + num2
        except:
            self.resultado = 'datos incorrectos'

    def resta(self, num1, num2):
        try:
            self.resultado = num1 - num2
        except:
            self.resultado = 'datos incorrectos'

    def multiplicacion(self, num1, num2):
        try:
            int(num1)
            int(num2)
            self.resultado = num1 * num2
        except:
            self.resultado = 'datos incorrectos'

    def division(self, num1, num2):
        try:
            if(num2 == 0):
                self.resultado = 'no se puede dividir entre cero'
            else:
                self.resultado = num1 / num2
        except:
            self.resultado = 'datos incorrectos'

    def potencia(self, num1, num2):
        try:
            self.resultado = num1 ** num2
        except:
            self.resultado = 'datos incorrectos'

    def raiz2(self, num1):
        try:
            self.resultado = num1 ** 0.5
        except:
            self.resultado = 'datos incorrectos'
