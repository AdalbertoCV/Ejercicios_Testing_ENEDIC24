from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'logos')

    def __str__(self):
        return self.nombre
    

class Candidato(models.Model):
    nombre = models.CharField(max_length = 50)
    partido = models.ForeignKey("candidatos.Partido", verbose_name="Partido", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
