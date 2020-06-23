from django.db import models

# Create your models here.

class Tech(models.Model):
    
    name = models.CharField(verbose_name="Nombre", max_length=100)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Image", upload_to="tech")
    created = models.DateField(verbose_name="Creado", auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name="Actualizado", auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"