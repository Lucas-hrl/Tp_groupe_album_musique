from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class GroupeFormulaire(ModelForm):
    class Meta:
        model = models.Groupe
        fields = ('nom','annee_creation')
        labels = {
            'nom':_('Nom du groupe: '),
            'annee_creation':_("Année de formation du groupe: "),
        }

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'Nom du groupe…'}),
        }


class AlbumFormulaire(ModelForm):
    class Meta:
        model = models.Album
        fields = ('nom_album', 'date_sortie', 'style_musique','nbr_musique','duree')
        labels = {
            'nom_album': _("Nom de l'album: "),
            'date_sortie': _("Date de parution: "),
            'style_musique': _("Style de musique: "),
            'nbr_musique': _("Nombre de pistes musicale: "),
            'duree': _("Temps d'écoute: "),
        }

        widgets = {
    'nom_album': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': "Nom de l'album…"}),
            'date_sortie': forms.DateInput(attrs={'class': 'class_css_input', 'type': 'date'}),
            'style_musique': forms.Select(attrs={'class': 'class_css_input'}),
            'nbr_musique': forms.NumberInput(attrs={'class': 'class_css_input', 'placeholder': 'Nombre de titres...', 'min': '0'}),
            'duree': forms.TimeInput(attrs={'class': 'class_css_input', 'type': 'time' , 'placeholder': 'HH:MM:SS','step':'1'})

}