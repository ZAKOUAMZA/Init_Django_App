from django.db import models


class Identifiant(models.Model):
    Nom=models.TextField()
    Prenom=models.TextField()
    Age = models.IntegerField
    
    def __str__(self):
        return self.Nom