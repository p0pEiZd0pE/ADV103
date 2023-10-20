from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import TagSerializer, CategorySerializer, ArticleSerializer
from .models import Tag, Category, Article

class TagsViewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    page_query_param = 'p'
    
class CategoryViewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    page_query_param = 'p'

class ArticleViewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    page_query_param = 'p'

class Tags(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagsViewPagination

class Category(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryViewPagination

class Article(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleViewPagination
