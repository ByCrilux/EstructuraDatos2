class Calculator():
    """"Una simple calculadora que realiza operaciones básicas cambio"""
    def __init__(self):
        self._a = 0
        self._b = 0
        
    def pedir_valores(self, valor_1, valor_2):
        """Asigna los valores a y b para las operaciones"""
        self._a = valor_1
        self._b = valor_2

    def sumar(self):
        return self._a + self._b
    
    def restar(self):
        return self._a - self._b
    
    def multiplicar(self):
        return self._a * self._b
    
    def devidir(self):
        return self._a / self._b