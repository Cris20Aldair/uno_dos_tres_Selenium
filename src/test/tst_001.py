# -*- coding: utf-8 -*-
import time
import unittest
from src.functions.functions import Function as Fun
##Descripcion ##Este caso de prueba valida que al ingresar los datos, numero,operador y monto permita navegar a la pantalla de resumend e la compra
##Autor       ##Uno Dos Tres
##Fecha       ##04/03/2022


class Test001(unittest.TestCase):

    def test_001(self):
        Fun.abrir_navegador(self, "safari")
        Fun.get_json_file(self)
        Fun.get_entity(self, "operator")
        Fun.get_elements(self, "operator").click()
        Fun.get_elements(self, "telcel").click()
        time.sleep(1)
        Fun.get_elements(self, "mobile").send_keys("8465433546")
        time.sleep(1)
        Fun.get_elements(self, "amount").click()
        time.sleep(1)
        Fun.get_elements(self, "amount10").click()
        time.sleep(1)
        Fun.get_elements(self, "siguiente").click()
        time.sleep(5)
        assert Fun.get_text(self, "resumen") == "Resumen de la compra"
        assert Fun.get_text(self, "monto") == "10"

    def tearDown(self):
        Fun.cerrar_navegador(self)


if __name__ == '__main__':
    unittest.main()
