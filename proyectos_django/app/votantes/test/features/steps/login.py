from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso a la url "{url}"')
def step_impl(context,url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'escribo mi usuario "{usuario}" y mi contraseña "{password}"')
def step_impl(context,usuario, password):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(password)


@when(u'presiono el botón de Log In')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()


@then(u'puedo ver el usuario "{usuario}" en la barra principal')
def step_impl(context, usuario):
    div = context.driver.find_element(By.ID, 'user-tools')
    #time.sleep(10)
    assert usuario in div.text, f"El usuario {usuario} no se encuentra en {div.text}"


@then(u'puedo ver el error "{error}" en pantalla')
def step_impl(context, error):
    div = context.driver.find_element(By.CLASS_NAME, 'errornote')
    time.sleep(10)
    assert div, f"No aparece el mensaje: {mensaje}"