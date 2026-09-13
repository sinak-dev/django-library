from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
# books/views.py

from django.shortcuts import get_object_or_404
from .models import Book, Comment
from .forms import CommentForm

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comments.all()  # گرفتن نظرات این کتاب خاص

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # هنوز ذخیره نکن
            comment.book = book                # کتاب را به نظر وصل کن
            comment.save()                     # حالا ذخیره کن
            return redirect('book_detail', book_id=book.id)
    else:
        form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': comments,
        'form': form
    })


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # بعد از ذخیره، به لیست کتاب‌ها برو
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})