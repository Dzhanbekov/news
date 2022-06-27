from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from .forms import NewsForm
from .models import News


class ListNewsView(ListView):
    queryset = News.objects.order_by('-date')
    template_name = 'base.html'
    context_object_name = 'news_list'


class ListPaginate10NewsView(ListView):
    queryset = News.objects.order_by('-date')
    template_name = 'paginate_list10.html'
    context_object_name = 'news_list'
    paginate_by = 10


class ListPaginate20NewsView(ListView):
    queryset = News.objects.order_by('-date')
    template_name = 'paginate_list20.html'
    context_object_name = 'news_list'
    paginate_by = 20


class ListPaginate50NewsView(ListView):
    queryset = News.objects.order_by('-date')
    template_name = 'paginate_list50.html'
    context_object_name = 'news_list'
    paginate_by = 50


class CreateNewsView(CreateView):
    queryset = News
    form_class = NewsForm
    template_name = 'create_news.html'
    success_url = reverse_lazy('news-list')


class DetailNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        context = {'news': news}
        return render(request, template_name='news_detail.html', context=context)
