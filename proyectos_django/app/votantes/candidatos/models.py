from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre
    

class Candidato(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    apellido_paterno = models.CharField(max_length = 50)
    apellido_materno = models.CharField(max_length = 50)
    partido = models.ForeignKey("candidatos.Partido", verbose_name="Partido", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno


class Votacion(models.Model):
    id = models.AutoField(primary_key = True)
    candidato = models.ForeignKey("candidatos.Candidato", verbose_name="Candidato", on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidato + " - " + str(fecha_hora)
    

    
