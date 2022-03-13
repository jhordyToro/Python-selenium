import unittest
from selenium import webdriver
#Importar libreria ddt y extraer submodulos
from ddt import ddt, data, unpack #Permitira utilizar los datos y desempaquetarlos

#Colocar decorado
@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path= r'./geckodriver.exe')
        driver = self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('https://demo-store.seleniumacademy.com/')

    @data(('dress', 6),('music', 5)) #Decorador que almacena los elementos a buscar

    @unpack #Decorador para desempaquetar las tuplas y poder ingresar a ellass de forma individual

    #Agregaremos dos parametros al metodo uno para buscar y otro para validar
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        #Ubicar campo de busqueda
        search_field = driver.find_element_by_name('q')
        search_field.clear()#Limpiar en caso de que tengan algun texto

        #Ingresamos el valor a buscar
        search_field.send_keys(search_value)

        #Boton de busqueda
        search_button = driver.find_element_by_class_name('button')
        search_button.click()

        #Identificar donde estan los productos
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        #Verficiar que todo haya salido bien con un print statement
        print(f"Found {len(products)} products")

        #Ciclo for para imprimir los elementos de la pagina actual
        for i in products:
            print(i.text)

        #Assertion de validacion
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()