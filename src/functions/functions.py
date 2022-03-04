from selenium import webdriver
import os
import openpyxl
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Function:

    def __init__(self):
        self.json_strings = None
##Funcion que permite abriri la URL tanto en Chrome o Safari
    def abrir_navegador(self, explorador):

        if explorador == ("safari"):
            self.driver = webdriver.Safari()
            self.driver.maximize_window()
            self.driver.get('http://sanbox.undostres.com.mx')

        if explorador == ("chrome"):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get('http://sanbox.undostres.com.mx')
##Funcion que permite cerrar el navegador en condiciones de error o al finalizar la ejecucion 
    def cerrar_navegador(self):
        print("Cerrando navegador")
        self.driver.quit()
##Funcion que permite abrir un archivo Json
    def get_json_file(self):
        json_path = "/Users/chrismonroy/Documents/Python3/src/pages/selector.json"
        with open(json_path, "r") as read_file:
            self.json_strings = json.loads(read_file.read())
##Funcion que permite interactuar con el Json
    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["selector"]
                self.json_GetFieldBy = self.json_strings[entity]["identi"]
                return True
            except KeyError:
                print(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                Function.cerrar_navegador(self)
                return None
##Funcion que evaluo que tipo de objto es y interactuar con el Json
    def get_elements(self, entity):

        global elements
        Get_Entity = Function.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)
                return elements
            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Function.cerrar_navegador(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Function.cerrar_navegador(self)

##Lee los elementos de pantalla y los cambia a texto para coparar
    def get_text(self, entity):
        global elements
        Get_Entity = Function.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Function.cerrar_navegador(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Function.cerrar_navegador(self)
##Salto a un iFrame
    def saltoiframe(self):
        a = "/html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/form/div[4]/div/div/iframe"
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(a))
##Regrsar a la pagina prinsipal
    def regresarframe(self):
        self.driver.switch_to.default_content()
##Funcion que permite esperar que sea interactuable un objeto 
    def esperar_elemento(self, locator):
        Get_Entity = Function.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    return True

            except TimeoutException:
                print(u"Esperar_Elemento: No presente " + locator)
                Function.cerrar_navegador(self)
            except NoSuchElementException:
                print(u"Esperar_Elemento: No presente " + locator)
                Function.cerrar_navegador(self)
##Funcion que permite leer los datos de un .xlsx
    def datosleer(self, celda):

        wb = openpyxl.load_workbook('/Users/chrismonroy/Documents/Python3/src/data/Datos.xlsx')
        sheet = wb["Sheet1"]
        valor = str(sheet[celda].value)
        return valor
