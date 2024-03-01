# Calculadora para la clase de testing 2024
# Adalberto Cerrillo Vázquez - 8A
class calculadora():
    # Funcion de suma de dos numeros enteros
    def sumar(self, num1, num2):
        # Verificamos que los numeros enviados no sean una lista
        if not isinstance(num1, list) and not isinstance(num2, list):
            # Verificamos que se trate unicamente de numero positivos
            if (num1 > 0 and num2 > 0):
                # Verificamos que los numeros sean enteros
                if isinstance(num1, int) and isinstance(num2, int):
                    if isinstance(num1, bool) or isinstance(num2, bool):
                        return 'No se permiten booleanos'
                    # Pasado todas las condiciones, enviamos la suma.
                    return num1 + num2
                else:
                    # Si los numero no son enteros, enviamos el mensaje
                    return 'Sólo numeros enteros'
            else:
                # Si los numeros son negativos, enviamos el mensaje
                return 'Sólo numeros positivos'
        else:
            # Si se envia una listam se envia el mensaje
            return 'Sólo numeros, no listas'

    # Funcion para restar dos numeros
    def restar(self, num1, num2):
        # Verificamos que se trata de dos numeros enteros
        if isinstance(num1, int) and isinstance(num2, int):
            if isinstance(num1, bool) or isinstance(num2, bool):
                return 'No se permiten booleanos'
            # Si es asi, regresamos la resta.
            return num1 - num2
        else:
            # Verificamos que no se envien decimales
            if isinstance(num1, float) or isinstance(num2, float):
                # Si es asi, regresamos un mensaje
                return 'No se permiten decimales'
            # Verificamos que no se envien cadenas de texto
            elif isinstance(num1, str) or isinstance(num2, str):
                # Si es asi, regresamos un mensaje
                return 'No se permiten cadenas de texto'
            # Verificamos que no se envien listas
            elif isinstance(num1, list) or isinstance(num2, list):
                # Si es asi, regresamos un mensaje
                return 'No se permiten listas'
            else:
                return 'Elemento no valido para la operacion'

    # Funcion para multiplicar dos numeros enteros.
    def multiplicar(self, num1, num2):
        # verificamos que se envien dos numeros enteros
        if isinstance(num1, int) and isinstance(num2, int):
            if isinstance(num1, bool) or isinstance(num2, bool):
                return 'No se permiten booleanos'
            # Si es asi, retornamos la operacion
            return num1 * num2
        else:
            # Verificamos que no se envien decimales
            if isinstance(num1, float) or isinstance(num2, float):
                # Si es asi, regresamos un mensaje
                return 'No se permiten decimales'
            # Verificamos que no se envien cadenas de texto
            elif isinstance(num1, str) or isinstance(num2, str):
                # Si es asi, regresamos un mensaje
                return 'No se permiten cadenas de texto'
            # Verificamos que no se envien listas
            elif isinstance(num1, list) or isinstance(num2, list):
                # Si es asi, regresamos un mensaje
                return 'No se permiten listas'
            else:
                return 'Elemento no valido para la operacion'

    # Funcion para dividir dos numeros enteros
    def dividir(self, num1, num2):
        # Verificamos que se envien numeros enteros
        if isinstance(num1, int) and isinstance(num2, int):
            if isinstance(num1, bool) or isinstance(num2, bool):
                return 'No se permiten booleanos'
            # Verificamos que el divisor no sea un cero
            # ya que provocaría un error matemático
            if num2 > 0:
                # Retornamos el resultado de la operación.
                resultado = num1 / num2
                # Si el resultado es entero
                if resultado.is_integer():
                    # Retornamos el resultado
                    return int(resultado)
                else:
                    # Si no es un entero, redondeamos a dos decimales
                    return round(resultado, 2)
            else:
                return 'No se puede dividir entre cero'

        else:
            # Verificamos que no se envien decimales
            if isinstance(num1, float) or isinstance(num2, float):
                # Si es asi, regresamos un mensaje
                return 'No se permiten decimales'
            # Verificamos que no se envien cadenas de texto
            elif isinstance(num1, str) or isinstance(num2, str):
                # Si es asi, regresamos un mensaje
                return 'No se permiten cadenas de texto'
            # Verificamos que no se envíen listas
            elif isinstance(num1, list) or isinstance(num2, list):
                # Si es asi, regresamos un mensaje
                return 'No se permiten listas'
            else:
                return 'Elemento no valido para la operacion'

    # Funcion para calcular una raíz
    def sqrt(self, num1, num2):
        # Verificamos que se hayan enviado dos numeros enteros.
        if isinstance(num1, int) and isinstance(num2, int):
            if isinstance(num1, bool) or isinstance(num2, bool):
                return 'No se permiten booleanos'
            # Verificamos que los numeros sean positivos
            if num1 > 0 and num2 > 0:
                # Calculamos el resultado de la operación
                resultado = num1 ** (1/num2)
                # Si el resultado es entero
                if resultado.is_integer():
                    # Devolvemos el resultado
                    return int(resultado)
                else:
                    # Si no lo es, redondeamos el resultado a dos decimales.
                    return round(resultado, 2)
            else:
                # Si se envian numeros negativos, se indica con un mensaje
                return 'No se permiten raíces negativas'
        else:
            # Verificamos que no se envien numeros decimales
            if isinstance(num1, float) or isinstance(num2, float):
                # Si es asi, regresamos un mensaje
                return 'No se permiten decimales'
            # Verificamos que no se envien cadenas de texto
            elif isinstance(num1, str) or isinstance(num2, str):
                # Si es asi, regresamos un mensaje
                return 'No se permiten cadenas de texto'
            # Verificamos que no se envien listas.
            elif isinstance(num1, list) or isinstance(num2, list):
                # Si es asi, regresamos un mensaje
                return 'No se permiten listas'
            else:
                return 'Elemento no valido para la operacion'

    # Funcion para elevar un numero a una potencia.
    def potencia(self, num1, num2):
        # Verificamos que se hayan enviado dos numeros enteros.
        if isinstance(num1, int) and isinstance(num2, int):
            if isinstance(num1, bool) or isinstance(num2, bool):
                return 'No se permiten booleanos'
            # Verificamos que los numeros sean positivos
            if num1 > 0 and num2 > 0:
                # inicializamos la variable para guardar el resultado
                resultado = num1
                # Iteramos para multipicar el numero
                # la cantidad de veces indicadas.
                for i in range(num2-1):
                    resultado = resultado * num1
                    # Retornamos el resultado
                return resultado
            else:
                # Si se envian numeros negativos
                # se indica con un mensaje
                return 'No se permiten numeros negativos'
        else:
            # Verificamos que no se envien numeros decimales
            if isinstance(num1, float) or isinstance(num2, float):
                # Si es asi, regresamos un mensaje
                return 'No se permiten decimales'
            # Verificamos que no se envien cadenas de texto
            elif isinstance(num1, str) or isinstance(num2, str):
                # Si es asi, regresamos un mensaje
                return 'No se permiten cadenas de texto'
            # Verificamos que no se envien listas.
            elif isinstance(num1, list) or isinstance(num2, list):
                # Si es asi, regresamos un mensaje
                return 'No se permiten listas'
            else:
                # Si se envia cualquier otro elemento
                # que no sea válido para la operación.
                return 'Elemento no valido para la operacion'
