
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# this allows us to add items by submitting a post to the add items bar at top of page
def home(request):
    
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Your item has been successfully added!')) #go to hone.html and output w/d links
        return render(request, 'home.html', {'all_items': all_items})
    
    else:
    
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    my_name = 'James Kenney'
    return render(request, 'about.html', {'name': my_name})

# to delete items
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Your item has been successfully deleted!')) #delete confirmation message
    return redirect('home')

# cross off function
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

#to uncross function
def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

#edit function
def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        
        if form.is_valid():
            form.save()
            messages.success(request, ('Your item has been successfully updated!')) #go to hone.html and output w/d links
        return redirect('home')
    
    else:
    
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
    
