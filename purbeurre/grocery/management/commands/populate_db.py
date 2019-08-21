import os
# import sys
# sys.path.append('/C:/Users/Alex Tour/P8-purbeurre/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "purbeurre.settings")
import requests as req
import django
django.setup()
import requests as req
from grocery.models import Category, Product
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    CATEGORYNAME = [
        "Pizzas",
        "Conserves",
        "Fromages",
        "Boissons",
        "Snacks sucrés",
        "Viandes",
        "Charcuteries",
        "Epicerie",
        "Desserts",
        "Surgelés",
        "Sauces",
        "Biscuits",
        "Chocolats",
        "Gâteaux",
        "Confitures",
        "Apéritif",
        "Condiments",
        "Yaourts",
        "Pains",
        "Huiles",
    ]

    idcat = 1
    for name in CATEGORYNAME:
        categ = Category.objects.create(name=name)
        categ.save()
        print(Category.objects.all())
        
        count = 0
        for i in range(1, 20):
            url = ("https://fr.openfoodfacts.org/category/"+ name + "/"+ str(i) + ".json")
            extract = req.get(url)
            response_data = extract.json()
            for products in response_data["products"]:
                if count < 100:
                    if "product_name" in products:
                        if "nutrition_grade_fr" in products:
                            if "image_url" in products:
                                if "url" in products:
                                    if "image_nutrition_url" in products:
                                        print(categ.id)
                                        product = Product.objects.create(name=products["product_name"], nutrigrade=products["nutrition_grade_fr"], image=products["image_url"], url=products["url"], nutrient=products["image_nutrition_url"], category=categ) 
                                        product.save()
                                        count = count + 1
        idcat = idcat +1
                        
