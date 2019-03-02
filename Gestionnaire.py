from tkinter import *
from tkinter.messagebox import *
from fonction_gestion import *
from envoi_mail import *

class gestionnaire:
    def __init__(self, file):
        # Ma fenetre
        fenetreGestion = Tk()
        fenetreGestion.geometry("500x300")
        fenetreGestion.title("Gestionnaire")

        # Mes éléments
        Button(fenetreGestion, text='Dédoublonner', command=lambda: SetSupDoublons(file+'.csv')).place(x=100,y=50)
        Button(fenetreGestion, text='Vérification', command=lambda: verifMail(file+'.csv')).place(x=300,y=50)
        Button(fenetreGestion, text='/!Import CSV/!', command=lambda: importCSV(file, fenetreGestion)).place(x=100,y=100)
        Button(fenetreGestion, text='Import URL', command=lambda: crawler(file+'.csv')).place(x=300,y=100)

        Label(fenetreGestion, text='Liste de mail : ',font='Arial 12 bold').place(x=100,y=150)
        #Affichage des emails

        Button(fenetreGestion, text='Valider', command=lambda: mailWindow(file+'.csv')).place(x=400,y=200)
        campagne = readFile(file+'.csv')
        mails = campagne.split('\n')
        i=0
        for mail in mails:
            Label(fenetreGestion, text=mail).place(x=100, y=200+i)
            i=i+20
        fenetreGestion.mainloop()

