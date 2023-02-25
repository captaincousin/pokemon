from django.db import models

class Generacion(models.Model):
    NUMERO_GENERACION_CHOICES = (
        (1, 'Primera Generación'),
        (2, 'Segunda Generación'),
        (3, 'Tercera Generación'),
        (4, 'Cuarta Generación'),
        (5, 'Quinta Generación'),
        (6, 'Sexta Generación'),
        (7, 'Séptima Generación'),
        (8, 'No especificado'),
    )
    numero_generacion = models.IntegerField(choices=NUMERO_GENERACION_CHOICES)

    def __str__(self):
        return f"Generación {self.numero_generacion}"

class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField()
    #generacion = models.ForeignKey(Generacion, on_delete=models.CASCADE, default=8)

    def __str__(self):
        return self.nombre

class Entrenador(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    ciudad_natal = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Gimnasio(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    lider = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre