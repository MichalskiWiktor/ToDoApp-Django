from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewItemForm 
from .models import ListItem 


# Create your views here.
def showList(request):
    items = ListItem.objects.all()
    context = {"items":items}
    return render(request, "list.html", context)

def create_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()

            redirect("list")
    else:
        form = NewItemForm()

    return render(request, "item_form.html", {"form": form})

def update_item(request):
    return HttpResponse("New Item")

def delete_item(request):
    return HttpResponse("New Item")

def view_item(request):
    return HttpResponse("New Item")
 