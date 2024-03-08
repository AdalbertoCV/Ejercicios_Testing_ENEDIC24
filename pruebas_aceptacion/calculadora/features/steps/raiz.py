from behave import given, when, then
from calculadora import calculadora

@when(u'realizo la raiz')
def step_impl(context):
    calc = calculadora()
    context.resultado = calc.sqrt(context.num1, context.num2)