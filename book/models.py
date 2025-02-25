from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model) :
    title = models.CharField(max_length=100, verbose_name="论坛名")
    description = models.TextField(verbose_name="论坛简介")
    image = models.ImageField(upload_to='book/images/', verbose_name="论坛封面" )
    url = models.URLField(blank=True, verbose_name="论坛链接")

    class Meta:
        verbose_name = "论坛"
        verbose_name_plural = "论坛"

class Reviews(models.Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
        return self.text

