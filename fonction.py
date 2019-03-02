import os
from bs4 import BeautifulSoup
import requests
from tkinter import *

def readFile(fichier):
    file = open(fichier, "r")
    lecture = file.read()
    file.close()
    return lecture

def writeFile(fichier, contenu):
    file = open(fichier, "a")
    file.write(contenu+"\n")
    file.close()

def verifMail(filepath):
    f = open(filepath, 'r')
    lines = f.readlines()
    out = open(filepath, 'w')
    for line in lines:
        if (line.count('@')==1 and (line.endswith(".fr\n") or line.endswith(".com\n"))) == 1:
            print(line)
            out.write(line)
    f.close()

# Supprime les doublons du fichier
def SetSupDoublons(filePath):
    f = open(filePath, 'r')
    lines = f.readlines()
    lines_set = set(lines)
    out = open(filePath, 'w')
    for line in lines_set:
        out.write(line)
    f.close()

def crawlImport(urlImport, filePath):
    #print(urlImport.get())
    #webUrl = urlImport.get()
    #print(webUrl)
    webUrl = 'http://univcergy.phpnet.org/python/mail.html'
    code = requests.get(webUrl)
    plain = code.text
    tet = []
    s = BeautifulSoup(plain, "html.parser")
    for link in s.findAll('a'):
        ajout = link.get('href')
        if(ajout.startswith("mailto:")):
            tet.append(ajout.split("mailto:")[1])

    out = open(filePath, 'a')
    for tets in tet:
        out.write(tets+'\n')
    out.close()

    print(tet)

def crawler(filePath):
    # Ma fenetre
    importURL = Tk()
    importURL.geometry("500x200")
    importURL.title("Import URL")

    Label(importURL, text='URL import : ', font='Arial 12 bold').place(x=140, y=50)
    urlImport = StringVar()
    Entry(importURL, width=20, textvariable=urlImport).place(x=100,y=100)
    Button(importURL, text="Valider", command=lambda: crawlImport(urlImport, filePath)).place(x=300, y=100)
