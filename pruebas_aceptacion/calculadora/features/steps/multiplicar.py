from behave import given, when, then
from calculadora import calculadora

@when(u'realizo la multiplicación')
def step_impl(context):
    calc = calculadora()
    context.resultado = calc.multiplicar(context.num1, context.num2)

