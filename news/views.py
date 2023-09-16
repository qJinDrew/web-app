from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')  # сортировка по дате
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':  # проверка
        form = ArticlesForm(request.POST)  # получаем данные, которые ввел пользователь
        if form.is_valid():  # проверка данных
            form.save()  # если они корректны - сохраняем в БД
            return redirect('home')  # переход на страницу news
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', date)
