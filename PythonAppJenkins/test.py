import unittest
import calculadora
import xmlrunner

class TestCalculadora(unittest.TestCase):
    def teste_adiciona_inteiros(self):
        resultado = calculadora.add(2,2)
        self.assertEqual(resultado,4)
    def teste_adiciona_decimais(self):
        resultado = calculadora.add('5.3',2)
        self.assertEqual(resultado,7.3)
    def teste_adiciona_string_inteiro(self):
        resultado = calculadora.add('sergio',2)
        self.assertEqual(resultado,'sergio2')
    def teste_adiciona_string_decimal(self):
        resultado = calculadora.add('sergio','2.2')
        self.assertEqual(resultado,'sergio2.2')
    def teste_adiciona_string(self):
        resultado = calculadora.add('sergio',' fontes')
        self.assertEqual(resultado,'sergio fontes')

if __name__ =="__main__":
    #unittest.main()
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output='relatorio-testes'))