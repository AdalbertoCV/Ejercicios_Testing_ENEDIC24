# importamos el driver de selenium para comunicarnos con el navegador
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# inicializamos el driver con un navegador
driver = webdriver.Chrome()

driver.get("https://google.com")
# obtenemos el buscador de google 
q = driver.find_element(By.NAME, "q")
# enviamos una busqueda al query
q.send_keys("Empleos en NASA" + Keys.RETURN)
# podemos buscar por id para extraer elementos de una seccion específica.
resultados = driver.find_element(By.ID, "res")
# recuperamos todos los h3 (titulos de búsqueda)
items = resultados.find_elements(By.TAG_NAME, 'h3')
# iteramos los items
for i in items:
    if i.text != '':
        print(i.text)
# ponemos un sleep para evitar que el script se cierre automáticamente
time.sleep(25)