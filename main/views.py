from django.shortcuts import render


def index(request):
    data = {    #блокнот
        'title': 'Главная страница',
        'values': ['Nastia', 'I', 'Love', 'You'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


