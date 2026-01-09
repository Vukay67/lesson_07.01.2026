from django.shortcuts import render

def main_page(request):
    return render(request, "index.html", {})

def students_page(request, test):
    return render(request, "second.html", {'test':test})

def date_page(request, date):
    return render(request, "thrid.html", {'date':date})

# Внутри request.GET хранятся все параметры GET - запроса в виде dict
def test_page(request):
    name = request.GET.get('name')
    surname = request.GET.get('surname')
    show = request.GET.get('show')

    if show == "True": 
        show == True
    else: 
        show == False

    print(show)

    login = request.POST.get('login')
    password = request.POST.get('password')

    context = {
        'name': name,
        'surname': surname,
        'show': show,
        'login': login,
        'password': password
    }

    return render(request, "test.html", context)

def task(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    date = request.POST.get('date')
    film = request.POST.get('film')

    context = {
        'name': name,
        'surname': surname,
        'date': date,
        'film': film
    }

    return render(request, "task.html", context)

def calculator(request):
    num_1 = request.POST.get('num_1')
    num_2 = request.POST.get('num_2')
    oper = request.POST.get('oper')
    ans = 0

    if num_1 != None:
        num_1 = int(num_1)
    else:
        num_1 = 0

    if num_2 != None:
        num_2 = int(num_2)
    else:
        num_2 = 0

    if oper == "+":
        ans = num_1 + num_2
    elif oper == "-":
        ans = num_1 - num_2
    elif oper == "*":
        ans = num_1 * num_2
    elif oper == "/":
        ans = num_1 / num_2
        
    context = {
        'num_1': num_1,
        'num_2': num_2,
        'oper': oper,
        'ans': ans
    }

    return render(request, "calculator_page.html", context)