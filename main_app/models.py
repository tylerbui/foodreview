from django.db import models
from django.urls import reverse 
# Create your models here.

MEALS = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
)


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})
    
class Eat(models.Model):
    date = models.DateField('Meal Time')
    meal = models.CharField(
    max_length=30,
    choices=MEALS,
    default=MEALS[0][0]
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class FoodCategory(models.Model):
    food = models.ManyToManyField(Food)
    eat = models.ManyToManyField(Eat)

    def __str__(self):
        return f"{self.food} - {self.eat}"