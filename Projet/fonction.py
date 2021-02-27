from requests import get
import bs4
import sys
import re
import requests as rq
from collections import namedtuple

noms_club =  namedtuple("Resultats", ("date", "competition", "equipe equipe1", "score"))

def extrait_equipe(page):
    raise NotImplementedError
    
def extrait_arbre(noms_club):
    chemin = "https://www.lequipe.fr/Football/FootballFicheEquipe26.html" + noms_club
    page = get(chemin)
    texte = page.text
    arbre = bs4.BeautifulSoup(texte, "lxml")
    return arbre

def extrait_date(arbre):
    noeud, = arbre.find_all("th", text="date")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d{1,3})\\xA0(\d{3})")
    (n1, n2), = motif.findall(resultat.text)
    resultat_final = int(n1 + n2)
    return resultat_final

def extrait_competition(arbre):
    """Prends une page wikipedia de pays sous forme d'arbre et renvoit son PIB."""
    noeud, *_ = arbre.find_all("a", text="PIB nominal")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d)\\xA0?(\d{3}),(\d{3})")
    (n1, n2, n3), = motif.findall(resultat.text)
    resultat_final = int(n1 + n2 + n3 + "0" * 6)
    return resultat_final
    