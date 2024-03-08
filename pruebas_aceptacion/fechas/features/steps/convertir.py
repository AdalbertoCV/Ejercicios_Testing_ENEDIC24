from behave import given, when, then
from fechas import fechas

@when(u'convierto la fecha')
def step_impl(context):
    f = fechas()
    context.resultado = f.convertir(context.fecha)


@given(u'que el usuario ingresa la fecha "{fecha}"')
def step_impl(context, fecha):
    context.fecha = str(fecha)

@then(u'obtengo la cadena "{cadena}"')
def step_impl(context, cadena):
    assert context.resultado == cadena