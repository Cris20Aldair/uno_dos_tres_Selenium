# uno_dos_tres_Seleniu
Es un proyecto basado en Python con algunos Frameworks (pytest, allure-pytest ,openpyxl, behave, unittest) combinado con Selenium.
Para poder ejecutar este enterno de pruebas es nesesario tener e intalar:
Python3 desde su pagina oficial y validado su corre instalacion desde la consola con (python3 --version)
PIP desde la consola python get-pip.py y validado su corre instalacion(pip --version)
pytest desde la consola python  (python -m pip install -U pytest)
Selenium desde la consola python  (python -m pip install -U selenium)
Allure desde la consola python  (python -m pip install -U allure-behave)
Lectura de archivos desde la consola python  (python -m pip install -U openpyxl)
Ejecucion de las pruebas desde la consola python  (python -m pip install -U behave)
Ejecucion por testset desde la consola python  (python -m pip install unittest-xml-reporting)
Despues de intalar todo los Frameworks se puede validar la intalacion correcta con en la copnsola con (pip list)
Despues cona pycharm (recomendado) se abre el proyecto dejando como carpeta rais ("uno_dos_tres_Selenium")
Siguiendo con el proseo de configuracion se abre el archivo de funcionalidades y en la funcionalidad de "get_json_file" y "datosleer" se actualizan las rutas absolutas 
de acuerdo a como esten en su equipo.
Por ultimo en la la funcin "abrir_navegador" en la linea self.driver = webdriver.Chrome("aqui ruta del chromedriver") agregar la ruta de le chromedriver y en el llamda de dicha funcion en el archivo prinsipal tst_001 y tst_002 cambiar safari por chrome como en el ejemplo:  Fun.abrir_navegador(self, "chrome") 
Despues de concluir con la configuracion, se abre las pruebas ubicadas en test tst_001 y tst_002 las cuales solo hay que abrirlas y con clic derecho se selecciona "Run Python test for tst...."
