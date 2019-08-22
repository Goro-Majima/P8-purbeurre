from django.http import HttpResponse
from django.shortcuts import render
from grocery.models import Category, Product
import json

def home(request):
    return render(request, 'grocery/home.html')

def results(request):
    if request.method == 'GET':
        text = request.GET.get('txtSearch')
        product = Product.objects.filter(name__startswith=text).first()
        context = {
            'product_name': product.name,
            'product_image': product.image,
            'product_nutrigrade': product.nutrigrade,
            'product_nutrient': product.nutrient,
            'product_url': product.url,
        }
    return render(request, 'grocery/results.html', context)

def mentions(request):
    return render(request, 'grocery/mentions.html')

def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Product.objects.filter(name__startswith=q)
        results = []
        # print(q)
        for r in search_qs:
            results.append(r.name)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)