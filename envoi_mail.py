import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *

# Pour envoyer le mail
def sendMail(filePath, fromaddr, password, subject, close):
#def sendMail(filePath):
    print(type(subject))
    close.destroy()
    #fromaddr = "k0t30bScuR2LaForce@gmail.com"
    toaddr ='k0t30bScuR2LaForce@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    #msg['Subject'] = 'Test numero 68954'
    msg['Subject'] = str(subject)

    body = "Ecoute Vador, j'ai fais des tests, et tu n'es pas mon père. Je suis le fils de C3PO"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()

    f = open(filePath, 'r')
    lines = f.readlines()
    for line in lines:
        toaddr = line
        server.sendmail(fromaddr, toaddr, text)
    server.quit()
    f.close()

#Pour le message à envoyer
def mailContent(filePath, fromaddr, pwd, close):
    close.destroy()
    # Ma fenetre
    fenetreContent = Tk()
    fenetreContent.geometry("500x200")
    fenetreContent.title("Send Mail")

    # Le titre
    Label(fenetreContent, text="Votre mail : ", font='Arial 12 bold').place(x=140, y=50)

    # Mes éléments
    contenu = StringVar()

    Label(fenetreContent, text="Content : ", font='Arial 12 bold').place(x=30, y=100)
    entre = Entry(fenetreContent, width=20, textvariable=contenu)

    btnValide = Button(fenetreContent, text='Valider',
                       command=lambda: sendMail(filePath, fromaddr, pwd, contenu.get(), fenetreContent))

    entre.place(x=100, y=100)
    btnValide.place(x=300, y=100)

    fenetreContent.mainloop()

# Pour récupérer les identifiants de la personne
def mailWindow(filePath):
    # Ma fenetre
    fenetreMail = Tk()
    fenetreMail.geometry("500x200")
    fenetreMail.title("Send Mail")

    # Le titre
    Label(fenetreMail, text="Votre mail : ", font='Arial 12 bold').place(x=140, y=50)

    # Mes éléments
    identifiants = StringVar()
    identifiantsPSW = StringVar()

    Label(fenetreMail, text="Mail : ", font='Arial 12 bold').place(x=50, y=100)
    name = Entry(fenetreMail, width=20, textvariable=identifiants)

    Label(fenetreMail, text="Pass : ", font='Arial 12 bold').place(x=50, y=150)
    password = Entry(fenetreMail, width=20, textvariable=identifiantsPSW)

    btnValide = Button(fenetreMail, text='Valider', command=lambda: mailContent(filePath, identifiants.get(), identifiantsPSW.get(), fenetreMail))
    name.place(x=100, y=100)
    password.place(x=100, y=150)
    btnValide.place(x=300, y=100)

    fenetreMail.mainloop()