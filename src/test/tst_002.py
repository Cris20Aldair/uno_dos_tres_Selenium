# -*- coding: utf-8 -*-
import time
import unittest
from src.functions.functions import Function as Fun
##Descripcion ##Este caso de prueba valida que el pago con una nueva targeta de se realice de forma correcta y del monto correcto y al numero correcto 
##Autor       ##Uno Dos Tres
##Fecha       ##04/03/2022

class Test002(unittest.TestCase):

    def test_002(self):
        Fun.abrir_navegador(self, "safari")
        Fun.get_json_file(self)
        Fun.get_entity(self, "operator")
        Fun.get_elements(self, "operator").click()
        Fun.get_elements(self, "telcel").click()
        time.sleep(1)
        Fun.get_elements(self, "mobile").send_keys(Fun.datosleer(self, "A2"))

        Fun.get_elements(self, "amount").click()

        Fun.get_elements(self, "amount10").click()

        Fun.get_elements(self, "siguiente").click()
        time.sleep(5)
        Fun.get_elements(self, "targeta").click()
        time.sleep(1)
        Fun.get_elements(self, "nuevatargeta").click()
        time.sleep(1)
        Fun.get_elements(self, "numtargeta").send_keys("4111111111111111")

        Fun.get_elements(self, "mes").send_keys(Fun.datosleer(self, "C2"))

        Fun.get_elements(self, "año").send_keys(Fun.datosleer(self, "D2"))

        Fun.get_elements(self, "cv").send_keys(Fun.datosleer(self, "E2"))

        Fun.get_elements(self, "correo1").send_keys(Fun.datosleer(self, "F2"))
        Fun.esperar_elemento(self, "pagartargeta")
        Fun.get_elements(self, "pagartargeta").click()
        Fun.esperar_elemento(self, "user")
        Fun.get_elements(self, "user").send_keys(Fun.datosleer(self, "G2"))
        time.sleep(2)
        Fun.get_elements(self, "password").send_keys(Fun.datosleer(self, "H2"))
        time.sleep(2)
        Fun.saltoiframe(self)
        time.sleep(3)
        Fun.get_elements(self, "robot").click()
        time.sleep(2)
        Fun.regresarframe(self)
        time.sleep(2)
        Fun.get_elements(self, "acceso").click()
        Fun.esperar_elemento(self, "recargaexitosa")
        assert Fun.get_text(self, "recargaexitosa") == "¡Recarga Exitosa!"
        assert Fun.get_text(self, "recargaexitosamonto") == " $10"
        assert Fun.get_text(self, "recargaalnumero") == "Recarga Saldo de Telcel al número 8465433546"

    def tearDown(self):
        Fun.cerrar_navegador(self)


if __name__ == '__main__':
    unittest.main()
