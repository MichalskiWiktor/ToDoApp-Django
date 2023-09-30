from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewItemForm
from .models import ListItem 
from django.http import JsonResponse
import json

# Fix the css
# Change Status checkbox

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
    form = NewItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() # save method can create new object or update and existing one 
        return redirect("list")
    return render(request, "item_form.html", {"form": form})

def delete_item(request, pk):
    ListItem.objects.filter(id=pk).delete()
    return redirect("list")

def changeStatus(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            obj = ListItem.objects.get(pk=data["key1"])
            if obj.status:
                obj.status = False
            else:
                obj.status = True
            obj.save()
            return redirect("list")
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

