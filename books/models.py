from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):  
    name = models.CharField(max_length=100, null=True)
    author = models.JSONField()
    year_published = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    my_review =  models.TextField(max_length=300, null=True, blank=True)
    stars = models.IntegerField(default=5)
    unfinished = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ["my_review", "stars", "unfinished"]

    def __str__(self):
        return '{} - {} - {}'.format(self.my_review, self.stars, self.unfinished)
    

class Topic(models.Model):
    # topic to the user wants to learn
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    
class Entry(models.Model):
    # Something specific learned

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        # Return string representation of the first 50 characters from the model
        return f'{self.text[:50]}...'     
      

    
