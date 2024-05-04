from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@when(u'doy clic en el boton de votar a "{candidato}"')
def step_impl(context, candidato):
    boton = context.driver.find_element(By.NAME, str(candidato))
    boton.click()
    time.sleep(3)


@then(u'puedo ver el mensaje "{mensaje}" en pantalla')
def step_impl(context, mensaje):
    etiqueta = context.driver.find_elements(By.TAG_NAME, 'h1')
    assert etiqueta[0].text == mensaje, f"No aparece el mensaje {mensaje}"

@then(u'puedo ver el mensaje con el ganador en pantalla')
def step_impl(context):
    etiqueta = context.driver.find_elements(By.TAG_NAME, 'h3')
    assert "El ganador es:" in etiqueta[0].text, f"No aparece el mensaje del ganador"
