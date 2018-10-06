from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Books(models.Model):
    isbn = models.CharField(max_length=16)
    title = models.CharField(max_length=32)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
