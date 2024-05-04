Característica: Inicio de sesión
    Como usuario del sistema de votantes
    quiero iniciar sesión 
    para realizar mis actividades.

    Escenario: Credenciales validas
        Dado que ingreso a la url "http://localhost:8000/admin/login/?next=/admin/"
        Y escribo mi usuario "adal" y mi contraseña "adal1234@"
        Cuando presiono el botón de Log In
        Entonces puedo ver el usuario "ADAL" en la barra principal

    Escenario: Credenciales Invalidas
        Dado que ingreso a la url "http://localhost:8000/admin/login/?next=/admin/"
        Y escribo mi usuario "usuario-random" y mi contraseña "Admin1234@"
        Cuando presiono el botón de Log In
        Entonces puedo ver el error "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." en pantalla