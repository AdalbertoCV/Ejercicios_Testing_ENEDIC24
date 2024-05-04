Característica: Registro de candidato
    Como administrador del sistema de votación
    quiero registrar un candidato
    para que sea votado

    Escenario: Registrar a Xóchitl Gálvez Ruiz
        Dado que ingreso a la url "http://localhost:8000/admin/login/?next=/admin/"
        Y escribo mi usuario "adal" y mi contraseña "adal1234@"
        Y presiono el botón de Log In
        Y doy click en el enlace Candidatos
        Y luego click en el boton Agregar Candidato
        Y escribo el nombre de "Xóchitl"
        Y escribo el apellido paterno "Gálvez"
        Y escribo el apellido materno "Ruiz"
        Y selecciono la imagen de candidato "C:\Users\booco\Documents\Testing\Ejercicios_Testing_ENEDIC24\proyectos_django\app\votantes\pruebas_aceptacion\imagenes_pruebas\img.jpg"
        Y selecciono el partido "PAN"
        Cuando presiono el botón de Guardar
        Entonces puedo ver el candidato "Xóchitl Gálvez Ruiz" en la lista de candidatos
