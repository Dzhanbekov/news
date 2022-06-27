from django.urls import path
from .views import ListNewsView, CreateNewsView, DetailNewsView, ListPaginate10NewsView,\
    ListPaginate20NewsView, ListPaginate50NewsView

urlpatterns = [
    path('', ListNewsView.as_view(), name='news-list'),
    path('create/', CreateNewsView.as_view(), name='news-create'),
    path('<int:pk>/', DetailNewsView.as_view(), name='news-detail'),
    path('paginate10/', ListPaginate10NewsView.as_view(), name='paginate-10'),
    path('paginate20/', ListPaginate20NewsView.as_view(), name='paginate-20'),
    path('paginate50/', ListPaginate50NewsView.as_view(), name='paginate-50'),
]