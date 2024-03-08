Característica: Como usuario de la calculadora
                deseo utilizar la función de raiz
                para sacar la raiz n de un numero hacer cálculos precisos

Escenario: Calcular raíz 8 de 3
    Dado que el usuario ingresa los numeros "8" y "3"
    Cuando realizo la raiz
    Entonces puede ver el resultado igual a "2"

Escenario: Calcular raíz una cadena "hola" de 2
    Dado  que el usuario ingresa el caractér "hola" y el número "2"
    Cuando realizo la raiz
    Entonces puede ver el mensaje: "No se permiten cadenas de texto"

Escenario: Calcular raíz una lista vacía de 2
    Dado que el usuario ingresa la lista "[]" y el número "2"
    Cuando realizo la raiz
    Entonces puede ver el mensaje: "No se permiten listas"

Escenario: Calcular raíz 12.4 de 2
    Dado que el usuario ingresa el entero "2" y el decimal "12.4"
    Cuando realizo la raiz
    Entonces puede ver el mensaje: "No se permiten decimales"


Escenario: Calcular raíz True de 3
    Dado que el usuario ingresa el booleano "True" y el número "3"
    Cuando realizo la raiz
    Entonces puede ver el mensaje: "No se permiten booleanos"