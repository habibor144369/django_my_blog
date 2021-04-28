from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/%y')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=250)
    email = models.EmailField(max_length=150)
    twitter = models.URLField(max_length=350)
    facebook = models.URLField(max_length=350)
    linkdin = models.URLField(max_length=350)
    github = models.URLField(max_length=350)
    stack_overflow = models.URLField(max_length=350)

    def __str__(self):
        return str(self.name)
    
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
        

class Article(models.Model):
    title = models.CharField(max_length=250)
    artcle_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/%y')
    published = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, allow_unicode=True)
   
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify([str(self.title), self.artcle_author, self.category, self.published, self.unique_id])
        super(Article, self).save(*args, **kwargs)

    
class About_Me(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/%y')
    name_1 = models.CharField(max_length=20)
    name_2 = models.CharField(max_length=20)
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    details = RichTextField()
    twitter = models.URLField(max_length=350)
    facebook = models.URLField(max_length=350)
    linkdin = models.URLField(max_length=350)
    github = models.URLField(max_length=350)
    stack_overflow = models.URLField(max_length=350)
    resume = models.FileField(upload_to='documents')
  
    def __str__(self):
        return f'{self.name_1} {self.name_2}'
                                    
