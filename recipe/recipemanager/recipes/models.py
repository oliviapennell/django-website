from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Step(models.Model):
    step_text = models.CharField(max_length=100, blank=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Ingredient(models.Model):
    text = models.CharField(max_length=100, blank=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

