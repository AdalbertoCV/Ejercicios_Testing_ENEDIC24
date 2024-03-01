# Funcionamiento para transformar numero a letra desde 0 a mil millones
# Adalberto Cerrillo Vázquez

class numeros_a_letras():
    def convertir(self, num):
        # para las unidades
        unidades = ["", "uno", "dos", "tres", "cuatro",
                    "cinco", "seis", "siete", "ocho", "nueve"]
        # para las decenas
        decenas = ["", "diez", "veinte", "treinta", "cuarenta",
                   "cincuenta", "sesenta", "setenta", "ochenta", 
                   "noventa"]
        # para las centenas
        centenas = ["", "ciento", "doscientos", "trescientos",
                    "cuatrocientos", "quinientos", "seiscientos",
                    "setesientos", "ochocientos", "novecientos"]
        # especiales
        especiales = ["diez", "once", "doce", "trece", "catorce",
                      "quince", "dieciseis", "diecisiete", "dieciocho", 
                      "diecinueve"]

        # para el cero
        if num <= 0:
            return convertirCero(num)
        # para las unidades
        elif 0 < num <= 9:
            return unidades[num]
        # para los casos especiales
        elif 10 <= num <= 19:
            return especiales[num-10]
        # para las decenas
        elif 20 <= num <= 99:
            return decenas[num // 10] + (" y " + \
            unidades[num % 10] if num % 10 != 0 else "")
        # para las centenas
        elif 100 <= num <= 999:
            return convertirCentenas(self, num, centenas)
        # para los miles
        elif 1000 <= num <= 999999:
            return convertirMiles(self, num)
        # para los millones
        elif 1000000 <= num <= 1000000000:
            return convertirMillones(self, num)
        # si se introducen numeros mayores a mil millones
        else:
            return 'No se permiten numeros mayores a mil millones.'


def convertirCero(num):
    if num == 0:
        return "cero"
    else:
        return 'Ingrese numeros positivos'


def convertirCentenas(self, num, centenas):
    if num == 100:
        return 'cien'
    return centenas[num // 100] + (" " + \
    self.convertir(num % 100) if num % 100 != 0 else "")


def convertirMiles(self, num):
    if num == 1000:
        return 'mil'
    if num == 100000:
        return 'cien mil'
    if num < 1999:
        return 'mil' + (" " + \
        self.convertir(num % 1000) if num % 1000 != 0 else "")
    return self.convertir(num // 1000) + " mil" + \
    (" " + self.convertir(num % 1000) if num % 1000 != 0 else "")


def convertirMillones(self, num):
    if num == 1000000:
        return 'un millón'
    if num < 1999999:
        return "un millón" + (" " + \
        self.convertir(num % 1000000) if num % 1000000 != 0 else "")
    return self.convertir(num // 1000000) + " millones" + \
    (" " + self.convertir(num % 1000000) if num % 1000000 != 0 else "")
