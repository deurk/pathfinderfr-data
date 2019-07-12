#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import yaml
import sys
import html
import re
from bs4 import BeautifulSoup
from lxml import html


## Configurations pour le lancement
MOCK_ASTUCE = None
MOCK_ASTUCE = "mocks/astuces.html"       # décommenter pour tester avec les astuces pré-téléchargées



#
# cette fonction extrait le texte du prochain élément après ...
#
def findAfter(html, afterTag, afterCond, searched):
    elements = html.find_next(afterTag, afterCond).next_siblings
    for el in elements:
        if el.name == searched:
            return el.text.strip()

#
# cette fonction extrait le texte pour une propriété <b>propriété</b> en prenant le texte qui suit
#
def findProperty(html, propName):
    for el in html:
        if el.name == 'b' and el.text.lower().startswith(propName.lower()):
            value = ""
            for e in el.next_siblings:
                if e.name == 'br':
                    break
                elif e.string:
                    value += e.string
                else:
                    value += e
            return value.replace('.','').strip()
    return None

#
# cette fonction permet de sauter à l'élément recherché et retourne les prochains éléments
#
def jumpTo(html, afterTag, afterCond, elementText):
    seps = content.find_all(afterTag, afterCond);
    for s in seps:
        if s.text.lower().strip().startswith(elementText.lower()):
            return s.next_siblings

# vérification des paramètres
if len(sys.argv) < 1:
    print("Usage: %s" % sys.argv[0])
    exit(1)

liste = []


if MOCK_ASTUCE:
    content = BeautifulSoup(open(MOCK_ASTUCE),features="lxml").body
else:
    content = BeautifulSoup(urllib.request.urlopen("http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.astuces.ashx").read(),features="lxml").body

section = jumpTo(content, 'h2',{'class':'separator'}, u"Description des astuces de ninja")

LVL = 2
astuce = {'5Niveau':LVL}
newObj = False
descr = ""
source = 'AG'
for s in section:
    if s.name == 'h2' and u"Description des astuces de maître" in s.text:
        LVL = 10
    elif s.name == "table":
        for td in s.find_all('td'):
            for el in td.children:
                if el.name == "h3":
                    nom = el.text
                    if nom.endswith('¶'):
                        nom = nom[:-1]
                    reference = "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.astuces.ashx" + el.find_next("a")['href']

                    if newObj:
                        astuce['2Classe'] = u'Ninja'
                        astuce['6Description'] = descr.strip()
                        astuce['EMPTY'] = ""
                        liste.append(astuce)
                        astuce = {'5Niveau':LVL}
                        
                    descr = ""
                    astuce['1Nom'] = u"Astuce: " + nom
                    astuce['4Source'] = source
                    astuce['7Référence'] = reference
                    source = "AG"
                    newObj = True
                
                elif el.name is None or el.name == 'a':
                    descr += el.string
                elif el.name == 'i':
                    descr += el.text.replace("\n"," ")
                elif el.name == 'b':
                    descr += "\n\n" + el.text.replace("\n"," ").upper()
                elif el.name == 'ul':
                    for li in el.find_all("li"):
                        descr += "\n*) " + li.text.replace("\n"," ")
                elif el.name == 'div':
                    descr += "\n" + el.text.replace("\n", " ") + "\n"
    

# last element        
astuce['2Classe'] = u'Ninja'
astuce['6Description'] = descr.strip()
astuce['EMPTY'] = ""
liste.append(astuce)



yml = yaml.safe_dump(liste,default_flow_style=False, allow_unicode=True)
yml = yml.replace('1Nom','Nom')
yml = yml.replace('2Classe','Classe')
yml = yml.replace(u'3Prérequis',u'Prérequis')
yml = yml.replace('4Source','Source')
yml = yml.replace('5Niveau','Niveau')
yml = yml.replace('6Auto','Auto')
yml = yml.replace('6Description','Description')
yml = yml.replace(u'7Référence',u'Référence')
yml = yml.replace("EMPTY: ''",'')
print(yml)