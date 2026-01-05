from django.shortcuts import render

def main_page(request):
    return render(request, "index.html", {})

def students_page(request, test):
    return render(request, "second.html", {'test':test})

def date_page(request, date):
    return render(request, "thrid.html", {'date':date})