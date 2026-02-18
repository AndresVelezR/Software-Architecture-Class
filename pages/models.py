from django.db import models


class Product(models.Model): # la implementación esta en base.py del repo de django en ghub.
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # toma el time stamp de cuando se crea un registro en especifico
    updated_at = models.DateTimeField(auto_now=True) # el auto now es par a que guarde el time stamp cada vez que se guarde, no cada que se cree

    def __str__(self) -> str: # la notación con la -> no influye funcionalmente. Es solo para hacer anotaciones de los tipos
        # los metodos que comienzan y terminan con __ (doble guion bajo) son especiales. POr ejemplo este es para decir como debe mostrarse el objeto si se ve como string
        return f"{self.name} (${self.price})" # el self es para indicar que es sobre una instancia en especifico. Por eso el parametro de la funcion tambien es self, porque es para la instancia para la que se llame.

