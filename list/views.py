from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewItemForm 
from .models import ListItem 

def showList(request):
    items = ListItem.objects.all()
    context = {"items":items}
    return render(request, "list.html", context)

def create_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = NewItemForm()
    return render(request, "item_form.html", {"form": form})

def update_item(request, pk):
    obj = ListItem.objects.get(pk=pk)
    # an empty NewItemForm means new Form
    # with request.POST we fill the form with data that was submited
    # and with instance we can fill the form with data that we choose
    form = NewItemForm(request.POST or None, instance=obj) #
    if form.is_valid():
        form.save() # save method can create new object or update and existing one 
        return redirect("list")
    return render(request, "item_form.html", {"form": form})

def delete_item(request):
    return HttpResponse("New Item")
 