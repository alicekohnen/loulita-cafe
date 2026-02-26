from django.shortcuts import render
from .models import MenuItem

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def menu(request):
    qs = MenuItem.objects.all().order_by("category", "name")

    sections = {
        "coffee": [],
        "pastry": [],
        "seasonal": [],
    }

    for obj in qs:
        allergens_list = []
        if obj.allergens:
            allergens_list = [a.strip() for a in obj.allergens.split(",") if a.strip()]

        item = {
            "name": obj.name,
            "description": obj.description,
            "price": f"€{obj.price}",
            "allergens": allergens_list,
        }

        sections[obj.category].append(item)

    return render(request, "menu.html", {"sections": sections})