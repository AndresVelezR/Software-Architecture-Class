import factory

from .models import Product

class ProductFactory(factory.django.DjangoModelFactory): # la convencion es nombre del modelo + Factory
    # factory.django.DjangoModelFactory usa Model.objects.create() internametne.
    
    class Meta:
        model = Product # Meta es una clase de configuracion. Define que esta factory va aconstruir objetos del modelo PROduct
        # factory_boy necesita saber que clase instanciar, los campos que tiene y el como guardarlos
    
    name = factory.Faker("company")
    price = factory.Faker("random_int", min=200, max=9000)