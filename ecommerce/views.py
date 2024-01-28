from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742313 Kanpitcha Hong-ek views')

def item_view(request, item_id):

    context_data = {
        "item_id": item_id   
    }
    
    return render(request, 'index.html',context= context_data)

# Homework 28/01/2024

def homepage(request):
    return render(request, 'homepage.html', {'page_name': 'Homepage'})

def category_page(request):
    return render(request, 'category.html', {'page_name': 'Category Page'})

def product_page(request):
    return render(request, 'product.html', {'page_name': 'Product Page'})

def checkout_page(request):
    return render(request, 'checkout.html', {'page_name': 'Checkout Page'})

def contact_page(request):
    return render(request, 'contact.html', {'page_name': 'Contact Page'})