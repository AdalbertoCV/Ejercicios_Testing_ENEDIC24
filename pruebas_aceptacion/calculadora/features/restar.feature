Característica: Como usuario de la calculadora
                deseo utilizar la función de restar
                para restar dos numeros y hacer cálculos precisos

Escenario: Restar 8 menos 2
    Dado que el usuario ingresa los numeros "8" y "2"
    Cuando realizo la resta
    Entonces puede ver el resultado igual a "6"

Escenario: Restar -3 menos 2
    Dado que el usuario ingresa los numeros "-3" y "2"
    Cuando realizo la resta
    Entonces puede ver el resultado igual a "-5"

Escenario: Restar una cadena "hola" menos 2
    Dado  que el usuario ingresa el caractér "hola" y el número "2"
    Cuando realizo la resta
    Entonces puede ver el mensaje: "No se permiten cadenas de texto"

Escenario: Restar una lista vacía menos 2
    Dado que el usuario ingresa la lista "[]" y el número "2"
    Cuando realizo la resta
    Entonces puede ver el mensaje: "No se permiten listas"

Escenario: Restar 12.4 menos 2
    Dado que el usuario ingresa el entero "2" y el decimal "12.4"
    Cuando realizo la resta
    Entonces puede ver el mensaje: "No se permiten decimales"


Escenario: Restar True menos 3
    Dado que el usuario ingresa el booleano "True" y el número "3"
    Cuando realizo la resta
    Entonces puede ver el mensaje: "No se permiten booleanos"