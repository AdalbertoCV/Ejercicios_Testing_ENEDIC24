from behave import given, when, then
from calculadora import calculadora

@when(u'realizo la resta')
def step_impl(context):
    calc = calculadora()
    context.resultado = calc.restar(context.num1, context.num2)

