Característica: Como usuario de la calculadora
                deseo utilizar la función de sumar
                para sumar dos numeros y hacer cálculos precisos

    Escenario: Sumar 2 más 2
        Dado que el usuario ingresa los numeros "2" y "2"
        Cuando realizo el cálculos
        Entonces puede ver el resultado igual a "4"

    Escenario: Sumar 2 más 3
        Dado que el usuario ingresa los numeros "2" y "3"
        Cuando realizo el cálculos
        Entonces puede ver el resultado igual a "5"

    Escenario: Sumar x más 6
        Dado que el usuario ingresa el caractér "x" y el número "6"
        Cuando realizo el cálculos
        Entonces puede ver el mensaje: "No se permiten cadenas de texto"

    Escenario: Sumar True más 3
        Dado que el usuario ingresa el booleano "True" y el número "3"
        Cuando realizo el cálculos
        Entonces puede ver el mensaje: "No se permiten booleanos"

    Escenario: Sumar -2 más -3
        Dado que el usuario ingresa los numeros "-2" y "-3"
        Cuando realizo el cálculos
        Entonces puede ver el mensaje: "Sólo numeros positivos"

    Escenario: Sumar 1 más 9.5
        Dado que el usuario ingresa el entero "1" y el decimal "9.5"
        Cuando realizo el cálculos
        Entonces puede ver el mensaje: "Sólo numeros enteros"


    Escenario: Sumar lista más 9
        Dado que el usuario ingresa la lista "[]" y el número "9"
        Cuando realizo el cálculos
        Entonces puede ver el mensaje: "Sólo numeros, no listas"