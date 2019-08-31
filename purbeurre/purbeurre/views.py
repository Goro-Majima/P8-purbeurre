import json
import urllib
import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from grocery.models import Category, Product, Favorite
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def homepage(request):
    return render(request, 'grocery/home.html')

def mentions(request):
    return render(request, 'grocery/mentions.html')

def results(request):
    if request.method == 'GET':
        text = request.GET.get('txtSearch')
        product = Product.objects.filter(name__startswith=text).first()
        if product.nutrigrade == 'a':
            substitute_list =[]
        else:
            if product.nutrigrade == 'b':
                substitute_queries= Product.objects.filter(category= product.category, nutrigrade='a')
            elif product.nutrigrade == 'c':
                substitute_queries= Product.objects.filter(Q(category= product.category, nutrigrade='a') | Q(category= product.category, nutrigrade='b'))
            else:
                substitute_queries= Product.objects.filter(Q(category= product.category, nutrigrade='a') | Q(category= product.category, nutrigrade='b') | Q(category= product.category, nutrigrade='c'))
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
            'product_id': product.id,
            'sub_list': substitute_list,
            'paginate': True,
            'text':urllib.parse.quote_plus(text)
        }
    return render(request, 'grocery/results.html', context)

def detail(request, substitute_id):
    try:
        substitute = Product.objects.get(id=substitute_id)
    except:
        substitute = Product.objects.get(id=product_id)
    context = {
        'substitute_name': substitute.name,
        'substitute_image': substitute.image,
        'substitute_nutrigrade': substitute.nutrigrade,
        'substitute_nutrient': substitute.nutrient,
        'substitute_url': substitute.url,
        'substitute_id': substitute.id,
    }
    return render(request, 'grocery/detail.html', context)

# def detail(request):
#     return render(request, 'grocery/detail.html')

@login_required
def favorite(request, user_name):
    if request.method == 'POST':
        product = request.POST.get('substitute')
        myproduct = Product.objects.get(id=product)
        favorite = Favorite.objects.filter(product=myproduct, user=request.user)
        if favorite.exists():
            messages.success(request, f'Ce produit est déjà dans vos favoris !') 
        else:
            favorite = Favorite.objects.create(product=myproduct, user=request.user)
            favorite.save()
            messages.success(request, f'Ce produit a été ajouté à vos favoris !')    
    addfavorite = Favorite.objects.filter(user=request.user)
    if addfavorite != []:
        paginator = Paginator(addfavorite, 6) 
        page = request.GET.get('page')
        try:
            addedfavorite = paginator.page(page)
        except PageNotAnInteger:
            addedfavorite = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            addedfavorite = paginator.page(paginator.num_pages)
        context = {
            'paginate': True,
            'added_favorite': addedfavorite
        }
    else:
        context = {
            'added_favorite': addfavorite
        }
    return render(request, 'grocery/favorite.html', context)
   

    
    # addfavorite = Favorite.objects.filter(user=request.user)
    # paginator = Paginator(addfavorite, 6) 
    # page = request.GET.get('page')
    # try:
    #     addedfavorite = paginator.page(page)
    # except PageNotAnInteger:
    #     addedfavorite = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     addedfavorite = paginator.page(paginator.num_pages)
    # context = {
    #         'added_favorite': addedfavorite
    #     }
    # return render(request, 'grocery/favorite.html', context)
    


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



def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)