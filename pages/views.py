from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

#from django.http import HttpResponse
# Create your views here.

#def homePageView(request):
    #return HttpResponse('Hello WOrld!')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    
class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "Contact us",
            "email": "contact@onlinestore.fake",
            "phone": "+1 (555) 123-4567",
            "address": "123 Fake Street, Springfield, USA",
        })
        return context
    

##### Show products

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 101},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 77},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 50},
    ]


class ProductIndexView(View):
    template_name = "pages/products/index.html"

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = "pages/products/show.html"

    def get(self, request, id):
        try:
            idx = int(id) - 1
        except ValueError:
            return HttpResponseRedirect(reverse('home'))
        
        if idx < 0 or idx >= len(Product.products):
            return HttpResponseRedirect(reverse('home'))
        
        viewData = {}

        product = Product.products[idx]

        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
