Característica: Registro de partido
    Como administrador del sistema de votación
    quiero registrar un partido
    para que pueda registrar candidatos

    Escenario: Registrar al PAN
        Dado que ingreso a la url "http://localhost:8000/admin/login/?next=/admin/"
        Y escribo mi usuario "adal" y mi contraseña "adal1234@"
        Y presiono el botón de Log In
        Y doy click en el enlace Partidos
        Y luego click en el boton Agregar Partido
        Y escribo el nombre de "PAN"
        Y escribo la descripción "Partido Acción Nacional"
        Y selecciono la imagen "C:\Users\booco\Documents\Testing\Ejercicios_Testing_ENEDIC24\proyectos_django\app\votantes\pruebas_aceptacion\imagenes_pruebas\pan.png"
        Cuando presiono el botón de Guardar
        Entonces puedo ver el partido "PAN" en la lista de partidos
