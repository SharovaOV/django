from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Film(models.Model):
    ID = models.Index
    name=models.CharField(max_length=300,verbose_name='Name')
    poster=models.ImageField(upload_to='media', null=True,verbose_name='Poster')
    preview=models.TextField(max_length=500,null=True,verbose_name='Summary')
    def  __str__(self):
        return self.name

class Feedback(models.Model):
    ID = models.Index
    date = models.DateTimeField( auto_now_add=True)
    film_id=models.ForeignKey(Film, on_delete=models.CASCADE,verbose_name='Film')
    name=models.CharField(max_length = 70,null=False,verbose_name='Nickname')
    feedback=models.TextField(max_length=1000,null = False,verbose_name='Your feedback')
    positiv=models.BooleanField(null=False)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])

