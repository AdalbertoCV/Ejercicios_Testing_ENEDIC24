from django.test import TestCase
from candidatos.models import Partido, Candidato

class TestViewsCandidatos(TestCase):
    def test_votaciones_estatus_200(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_page_not_found_404(self):
        response = self.client.get('/asd')
        self.assertEqual(404, response.status_code)

    def test_votaciones_mensaje(self):
        response = self.client.get('/')
        self.assertIn(b'Partido', response.content)

    def test_votaciones_candidato(self):
        response = self.client.get('/')
        self.assertIn(b'Candidato', response.content)
    
    def test_votar_candidato_1(self):
        partido = Partido.objects.create(nombre = 'PRD', descripcion = 'Partido reforma democrática')
        candidato = Candidato.objects.create(nombre = 'Juan', apellido_paterno = 'López' , apellido_materno = 'Sánchez', partido = partido)
        response = self.client.get('/Candidatos/Votar/1')
        self.assertIn(b'Gracias por votar por: Juan', response.content)

    def test_visualizar_ganador(self):
        partido = Partido.objects.create(nombre = 'PRD', descripcion = 'Partido reforma democrática')
        candidato = Candidato.objects.create(nombre = 'Juan', apellido_paterno = 'López' , apellido_materno = 'Sánchez', partido = partido)
        response = self.client.get('/Candidatos/Votar/1')
        self.assertIn(b'El ganador es: Juan', response.content)