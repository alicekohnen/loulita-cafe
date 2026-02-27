from django.shortcuts import render, get_object_or_404
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
            "id": obj.id,
            "name": obj.name,
            "description": obj.description,
            "price": f"€{obj.price}",
            "allergens": allergens_list,
        }

        sections[obj.category].append(item)

    return render(request, "menu.html", {"sections": sections})

def menu_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    allergens_list = []
    if item.allergens:
        allergens_list = [a.strip() for a in item.allergens.split(",") if a.strip()]

    context = {
        "item": item,
        "allergens": allergens_list,
    }
    return render(request, "menu_detail.html", context)