from django.db import models

# Create your models here.
class Link(models.Model):
    
    name_link = models.CharField(verbose_name="Nombre del Link", max_length=50)
    link = models.URLField(verbose_name="Enlace", max_length=200)
    created = models.DateField(verbose_name="Creado", auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name="Actualizado", auto_now=True, auto_now_add=False)
        
    def __str__(self):
        return self.name_link
    
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        