from django.db import models

# Create your models here.

class Record(models.Model):

    datum_kreiranja = models.DateTimeField(auto_now_add=True)
    klijent = models.CharField(max_length = 100)
    tip_stranke = models.CharField(max_length = 15)
    email = models.CharField(max_length=50)
    telefon = models.CharField(max_length=13)
    uredjaj = models.CharField(max_length=70)
    opis_zahteva = models.CharField(max_length=300)

    def __str__(self):
        
        return self.klijent 
    