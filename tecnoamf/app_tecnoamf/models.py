from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudante(User):
    foto = models.ImageField(upload_to = 'curso/')
    data_de_nascimento = models.DateField()

    def __str__(self):
        return f"{self.get_full_name()}"


class Curso(models.Model):
    nome_curso = models.CharField(max_length=255)
    professor = models.ForeignKey(User,on_delete=models.PROTECT)
    data_de_inicio = models.DateField()
    data_de_termino = models.DateField()


    def __str__(self):
        return f"{self.nome_curso}"

class Nota(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()
    data_avaliacao = models.DateField()

    def __str__(self):
        return f"{self.curso.nome_curso}"