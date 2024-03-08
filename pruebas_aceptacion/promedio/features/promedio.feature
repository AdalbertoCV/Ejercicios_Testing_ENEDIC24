Característica: Como usuario de la calculadora de promedio
                deseo utilizar la función de calcular el promedio
                para calcular el promedio de mis tres calificaciones parciales

    Escenario: promedio de 10, 10 y 10
        Dado que el usuario ingresa las calificaciones "10", "10" y "10"
        Cuando calculo el promedio
        Entonces puede ver el resultado igual a "10.0"

    Escenario: promedio de 9, 9.5 y 7
        Dado que el usuario ingresa las calificaciones "9", "9.5" y "7"
        Cuando calculo el promedio
        Entonces puede ver el resultado igual a "8.5"

    Escenario: promedio de 5, 6 y 6
        Dado que el usuario ingresa las calificaciones "5", "6" y "6"
        Cuando calculo el promedio
        Entonces puede ver el resultado igual a "5.67"

    Escenario: promedio de hola, 9.5 y 7
        Dado que el usuario ingresa las calificaciones "9", "9.5" y la cadena "hola"
        Cuando calculo el promedio
        Entonces puede ver el mensaje: "No se aceptan cadenas de texto"

    Escenario: promedio de True, 9.5 y 7
        Dado que el usuario ingresa las calificaciones "9", "9.5" y el booleano "True"
        Cuando calculo el promedio
        Entonces puede ver el mensaje: "No se aceptan booleanos"

    Escenario: promedio de 9, 9.5 y - 7
        Dado que el usuario ingresa las calificaciones "9", "9.5" y "-7"
        Cuando calculo el promedio
        Entonces puede ver el mensaje: "No se aceptan numeros negativos"

    Escenario: promedio de 9, 9.5 y 22
        Dado que el usuario ingresa las calificaciones "9", "9.5" y "22"
        Cuando calculo el promedio
        Entonces puede ver el mensaje: "La calificación máxima es 10"

    Escenario: promedio de 9, 9.5 y None
        Dado que el usuario ingresa las calificaciones "9", "9.5" y nulo
        Cuando calculo el promedio
        Entonces puede ver el mensaje: "No se aceptan valores nulos"
    