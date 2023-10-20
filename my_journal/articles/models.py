from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.name}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} {self.category_name}"
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    categories = models.ForeignKey('articles.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('articles.Tag')

    def __str__(self):
        return f"{self.id} {self.headline}"