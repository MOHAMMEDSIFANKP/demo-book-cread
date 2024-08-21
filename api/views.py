from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib import messages

# Create your views here.


def home(request):
    instance = Book.objects.all()
    dicts = {
        'book':instance
    }
    return render(request, 'index.html',dicts)

def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        Book.objects.create(title=title,price=price,description=description)
        return redirect('home')
    else:
        return redirect('home')
    
def book_edit(request,id):
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        description = request.POST.get('description').strip()
        price = request.POST.get('price').strip()

        if title == "":
            messages.error(request, "title can't be blank")
            return redirect('home')
        elif description == "":
            messages.error(request, "description can't be blank")
            return redirect('home')
        try:
            obj = Book.objects.get(id=id)
            obj.title = title
            obj.description = description
            obj.price = price

            obj.save()

            return redirect('home')
        except:
            return redirect('home')
        
    else:
        return redirect('home')
    

def book_delete(request,id):
    try:
        obj = Book.objects.get(id=id)
        obj.delete()
        return redirect('home')
    except:
        return redirect('home')