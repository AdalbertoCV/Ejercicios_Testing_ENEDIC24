from behave import given, when, then
from calculadora import calculadora

@when(u'realizo la potencia')
def step_impl(context):
    calc = calculadora()
    context.resultado = calc.potencia(context.num1, context.num2)