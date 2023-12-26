from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BooksForm


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books_list': books
    }
    return render(request, 'index.html', context)


def details(request, books_id):
    books = Book.objects.get(id=books_id)
    return render(request,'details.html',{'books':books})

def add_books(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        year = request.POST.get('year')
        img = request.FILES['img']
        books = Book(name=name,desc=desc,author=author,rating=rating,year=year,img=img)
        books.save()
    return render(request, 'add.html')

def update(request,id):
    books = Book.objects.get(id=id)
    form = BooksForm(request.POST or None, request.FILES, instance=books)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form':form,'books':books})

def delete(request,id):
    if request.method=='POST':
        books = Book.objects.get(id=id)
        books.delete()
        return redirect('/')
    return render(request,'delete.html')
