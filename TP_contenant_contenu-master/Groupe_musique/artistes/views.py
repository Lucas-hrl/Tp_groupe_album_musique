from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import GroupeFormulaire, AlbumFormulaire
from . import models
# Create your views here.

def index (request):
    return render(request,"artistes/index.html")

def formulaire(request):
    form = GroupeFormulaire()
    return render(request, "artistes/formulaire.html", {"form":form})

def traitement(request):
    gform = GroupeFormulaire(request.POST)
    if gform.is_valid():
        Groupe = gform.save()
        return HttpResponseRedirect("/artistes/index/")
    else:
        return render(request,"artistes/formulaire", {"gform":gform})

def afficher_all(request):
    liste_groupe = list(models.Groupe.objects.all())
    return render(request, "artistes/afficher_all.html", {"liste_g":liste_groupe})

def afficher_un(request,id):
    groupe= models.Groupe.objects.get(pk=id)
    return render (request, "artistes/afficher_un.html", {"groupe": groupe})

def update(request,id):
    groupe = models.Groupe.objects.get(pk=id)
    dico= groupe.dico()
    form = GroupeFormulaire(dico)
    return render(request,"artistes/formulaire.html", {"form":form, "id":id})

def traitement_update (request,id):
    gform = GroupeFormulaire(request.POST)
    if gform.is_valid():
        Groupe = gform.save(commit = False)
        Groupe.id = id
        Groupe.save()
        return HttpResponseRedirect("/artistes/index/")
    else:
        return render(request, "artistes/formulaire", {"gform": gform , "id":id})

def supprimer(request,id):
    groupe = models.Groupe.objects.get(pk=id)
    groupe.delete()
    return HttpResponseRedirect("/artistes/afficher_all/")



#actions pour les albums
def ajout_album(request):
    form = AlbumFormulaire()
    return render(request, "artistes/ajout_album.html", {"form": form})

def traitement_album(request):
    form = AlbumFormulaire(request.POST)
    if form.is_valid():
        Album = form.save()
        return HttpResponseRedirect("/artistes/index/")
    else:
        return render(request,"artistes/ajout_album/", {"form":form})

def afficher_all_album(request):
    liste_album = list(models.Album.objects.all())
    return render(request, "artistes/afficher_all_album.html", {"liste_a":liste_album})

def afficher_un_album(request,id):
    album= models.Album.objects.get(pk=id)
    return render (request, "artistes/afficher_un_album.html", {"album": album})

def update_album(request,id):
    album = models.Album.objects.get(pk=id)
    dico= album.dico()
    form = AlbumFormulaire(dico)
    return render(request,"artistes/ajout_album.html", {"form":form, "id":id})

def traitement_update_album (request,id):
    aform = AlbumFormulaire(request.POST)
    if aform.is_valid():
        Album = aform.save(commit = False)
        Album.id = id
        Album.save()
        return HttpResponseRedirect("/artistes/index/")
    else:
        return render(request, "artistes/ajout_album", {"aform": aform , "id":id})

def supprimer_album(request,id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return HttpResponseRedirect("/artistes/afficher_all_album")