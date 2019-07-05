from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.amount
