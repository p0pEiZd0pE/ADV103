from django.urls import path, include
from .views import Tags, Category, Article

urlpatterns = [
    path('tags/', Tags.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('tags/<int:pk>/', Tags.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('categories/', Category.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('categories/<int:pk>/', Category.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('', Article.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('<int:pk>/', Article.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
