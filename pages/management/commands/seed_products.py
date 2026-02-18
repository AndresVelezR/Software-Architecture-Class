from django.core.management.base import BaseCommand
from pages.factory import ProductFactory

class Command(BaseCommand):
    help = "Seed the database with products"

    def handle(self, *args, **kwargs):
        ProductFactory.create_batch(8) # este metodo le dice a factory boy que cree 8 instancias. 
        self.stdout.write(self.style.SUCCESS("Succesfully seeded products"))
