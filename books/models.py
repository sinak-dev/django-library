from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    status = models.CharField(
        max_length=10,
        choices=[('available', 'موجود'), ('borrowed', 'امانت رفته')],
        default='available'
    )

    def __str__(self):  
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)  # اسم کسی که نظر داده
    text = models.TextField()                # متن نظر
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ثبت

    def __str__(self):
        return f"نظر {self.name} برای {self.book.title}"