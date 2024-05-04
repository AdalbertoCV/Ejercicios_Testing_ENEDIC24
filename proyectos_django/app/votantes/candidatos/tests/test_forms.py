from django.test import TestCase
from .models import Partido, Candidato
from .forms import PartidoForm, CandidatoForm

class PartidoFormTest(TestCase):
    def test_partido_form_valid(self):
        form_data = {'nombre': 'Partido A', 'descripcion': 'Descripción del Partido A'}
        form = PartidoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_partido_form_invalid(self):
        form_data = {'nombre': '', 'descripcion': 'Descripción del Partido A'}
        form = PartidoForm(data=form_data)
        self.assertFalse(form.is_valid())

class CandidatoFormTest(TestCase):
    def setUp(self):
        self.partido = Partido.objects.create(nombre='Partido X', descripcion='Descripción del Partido X')

    def test_candidato_form_valid(self):
        form_data = {
            'nombre': 'Juan',
            'apellido_paterno': 'Pérez',
            'apellido_materno': 'Gómez',
            'partido': self.partido.id
        }
        form = CandidatoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_candidato_form_invalid(self):
        form_data = {
            'nombre': '',
            'apellido_paterno': 'Pérez',
            'apellido_materno': 'Gómez',
            'partido': self.partido.id
        }
        form = CandidatoForm(data=form_data)
        self.assertFalse(form.is_valid())