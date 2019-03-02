from tkinter import *
from tkinter.messagebox import *
from Gestionnaire import *
from fonction import *

# Fonction qui détruit la fenêtre et call le gestionnaire
def valide(file):
    showinfo('Redirection', 'Vous allez être redirigé')
    fenetreHome.destroy()
    writeFile(file+'.csv', '')
    gestionnaire(file)

# Ma fenetre
fenetreHome = Tk()
fenetreHome.geometry("500x200")
fenetreHome.title("Campagne")

# Le titre
Label(fenetreHome, text="Nom de la Campagne : ",font='Arial 12 bold').place(x=140, y=50)

# Mes éléments
nameFile = StringVar()
campagneName = Entry(fenetreHome, width=20, textvariable=nameFile)
btnValide = Button(fenetreHome, text='Valider', command=lambda: valide(nameFile.get()))
campagneName.place(x=100,y=100)
btnValide.place(x=300,y=100)

fenetreHome.mainloop()





