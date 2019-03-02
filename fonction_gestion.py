from tkinter import *
from tkinter import filedialog
from fonction import *
from Gestionnaire import *
import time

def importCSV(sourceFile, oldPage):
    filepath = filedialog.askopenfilename(filetypes=[('csv files', '.csv')])
    writeFile(sourceFile+'.csv', readFile(filepath))

    #Probleme de creation de page
    #oldPage.destroy()
    #gestionnaire(sourceFile)
