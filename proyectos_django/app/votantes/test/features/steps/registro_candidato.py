from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono el botón de Log In')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)

@given(u'doy click en el enlace Candidatos')
def step_impl(context):
   context.driver.find_element(By.LINK_TEXT, 'Candidatos').click()
   time.sleep(2)


@given(u'luego click en el boton Agregar Candidato')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/ul/li/a').click()
    time.sleep(2)


@given(u'escribo el nombre de "{candidato}"')
def step_impl(context, candidato):
    context.driver.find_element(By.NAME, 'nombre').send_keys(candidato)
    time.sleep(2)


@given(u'selecciono el partido "{partido}"')
def step_impl(context, partido):
    context.driver.find_element(By.NAME, 'partido').send_keys(partido)
    time.sleep(2)


@when(u'presiono el botón de Guardar')
def step_impl(context):
    context.driver.find_element(By.NAME, '_save').click()
    time.sleep(2)
    


@then(u'puedo ver el candidato "{candidato}" en la lista de candidatos')
def step_impl(context, candidato):
    lista = context.driver.find_element(By.ID, 'result_list')
    assert candidato in lista.text, f"No se registró el candidato: {candidato}"
    time.sleep(2)
    