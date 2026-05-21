from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

items = ["Pizza", "Burger", "Pasta", "Salad"]
# Create your views here.
def pizza(request):
    return HttpResponse("This is the pizza page")



# dynamic wrt index
def item_by_index(request,index):
    if index < len(items):
        # return HttpResponse(f"This is the {items[index]} page")

        # /menu/2/   -> /menu/burger/.  --> redirect
        return HttpResponseRedirect(f"/menu/{items[index]}")
    else:
        return HttpResponse("Item not found")
    
    
# dynamic wrt name. - /menu/pizza/
def item_by_name(request,item):
    if item in items:
        return HttpResponse(f"This is the {item} page")
    else:
        return HttpResponse("Item not found")



 



# /menu/1
# /menu/pizza/

# /menu/2
# menu/burger/

