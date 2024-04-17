Característica: Registro de candidato
    Como administrador del sistema de votación
    quiero registrar un candidato
    para que sea votado

    Escenario: Registrar a Jorge Maynez
        Dado que ingreso a la url "http://localhost:8000/admin/login/?next=/admin/"
        Y escribo mi usuario "adal" y mi contraseña "adal1234@"
        Y presiono el botón de Log In
        Y doy click en el enlace Candidatos
        Y luego click en el boton Agregar Candidato
        Y escribo el nombre de "Jorge Maynez"
        Y selecciono el partido "Naranja"
        Cuando presiono el botón de Guardar
        Entonces puedo ver el candidato "Jorge Maynez" en la lista de candidatos
