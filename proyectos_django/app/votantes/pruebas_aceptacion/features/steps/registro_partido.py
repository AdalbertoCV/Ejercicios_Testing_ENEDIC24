from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'doy click en el enlace Partidos')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Partidos').click()
    time.sleep(2)


@given(u'luego click en el boton Agregar Partido')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/ul/li/a').click()
    time.sleep(2)


@given(u'escribo la descripción "{descripcion}"')
def step_impl(context, descripcion):
    context.driver.find_element(By.NAME, 'descripcion').send_keys(descripcion)
    time.sleep(2)


@given(u'selecciono la imagen "{Imagen}"')
def step_impl(context, Imagen):
    context.driver.find_element(By.NAME, 'logo').send_keys(Imagen)
    time.sleep(2)


@then(u'puedo ver el partido "{partido}" en la lista de partidos')
def step_impl(context, partido):
    lista = context.driver.find_element(By.ID, 'result_list')
    assert partido in lista.text, f"No se registró el partido: {partido}"
    time.sleep(2)