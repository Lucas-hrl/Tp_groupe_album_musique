from django.urls import path
from . import views

urlpatterns = [
    #chemins pour le CRUD des groupes de musique
    path("index/", views.index),
    path("formulaire/", views.formulaire),
    path("traitement/",views.traitement),
    path("afficher_all/",views.afficher_all),
    path("afficher_un/<int:id>/", views.afficher_un),
    path("update/<int:id>/",views.update),
    path("traitement_update/<int:id>/",views.traitement_update),
    path("supprimer/<int:id>/",views.supprimer),

    #Chemins pour le CRUD des albums de musique
    path("ajout_album/",views.ajout_album),
    path("traitement_album/",views.traitement_album),
    path("afficher_all_album/",views.afficher_all_album),
    path("afficher_un_album/<int:id>/", views.afficher_un_album),
    path("update_album/<int:id>/",views.update_album),
    path("traitement_update_album/<int:id>/",views.traitement_update_album),
    path("supprimer_album/<int:id>/",views.supprimer_album),
]