from django.db import models


# Create your models here.
class Groupe(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    annee_creation = models.IntegerField(blank=False)
    nbr_album = models.IntegerField()
    nationalite = models.CharField(max_length=100, blank=False)

    def __str__(self):
        chaine = f"Le groupe {self.nom} fondé en  {self.annee_creation} est {self.nationalite}"
        return chaine

    def dico(self):
        return {"nom":self.nom,"annee_creation":self.annee_creation}




class Album(models.Model):
    STYLES = [
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('pop', 'Pop'),
        ('rap', 'Rap'),
        ('classique', 'Classique'),
        ('metal', 'Metal'),
        ('reggae', 'Reggae'),
        ('blues', 'Blues'),
        ('electro', 'Électronique'),
        ('rnb', 'R&B'),
        ('soul', 'Soul'),
        ('funk', 'Funk'),
        ('country', 'Country')
    ]

    nom_album = models.CharField(max_length=100, blank=False)
    date_sortie = models.CharField(max_length=100, blank=False)
    style_musique = models.CharField(max_length=50,choices=STYLES,blank=False)
    nbr_musique = models.PositiveIntegerField(blank=False)
    duree = models.DurationField(blank=False)

    def __str__(self):
        chaine = f"L'album {self.nom_album} sorti le  {self.date_sortie.strftime('%d %B %Y')} , dans la catégorie {self.style_musique}, contient {self.nbr_musique} musiques pour une durée de {self.duree}"
        return chaine

    def dico(self):
        return {"nom_album":self.nom_album,"date_sortie":self.date_sortie, "style_musique":self.style_musique,"nbr_musique":self.nbr_musique, "duree":self.duree}