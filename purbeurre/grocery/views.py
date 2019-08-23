import urllib
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from grocery.models import Category, Product


def home(request):
    return render(request, 'grocery/home.html')

def results(request):
    if request.method == 'GET':
        text = request.GET.get('txtSearch')
        product = Product.objects.filter(name__startswith=text).first()
        if product.nutrigrade == 'a':
            substitute_list =[]
        else:
            substitute_queries= Product.objects.filter(category= product.category, nutrigrade='a')
            print(substitute_queries)
            paginator = Paginator(substitute_queries, 6) 
            page = request.GET.get('page')
            try:
                substitute_list = paginator.page(page)
            except PageNotAnInteger:
                substitute_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                substitute_list = paginator.page(paginator.num_pages)
        context = {
            'product_name': product.name,
            'product_image': product.image,
            'product_nutrigrade': product.nutrigrade,
            'product_nutrient': product.nutrient,
            'product_url': product.url,
            'sub_list': substitute_list,
            'paginate': True,
            'text':urllib.parse.quote_plus(text)
        }

    return render(request, 'grocery/results.html', context)

def detail(request):
    return render(request, 'grocery/detail.html')

def favorites(request):
    return render(request, 'grocery/favorites.html')

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