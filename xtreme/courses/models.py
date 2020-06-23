from django.db import models

# Create your models here.
class Card(models.Model):
    
    CATEGORY_CHOICES = (
        ('m', 'Movíl'),
        ('w', 'Web'),
    )
    
    title = models.CharField(verbose_name="Titulo", max_length=100)
    start = models.DateField(verbose_name="Fecha de inicio")
    price = models.IntegerField(verbose_name="Costo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="product")
    type = models.CharField(verbose_name="Tipo", max_length=50, choices=CATEGORY_CHOICES)
    created = models.DateField(verbose_name="Creado", auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name="Actualizado", auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Carta"
        verbose_name_plural = "Cartas"
        

class Question(models.Model):
    card = models.ForeignKey(Card, verbose_name="Carta", on_delete=models.CASCADE)
    question = models.CharField(verbose_name="Pregunta", max_length=200)
    response = models.CharField(verbose_name="respuesta", max_length=200)
    temary = models.URLField(verbose_name="Temario", max_length=400,)
    created = models.DateField(verbose_name="Creado", auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name="Actualizado", auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        