from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>سلام!</h1><p>این اولین صفحه‌ی جنگو من است.</p>")