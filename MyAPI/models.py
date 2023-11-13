from django.db import models

# Create your models here.
class Characters(models.Model):
     NAMEK="Namekusei"
     SAIYAN="Saiyajin"
     HUMAN="Human"
     BREEDS_CHOICES = [
        (NAMEK, "Namekusei"),
        (SAIYAN, "Saiyajin"),
        (HUMAN, "Human"),
    ]

     name = models.CharField(max_length=254)
     ki = models.IntegerField()
     breed = models.CharField(max_length=15,choices=BREEDS_CHOICES,default=HUMAN)

     def __str__(self):
          return self.name