Característica: Como usuario de la calculadora
                deseo utilizar la función de dividir
                para dividir dos numeros y hacer cálculos precisos

Escenario: Dividir 8 entre 2
    Dado que el usuario ingresa los numeros "8" y "2"
    Cuando realizo la división
    Entonces puede ver el resultado igual a "4"

Escenario: Dividir -3 entre 2
    Dado que el usuario ingresa los numeros "-10" y "2"
    Cuando realizo la división
    Entonces puede ver el resultado igual a "-5"

Escenario: Dividir 3 entre 0
    Dado que el usuario ingresa los numeros "3" y "0"
    Cuando realizo la división
    Entonces puede ver el mensaje: "No se puede dividir entre cero"

Escenario: Dividir una cadena "hola" entre 2
    Dado  que el usuario ingresa el caractér "hola" y el número "2"
    Cuando realizo la división
    Entonces puede ver el mensaje: "No se permiten cadenas de texto"

Escenario: Dividir una lista vacía entre 2
    Dado que el usuario ingresa la lista "[]" y el número "2"
    Cuando realizo la división
    Entonces puede ver el mensaje: "No se permiten listas"

Escenario: Dividir 12.4 entre 2
    Dado que el usuario ingresa el entero "2" y el decimal "12.4"
    Cuando realizo la división
    Entonces puede ver el mensaje: "No se permiten decimales"


Escenario: Dividir True entre 3
    Dado que el usuario ingresa el booleano "True" y el número "3"
    Cuando realizo la división
    Entonces puede ver el mensaje: "No se permiten booleanos"