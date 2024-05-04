Característica: Voto por candidato
    Como usuario de la plataforma de votantes
    quiero votar por un candidato
    para elegir a mi presidente.

    Escenario: Votar por Jorge Álvarez Maynez
        Dado que ingreso a la url "http://localhost:8000/"
        Cuando doy clic en el boton de votar a "Jorge Álvarez Máynez"
        Entonces puedo ver el mensaje "Gracias por votar por: Jorge Álvarez Máynez" en pantalla

    Escenario: Votar por Xóchitl Gálvez Ruiz
        Dado que ingreso a la url "http://localhost:8000/"
        Cuando doy clic en el boton de votar a "Xóchitl Gálvez Ruiz"
        Entonces puedo ver el mensaje "Gracias por votar por: Xóchitl Gálvez Ruiz" en pantalla

    Escenario: Ver ganador
        Dado que ingreso a la url "http://localhost:8000/"
        Cuando doy clic en el boton de votar a "Xóchitl Gálvez Ruiz"
        Entonces puedo ver el mensaje con el ganador en pantalla