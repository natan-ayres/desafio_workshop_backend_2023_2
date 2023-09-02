from django.db import models

def upload_image_filme(instance, filename):
    return f"{instance.id_book}-{filename}"

class Filme(models.Model):
    filme = models.CharField(max_length = 100)
    image = models.ImageField(
        upload_to=upload_image_filme, blank=True, null=True )
    def __str__(self):
        return f'{self.filme}'

class Pessoa(models.Model):
    nome = models.CharField(max_length = 20)
    filme = models.ForeignKey(
        Filme,
        max_length= 100,
        on_delete=models.CASCADE, 
        null= True
    )
    nota = models.DecimalField(max_digits= 2, decimal_places= 1)

