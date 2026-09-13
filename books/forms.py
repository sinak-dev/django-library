from django import forms
from .models import Book
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']  # فقط اسم و متن
        labels = {
            'name': 'نام شما',
            'text': 'متن نظر',
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'status']
        labels = {
            'title': 'عنوان کتاب',
            'author': 'نویسنده',
            'year': 'سال انتشار',
            'status': 'وضعیت',
        }
        widgets = {
            'status': forms.Select(choices=[('available', 'موجود'), ('borrowed', 'امانت رفته')]),
        }