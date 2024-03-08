Característica: Como usuario de la calculadora
                deseo utilizar la función de multiplicar
                para multiplicar dos numeros y hacer cálculos precisos

Escenario: Multiplicar 8 por 2
    Dado que el usuario ingresa los numeros "8" y "2"
    Cuando realizo la multiplicación
    Entonces puede ver el resultado igual a "16"

Escenario: Multiplicar -3 por 2
    Dado que el usuario ingresa los numeros "-3" y "2"
    Cuando realizo la multiplicación
    Entonces puede ver el resultado igual a "-6"

Escenario: Multiplicar una cadena "hola" por 2
    Dado  que el usuario ingresa el caractér "hola" y el número "2"
    Cuando realizo la multiplicación
    Entonces puede ver el mensaje: "No se permiten cadenas de texto"

Escenario: Multiplicar una lista vacía por 2
    Dado que el usuario ingresa la lista "[]" y el número "2"
    Cuando realizo la multiplicación
    Entonces puede ver el mensaje: "No se permiten listas"

Escenario: Multiplicar 12.4 por 2
    Dado que el usuario ingresa el entero "2" y el decimal "12.4"
    Cuando realizo la multiplicación
    Entonces puede ver el mensaje: "No se permiten decimales"


Escenario: Multiplicar True por 3
    Dado que el usuario ingresa el booleano "True" y el número "3"
    Cuando realizo la multiplicación
    Entonces puede ver el mensaje: "No se permiten booleanos"