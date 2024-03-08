from behave import given, when, then
from calculadora import calculadora

@given(u'que el usuario ingresa los numeros "{num1}" y "{num2}"')
def step_impl(context, num1,  num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'realizo el cálculos')
def step_impl(context):
    calc = calculadora()
    context.resultado = calc.sumar(context.num1, context.num2)


@then(u'puede ver el resultado igual a "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == int(esperado)


@given(u'que el usuario ingresa el caractér "{caracter}" y el número "{num2}"')
def step_impl(context, caracter, num2):
    context.num1 = caracter
    context.num2 = int(num2)


@then(u'puede ver el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    assert context.resultado == mensaje

@given(u'que el usuario ingresa el booleano "{booleano}" y el número "{num2}"')
def step_impl(context, booleano, num2):
    context.num1 = bool(booleano)
    context.num2 = int(num2)

@given(u'que el usuario ingresa el entero "{num1}" y el decimal "{decimal}"')
def step_impl(context, num1, decimal):
    context.num1 = int(num1)
    context.num2 = float(decimal)

@given(u'que el usuario ingresa la lista "{lista}" y el número "{num2}"')
def step_impl(context, lista, num2):
    context.num1 = list(lista)
    context.num2 = int(num2)


    