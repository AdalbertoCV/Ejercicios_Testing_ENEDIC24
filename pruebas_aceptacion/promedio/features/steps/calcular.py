from behave import given, when, then
from promedio import promedio

@when(u'calculo el promedio')
def step_impl(context):
    p = promedio()
    context.resultado = p.calcular(context.cal1, context.cal2, context.cal3)


@then(u'puede ver el resultado igual a "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == float(esperado)

@then(u'puede ver el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    assert context.resultado == mensaje

@given(u'que el usuario ingresa las calificaciones "{c1}", "{c2}" y "{c3}"')
def step_impl(context, c1, c2, c3):
    context.cal1 = float(c1)
    context.cal2 = float(c2)
    context.cal3 = float(c3)

@given(u'que el usuario ingresa las calificaciones "{c1}", "{c2}" y la cadena "{cadena}"')
def step_impl(context, c1, c2 , cadena):
    context.cal1 = float(c1)
    context.cal2 = float(c2)
    context.cal3 = str(cadena)


@given(u'que el usuario ingresa las calificaciones "{c1}", "{c2}" y el booleano "{booleano}"')
def step_impl(context, c1, c2, booleano):
    context.cal1 = float(c1)
    context.cal2 = float(c2)
    context.cal3 = bool(booleano)


@given(u'que el usuario ingresa las calificaciones "{c1}", "{c2}" y nulo')
def step_impl(context, c1, c2):
    context.cal1 = float(c1)
    context.cal2 = float(c2)
    context.cal3 = None

