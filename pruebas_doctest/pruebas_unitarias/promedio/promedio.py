#Funcionalidad para calcular un promedio.
# Adalberto Cerrillo Vázquez - 8A
class promedio():
    def calcular(self,p1,p2,p3):
        try:
            # Verificamos que no se haya enviado ningun valor nulo.
            if p1 is not None and p2 is not None and p3 is not None:
                #Verificamos que se hayan enviado 3 numeros
                if (isinstance(p1,int) or isinstance(p1,float)) and (isinstance(p2,int)or isinstance(p2,float)) and (isinstance(p3,int)or isinstance(p3,float)):
                    #Verificamos que no se haya enviado algun booleano (recordemos que en forma un booleano es un entero)
                    if isinstance(p1,bool) or isinstance(p2, bool) or isinstance(p3,bool):
                        return 'No se aceptan booleanos'
                    #verificamos que no se hayan enviado numeros negativos
                    if p1>=0 and p2>=0 and p3>=0:
                        #Calculamos que el valor de cada calificacion no exceda el maximo (10)
                        if p1<=10 and p2<=10 and p3<=10:
                            #Calculamos el promedio de las 3 calificaciones
                            res = (p1+p2+p3)/3
                            return round(res,2)
                        else:
                            return 'La calificación máxima es 10'
                    # Redondeamos el resultado a 2 decimales
                    else:
                        return 'No se aceptan numeros negativos'
                # Si se han enviado cadenas de texto.
                elif isinstance(p1,str) or isinstance(p2,str) or isinstance(p3,str):
                    return 'No se aceptan cadenas de texto'
                # Si se han enviado listas.
                elif isinstance(p1,list) or isinstance(p2, list) or isinstance(p3,list):
                    return 'No se aceptan listas'
                # Si se envia cualquier otro elemento como tuplas, diccionarios, etc.
                else:
                    return 'Elementos no válidos para el cálculo'
            else:
                return 'No se aceptan valores nulos'
        except:
            return 'Error'