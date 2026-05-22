from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

items = ["Pizza", "Burger", "Pasta", "Salad"]
# Create your views here.
def pizza(request):
    return HttpResponse("<h1>This is the pizza page</h1>")



# dynamic wrt index
def item_by_index(request,index):
    if index < len(items):
        # return HttpResponse(f"This is the {items[index]} page")

        # /menu/2/   -> /menu/burger/.  --> redirect
        # return HttpResponseRedirect(f"/menu/{items[index]}")


        # url_pizza = reverse("pizza")   #frames the url. -> /menu/pizza/

        url_item = reverse( "item_by_name",args=[items[index]])  #frames the url. -> /menu/pizza/
        return HttpResponseRedirect(url_item)
    
    else:
        return HttpResponse("<h1>Item not found</h1>")
    
    # /menu/pizza/no_of_ppl/


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

