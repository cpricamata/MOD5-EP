from django.shortcuts import render
from .models import Supplier
from .models import WaterBottle

# Create your views here.
def view_bottles(request):
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/bottles.html', {'bottles':bottle_objects})

def view_supplier(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/suppliers.html', {'suppliers':supplier_objects})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')