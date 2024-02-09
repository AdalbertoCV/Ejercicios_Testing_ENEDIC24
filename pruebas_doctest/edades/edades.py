#Funcionalidad para enviar mensajes segun la edad proporcionada
#Adalberto Cerrillo Vázquez - 8A
class edades():
    def mensaje(self,x):
        #Verificamos que se trate de un numero entero
        if isinstance(x,int):
            #Verificamos que no se haya enviado un booleano (Recordemos que en escencia un booleano se trabaja como un entero)
            if not isinstance(x,bool):
                #Rango para mensaje: No existes
                if x<0:
                    return 'No existes'
                #Rango para mensaje: Eres niño
                elif x>=0 and x<13:
                    return 'Eres niño'
                #Rango para mensaje: Eres adolescente
                elif x>=13 and x<18:
                    return 'Eres adolescente'
                #Rango para mensaje: Eres adulto
                elif x>=18 and x<65:
                    return 'Eres adulto'
                #Rango para mensaje: Eres adulto mayor
                elif x>=65 and x<120:
                    return 'Eres adulto mayor'
                # Si es mayor a 120: Eres Mumm-Ra
                else:
                    return 'Eres Mumm-Ra'
            else:
                return 'No se permiten booleanos'
        # Si se envió un numero decimal
        elif isinstance(x,float):
            return 'Solo numeros enteros'
        # Si se envió una cadena de texto
        elif isinstance(x, str):
            return 'No se permiten cadenas'
        # Si se envió una lista
        elif isinstance(x,list):
            return 'No se permiten listas'
        # Si se envió algun otro formato no numerico.
        else:
            return 'Elemento proporcionado no válido'
        