# importamos la funcionalidad para convertir
# numeros a texto
from numeros_a_letras import numeros_a_letras

# funcionalidad para convertir fechas a texto


class fechas:
    def convertir(self, fecha):
        # instancia de conversor a letras
        conv = numeros_a_letras()
        # lista que guarda los nombres de los meses
        meses = ['', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                 'julio', 'agosto', 'septiembre', 'octubre',
                 'noviembre', 'diciembre']
        # inicializamos una lista para separar la fecha
        fecha_separada = fecha.split("/")
        # variable para almacenar el día
        try:
            dia = int(fecha_separada[0])
            # variable para almacenar el mes
            mes = int(fecha_separada[1])
            # variable para almacenar el año
            anio = int(fecha_separada[2])
        except ValueError:
            return 'formato de fecha incorrecto'

        fecha_en_rango = self.validarRango(dia, mes, anio)
        # si la fecha esta dentro del rango
        if fecha_en_rango == True:
            # calculamos el dia en letra
            dia_letra = conv.convertir(dia)
            # calculamos el año en letra
            anio_letra = conv.convertir(anio)
            resultado = dia_letra + " de "\
                + meses[mes] + ' año ' + anio_letra
            return resultado
        else:
            return fecha_en_rango

    # funcion para validar que la fecha este en rango
    def validarRango(self, dia, mes, anio):
        if 0 < dia < 32:
            if 0 < mes < 13:
                if 0 < anio < 1000000000:
                    return True
                else:
                    return 'año fuera de rango'
            else:
                return 'mes fuera de rango'
        else:
            return 'día fuera de rango'
