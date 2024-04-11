# importamos el driver de selenium para comunicarnos con el navegador
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from credenciales import usuario, clave

# inicializamos el driver con un navegador
driver = webdriver.Chrome()
# inicializamos la url para acceder
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=23&ct=1712714727&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC9qdW5rZW1haWwv%26RpsCsrfState%3d19d3d2f6-aa51-f5e8-9a7e-4195a0b5c5eb&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
# obtenemos el campo de usuario
driver.find_element(By.ID, "i0116").send_keys(usuario + Keys.RETURN)
# obtenemos el campos de contraseña
time.sleep(10)
driver.find_element(By.ID, 'i0118').send_keys(clave + Keys.RETURN)
# obtenemos el boton para enviar datos
time.sleep(10)
driver.find_element(By.ID, 'acceptButton').click()
# Esperar un momento para asegurarnos de que la página se cargue completamente
time.sleep(10)
# Hacer clic en el elemento que representa la carpeta de "Correo no deseado"
carpeta_correo_no_deseado = driver.find_element(By.XPATH, "//span[contains(text(),'Junk Email')]")
carpeta_correo_no_deseado.click()
# Esperar un momento para asegurarnos de que la página se cargue completamente
time.sleep(10)
# Obtener todos los elementos de correo no deseado
elementos_correo_no_deseado = driver.find_elements(By.XPATH, "//div[@role='checkbox']")
# Iterar sobre los elementos y seleccionarlos (marcar para eliminar)
for elemento in elementos_correo_no_deseado:
    elemento.click()
# Esperar un momento para asegurarnos de que todos los correos estén seleccionados
time.sleep(10)
# Hacer clic en el botón de eliminar
driver.find_element(By.XPATH, "//button[contains(text(),'Eliminar')]").click()

time.sleep(10)
# Obtener todos los elementos que contienen los títulos de los correos recibidos
elementos = driver.find_elements(By.XPATH, "//div[contains(@class, 'XVsEB')]/span[@class='gtcPn']")
# Crear una lista para almacenar los títulos de los correos
titulos_correos = []
# Iterar sobre los elementos y obtener el texto de cada título de correo
for titulo_correo in elementos:
    titulos_correos.append(titulo_correo.text)
# Imprimir la lista de títulos de los correos recibidos
print("Títulos de los correos recibidos:")
for titulo_correo in titulos_correos:
    print(titulo_correo)
time.sleep(50)