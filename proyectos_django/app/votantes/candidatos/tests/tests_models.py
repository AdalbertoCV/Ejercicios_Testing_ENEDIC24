from django.test import TestCase
from candidatos.models import Partido, Candidato

# prueba de humo para verificar que todo funcione correctamente
class TestSmoke(TestCase):
    def test_smoke(self):
        self.assertEqual(2,2)

    def test_crear_partido(self):
        partido = Partido.objects.create(nombre = 'PRD', descripcion = 'Partido reforma democrática')
        partido = Partido.objects.create(nombre = 'MC', descripcion = 'Movimiento Ciudadano')
        self.assertEqual(2, Partido.objects.count())

    def test_crear_partido_nombre(self):
        partido = Partido.objects.create(nombre = 'PRD', descripcion = 'Partido reforma democrática')
        self.assertEqual('PRD', partido.nombre)

    def test_crear_candidato(self):
        partido = Partido.objects.create(nombre = 'PRD', descripcion = 'Partido reforma democrática')
        candidato = Candidato.objects.create(nombre = 'Juan', apellido_paterno = 'López' , apellido_materno = 'Sánchez', partido = partido)
        self.assertEqual('Juan', candidato.nombre)

    def test_representacion_en_string_de_partido(self):
        partido = Partido.objects.create(nombre = 'PRD', descripcion = 'Partido reforma democrática')
        self.assertEqual('PRD', str(partido))

