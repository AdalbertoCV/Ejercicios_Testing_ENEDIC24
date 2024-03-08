Característica: Como usuario de la calculadora
                deseo utilizar la función de potencia
                para sacar la potencia n de un numero hacer cálculos precisos

Escenario: Calcular potencia 8 de 3
    Dado que el usuario ingresa los numeros "8" y "2"
    Cuando realizo la potencia
    Entonces puede ver el resultado igual a "64"

Escenario: Calcular potencia 2 de 3
    Dado que el usuario ingresa los numeros "2" y "3"
    Cuando realizo la potencia
    Entonces puede ver el resultado igual a "8"

Escenario: Calcular potencia una cadena "hola" de 2
    Dado  que el usuario ingresa el caractér "hola" y el número "2"
    Cuando realizo la potencia
    Entonces puede ver el mensaje: "No se permiten cadenas de texto"

Escenario: Calcular potencia una lista vacía de 2
    Dado que el usuario ingresa la lista "[]" y el número "2"
    Cuando realizo la potencia
    Entonces puede ver el mensaje: "No se permiten listas"

Escenario: Calcular potencia 12.4 de 2
    Dado que el usuario ingresa el entero "2" y el decimal "12.4"
    Cuando realizo la potencia
    Entonces puede ver el mensaje: "No se permiten decimales"


Escenario: Calcular potencia True de 3
    Dado que el usuario ingresa el booleano "True" y el número "3"
    Cuando realizo la potencia
    Entonces puede ver el mensaje: "No se permiten booleanos"