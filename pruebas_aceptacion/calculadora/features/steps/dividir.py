from behave import given, when, then
from calculadora import calculadora

@when(u'realizo la división')
def step_impl(context):
    calc = calculadora()
    context.resultado = calc.dividir(context.num1, context.num2)