from django.shortcuts import render
from .models import Candidato, Partido, Votacion
from django.utils import timezone

def lista_candidatos(request):
    # extraemos los candidatos de la base de datos
    candidatos = Candidato.objects.all()
    # los enviamos en el contexto
    context = {'candidatos': candidatos}
    # redireccionamos a la lista de candidatos
    return render(request, 'votaciones.html', context)

def votar(request, id):
    # extraemos el candidato segun su id enviada
    candidato_a_votar = Candidato.objects.get(id = id)
    # creamos una nueva votacion
    nueva_votacion = Votacion(candidato=candidato_a_votar, fecha_hora=timezone.now())
    nueva_votacion.save()

    # Obtener todos los candidatos
    candidatos = Candidato.objects.all()

    # Crear un diccionario para almacenar el número de votaciones por candidato
    resultados = {}
    for candidato in candidatos:
        # Contar el número de votaciones para este candidato
        num_votaciones = Votacion.objects.filter(candidato=candidato).count()
        resultados[candidato] = num_votaciones

    # Obtener al candidato con más votos
    max_votos = max(resultados.values())
    candidatos_mas_votados = [candidato for candidato, votos in resultados.items() if votos == max_votos]

    if len(candidatos_mas_votados) > 1:
        candidato_mas_votado = "Empate momentáneo"
    else:
        candidato_mas_votado = candidatos_mas_votados[0]

    # Renderizar la página de resultados y pasar el diccionario de resultados al contexto de la plantilla
    return render(request, 'resultados.html', {'resultados': resultados, 'ganador': candidato_mas_votado,'candidato_votado':candidato_a_votar})

