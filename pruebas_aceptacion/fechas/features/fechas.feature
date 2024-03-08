Característica: Como usuario del convertidor de fechas
                deseo utilizar la función de convertir
                para convertir la fecha a texto plano

  Escenario: fecha: 10/1/2000
    Dado que el usuario ingresa la fecha "10/1/2000"
    Cuando convierto la fecha
    Entonces obtengo la cadena "diez de enero año dos mil"

  Escenario: febrero_mil_ochocientos
    Dado que el usuario ingresa la fecha "15/2/2000"
    Cuando convierto la fecha
    Entonces obtengo la cadena "quince de febrero año dos mil"

  Escenario: marzo_dos_mil_doce
    Dado que el usuario ingresa la fecha "11/3/2012"
    Cuando convierto la fecha
    Entonces obtengo la cadena "once de marzo año dos mil doce"

  Escenario: abril_mil_novescientos_noventaynueve
    Dado que el usuario ingresa la fecha "21/4/2100"
    Cuando convierto la fecha
    Entonces obtengo la cadena "veinte y uno de abril año dos mil cien"

  Escenario: mayo_mil_novescientos_noventayocho
    Dado que el usuario ingresa la fecha "19/5/2000"
    Cuando convierto la fecha
    Entonces obtengo la cadena "diecinueve de mayo año dos mil"

  Escenario: junio_mil_cuarenta
    Dado que el usuario ingresa la fecha "19/6/2040"
    Cuando convierto la fecha
    Entonces obtengo la cadena "diecinueve de junio año dos mil cuarenta"

  Escenario: julio_dosmil_cuarenta
    Dado que el usuario ingresa la fecha "20/7/2040"
    Cuando convierto la fecha
    Entonces obtengo la cadena "veinte de julio año dos mil cuarenta"

  Escenario: agosto_dosmil_cuarenta
    Dado que el usuario ingresa la fecha "20/8/2040"
    Cuando convierto la fecha
    Entonces obtengo la cadena "veinte de agosto año dos mil cuarenta"

  Escenario: septiembre_dosmil_catorce
    Dado que el usuario ingresa la fecha "1/9/2014"
    Cuando convierto la fecha
    Entonces obtengo la cadena "uno de septiembre año dos mil catorce"

  Escenario: octubre_dosmil_catorce
    Dado que el usuario ingresa la fecha "2/10/2014"
    Cuando convierto la fecha
    Entonces obtengo la cadena "dos de octubre año dos mil catorce"

  Escenario: noviembre_dosmil_dos
    Dado que el usuario ingresa la fecha "2/11/2002"
    Cuando convierto la fecha
    Entonces obtengo la cadena "dos de noviembre año dos mil dos"

  Escenario: diciembre_dosmil_uno
    Dado que el usuario ingresa la fecha "31/12/2001"
    Cuando convierto la fecha
    Entonces obtengo la cadena "treinta y uno de diciembre año dos mil uno"

  Escenario: limite_dia
    Dado que el usuario ingresa la fecha "33/11/1000"
    Cuando convierto la fecha
    Entonces obtengo la cadena "día fuera de rango"

  Escenario: limite_mes
    Dado que el usuario ingresa la fecha "30/13/1000"
    Cuando convierto la fecha
    Entonces obtengo la cadena "mes fuera de rango"

  Escenario: limite_anio
    Dado que el usuario ingresa la fecha "30/12/1000000000000"
    Cuando convierto la fecha
    Entonces obtengo la cadena "año fuera de rango"

  Escenario: formato_incorrecto
    Dado que el usuario ingresa la fecha "30/13/hola"
    Cuando convierto la fecha
    Entonces obtengo la cadena "formato de fecha incorrecto"
    
