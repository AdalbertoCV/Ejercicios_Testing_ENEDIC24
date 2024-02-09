# Funcionalidad para calcular el pago de horas extra a un trabajador
""" Ejercicio 29: Determinar la cantidad de dinero que recibirá un trabajador de las horas extra, sabiendo que cuando las horas
trabajadas exceden las 40, el resto es horas extras y se pagan al doble de una normal, y si exceden de 8 horas extra, 
el resto se paga al triple"""

class horas_extra():
    def calcular(self, horas, costo):
        # Verificamos que se hayan enviado numeros
        if (isinstance(horas,int) or isinstance(horas,float)) and (isinstance(costo,int) or isinstance(costo,float)):
            #Verificamos que no se haya enviado booleanos
            if not isinstance(horas,bool) and not isinstance(costo,bool):
                #Verificamos que las horas sean un entero
                if isinstance(horas,int):
                    #Verificamos que las horas sean igual o menores a 40
                    if horas<=40:
                        #Calculamos el total de horas normales
                        return horas * costo
                    #Verificamos que las horas sean menores a 48
                    elif horas>40 and horas<=48:
                        # Aislamos las horas dobles de las normales
                        dobles = horas - 40
                        normales = horas - dobles
                        return (normales * costo) + (dobles * (costo*2))
                    # Si se exceden las 8 horas extra, entonces son triples
                    else:
                        #Asilamos las horas dobles, de las triples y las normales
                        triples = horas-48
                        dobles = 8
                        normales = 40
                        return (normales * costo) + (dobles * (costo*2)) +  (triples * (costo*3))
                else:
                    return 'No se aceptan decimales'
            else:
                return 'No se aceptan booleanos'
        else:
            # Verificamos que nos se hayan enviado cadenas de texto
            if isinstance(horas, str) or isinstance(costo,str):
                return 'No se aceptan cadenas'
            # Si se envio cualquier otro formato no válido
            else:
                return 'Formato no válido'