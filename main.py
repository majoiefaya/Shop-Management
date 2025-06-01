from tkinter import *
import tkinter.font as font
from tkinter.messagebox import showerror,showinfo
window=Tk()
window.title("Ma Boutique ")
window.geometry("897x790")
window.config(background="#11719e")
#
#fond d ecran de l image
width=800
height=600
image=PhotoImage(file="supermarche.png")
canvas=Canvas(window, width=width,height=height,bg="#031536",bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2, image=image)
canvas.place(x=50,y=80)
window.iconbitmap("ico1.ico")
import mysql.connector as mysql

db= mysql.connect(
    host= "localhost",
    user= "root",
    password= "",
    database="MA_BOUTIQUE"
    )

#print(db)

cursor = db.cursor()
class Table: 
      
    def __init__(self,window): 
          
        
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                tableau= Entry(window, width=20, fg='black',font=('Arial',10,'bold'))
                f = font.Font(family='Freestyle Script', size=22, weight="bold")
                tableau["font"]=f
                tableau.grid(row=i, column=j) 
                tableau.insert(END,lst[i][j]) 
  
  
lst = [("code",'Designation','Prix',"categorie"), 
       (2,'PAIN','100',"consommation"), 
       (3,'Eau','25',"consommation"), 
       (4,'COCACOLA',"450",'consommation'), 
       (5,'Boeur','500','consommation')]


class Article:
    def __init__(self,code,designation,prix,categorie):
        self._code=code
        self._designation=designation
        self._prix=prix
        self._categorie=categorie

class Achat:
    def __init__(self,numero,Article,quantite):
        self._numero=numero
        self._Article=Article
        self._quantite=quantite
liste_Achat=[]
liste_art=[]

def verifie1(liste_art,value):
        for i in range(len(liste_art)):
            if liste_art[i].__eq__(value):
                return False
            else:
                return True

def verifie2(liste_Achat,value):
        for i in range(len(liste_Achat)):
            if liste_Achat[i].__eq__(value):
                return False
            else:
                return True
"""def verifie2():
    if codeEntry.get() and DesignationEntry.get() and\
       PrixEntry.get() and categorieEntry.get():
        newarticle=Article(codeEntry.get(),DesignationEntry.get,PrixEntry.get(),categorieEntry.get())
        for i in liste_art:
            if codeEntry.get()==i:
                showerror(title="Formulaire invalide",message="Article deja Ajouté")
            else:
                liste_art.append(newarticle)
                showinfo(title="validation reusie",message="Article bien inseré")"""
def Valider():
    if codeEntry.get() and DesignationEntry.get() and\
        PrixEntry.get() and categorieEntry.get():
        newarticle=Article(codeEntry.get(),DesignationEntry.get,PrixEntry.get(),categorieEntry.get())
        if verifie1(liste_art,newarticle):
            showerror(title="Formulaire invalide",message="Article deja Ajouté")
        else:
            
            insertion="INSERT INTO article(codeart,design,prix,categorie)VALUES(%s,%s,%s,%s)"
            valeurs=(codeEntry.get(),DesignationEntry.get(),PrixEntry.get(),categorieEntry.get())
            cursor.execute(insertion, valeurs)
            db.commit()
            liste_art.append(newarticle)
            showinfo(title="validation reusie",message="Article bien inseré")   
            facture =Text(window, height = 2,width = 40,fg="white",bg="#11719e",bd=3)
            f = font.Font(family='Freestyle Script', size=22, weight="bold")
            facture["font"]=f
            #img =PhotoImage(file = "panier.png")
            #facture.image_create(END,image=img)
            facture.insert(END,"code")
            facture.insert(END,"\t")
            facture.insert(END,"designation")
            facture.insert(END,"\t")
            facture.insert(END," ")
            facture.insert(END,"Prix")
            facture.insert(END,"\t")
            facture.insert(END,"Categorie")
            facture.insert(END,"\t")
            facture.insert(END,"\n")
            facture.insert(END,codeEntry.get())
            facture.insert(END,"\t")
            facture.insert(END,DesignationEntry.get())
            facture.insert(END,"\t")
            facture.insert(END," ")
            facture.insert(END,PrixEntry.get())
            facture.insert(END,"\t")
            facture.insert(END,categorieEntry.get())
            facture.place(x=907,y=45)
    else:
        showerror(title="Formulaire invalide",message="Tous les champs doivent etre renseignés")
            #code=codeEntry.get()
            #designation=designationEntry.get()
            #prix=prixEntry.get()
            #categorie=categorieEntry.get()
def Annuler1():
    code=codeEntry.delete(0,END)
    designation=DesignationEntry.delete(0,END)
    prix=PrixEntry.delete(0,END)
    categorie=categorieEntry.delete(0,END)
    
def Annuler2():
    numero=numeroEntry.delete(0,END)
    Article=ArticleEntry.delete(0,END)
    quantite=QuantiteEntry.delete(0,END)
    
   
def Valider2():
    if numeroEntry.get() and ArticleEntry.get() and\
        QuantiteEntry.get():
        newachat=Achat(numeroEntry.get(),ArticleEntry.get,QuantiteEntry.get())
        if verifie2(liste_Achat,newachat):
            showerror(title="Formulaire invalide",message="Achat deja Ajouté")
        else:
            
            insertion="INSERT INTO achat(numero,article,quantite)VALUES(%s,%s,%s)"
            valeurs=(numeroEntry.get(),ArticleEntry.get(),QuantiteEntry.get())
            cursor.execute(insertion, valeurs)
            db.commit()
            liste_Achat.append(newachat)
            showinfo(title="validation reusie",message="Achat bien inseré")   
            facture =Text(window, height = 2,width = 40,fg="white",bg="#11719e",bd=3)
            """logo = BitmapImage('logo.xbm', foreground='red')
            facture(image=logo).grid()
            sbar = Scrollbar(facture)
            sbar.config(command=list.yview)
            facture.config(yscrollcommand=sbar.set)
            sbar.place(x=7,y=40)"""
            f = font.Font(family='Freestyle Script', size=22, weight="bold")
            facture["font"]=f
            #img =PhotoImage(file = "panier.png")
            #facture.image_create(END,image=img)
            facture.insert(END,"Numero")
            facture.insert(END,"\t")
            facture.insert(END,"\t")
            facture.insert(END,"Article")
            facture.insert(END,"\t")
            facture.insert(END,"\t")
            facture.insert(END," ")
            facture.insert(END,"Quantite")
            facture.insert(END,"\n")
            facture.insert(END,numeroEntry.get())
            facture.insert(END,"\t")
            facture.insert(END,"\t")
            facture.insert(END,ArticleEntry.get())
            facture.insert(END,"\t")
            facture.insert(END,"\t")
            facture.insert(END," ")
            facture.insert(END,QuantiteEntry.get())
            facture.place(x=907,y=170)
    else:
        showerror(title="Formulaire invalide",message="Tous les champs doivent etre renseignés")

def liste_article():
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("Listes des articles")
    fenetre_liste.geometry("490x300")
    fenetre_liste.iconbitmap("ico1.ico")
    fenetre_liste.config(background="#11719e")
    cursor.execute("SELECT* FROM article")
    label_liste_article=Label(fenetre_liste, text="Listes des Articles",fg="white",bg="#11719e")
    f = font.Font(family='Freestyle Script', size=22, weight="bold")
    label_liste_article["font"]=f
    label_liste_article.place(x=150,y=0)

    rows=cursor.fetchall()
    affichage_article=Text(fenetre_liste, height = 7,width = 44,fg="white",bg="#11719e",bd=3)
    f = font.Font(family='Freestyle Script', size=20, weight="bold")
    affichage_article["font"]=f
    affichage_article.insert(END,rows) 
    affichage_article.place(x=21,y=40)    
label_liste=Label(window, text="Article Ajouté",fg="white",bg="#11719e")
label_liste.place(x=1060,y=0)
label_achat=Label(window, text="Achat Ajouté",fg="white",bg="#11719e")
label_achat.place(x=1060,y=120)
f = font.Font(family='Freestyle Script', size=25, weight="bold")
f.configure(underline=True)
label_achat["font"]=f
f = font.Font(family='Freestyle Script', size=25, weight="bold")
label_liste["font"]=f
f.configure(underline=True)
labelajout=Label(window, text="Ajout d'articles",fg="white",bg="#11719e")
labelajout.place(x=400,y=200)
f = font.Font(family='Freestyle Script', size=22, weight="bold")
labelajout["font"]=f

codeEntry=Entry(window,textvariable=IntVar(),width=30)
codeEntry.place(x=150,y=230)
label1=Label(window, text="Code:",bg="#11719e",fg="white")
f = font.Font(family='Freestyle Script', size=22, weight="bold")
label1["font"]=f

label1.place(x=30,y=230)

DesignationEntry=Entry(window, textvariable=StringVar(), width=30)
DesignationEntry.place(x=150, y=270)
label2=Label(window, text="Designation:",bg="#11719e",fg="white")
label2.place(x=30, y=270)
f = font.Font(family='Freestyle Script', size=22, weight="bold")
label2["font"]=f

PrixEntry=Entry(window, textvariable=IntVar(), width=30)
PrixEntry.place(x=150, y=320)
label3=Label(window, text="Prix:",bg="#11719e",fg="white")
label3.place(x=30, y=320)
f = font.Font(family='Freestyle Script', size=22, weight="bold")
label3["font"]=f

categorieEntry=Entry(window, textvariable=StringVar(), width=30)
categorieEntry.place(x=150, y=370)
label4=Label(window, text="categorie:",bg="#11719e",fg="white")
f = font.Font(family='Freestyle Script', size=22, weight="bold")
label4["font"]=f
label4.place(x=30, y=370)

labelachat=Label(window, text="Ajout d'achat",fg="white",bg="#11719e")
f = font.Font(family='Freestyle Script', size=22, weight="bold")
labelachat["font"]=f
labelachat.place(x=400,y=400)

##
numeroEntry=Entry(window,textvariable=IntVar(),width=30)
numeroEntry.place(x=150,y=470)
labelnum=Label(window, text="Numero:",bg="#11719e",fg="white")
f = font.Font(family='Freestyle Script', size=22, weight="bold")
labelnum["font"]=f
labelnum.place(x=30,y=470)

ArticleEntry=Entry(window, textvariable=StringVar(), width=30)
ArticleEntry.place(x=150, y=520)
labelArticleEntry=Label(window, text="Article:",bg="#11719e",fg="white")
labelArticleEntry.place(x=30, y=520)
f = font.Font(family='Freestyle Script', size=22, weight="bold")
labelArticleEntry["font"]=f


QuantiteEntry=Entry(window, textvariable=IntVar(), width=30)
QuantiteEntry.place(x=150, y=570)
labelquantite=Label(window, text="Quantite:",bg="#11719e",fg="white")
labelquantite.place(x=30, y=570)
f = font.Font(family='Freestyle Script', size=22, weight="bold")
labelquantite["font"]=f




bouttonarticle=Button(window, text="+Ajouter Article", width=13, height=1,bg="#FF6800",fg="white",command=Valider)
bouttonarticle.place(x=745,y=355)
f = font.Font(family='Freestyle Script', size=12, weight="bold")
bouttonarticle["font"]=f

bouttonarticle_anuler=Button(window, text="Anuller", width=13, height=1,bg="#FF6800",fg="white",command=Annuler1)
bouttonarticle_anuler.place(x=745,y=255)
f = font.Font(family='Freestyle Script', size=12, weight="bold")
bouttonarticle_anuler["font"]=f


bouttonachat=Button(window, text="+Ajouter Achat", width=13, height=1,bg="#FF6800",fg="white",command=Valider2)
bouttonachat.place(x=745,y=569)   
f = font.Font(family='Freestyle Script', size=12, weight="bold")
bouttonachat["font"]=f

bouttonachat_anuler=Button(window, text="Anuller", width=13, height=1,bg="#FF6800",fg="white",command=Annuler2)
bouttonachat_anuler.place(x=745,y=470)
f = font.Font(family='Freestyle Script', size=12, weight="bold")
bouttonachat_anuler["font"]=f


bouttonfacture=Button(window, text="Details Facture", width=13, height=1,bg="#FF6800",fg="white")
bouttonfacture.place(x=1074,y=270) 
f = font.Font(family='Freestyle Script', size=12, weight="bold")
bouttonfacture["font"]=f
total_rows = len(lst) 
total_columns = len(lst[0])
t = Table(window) 

menuprinci=Menu(window,tearoff=0)


menu_afficher=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Afficher",menu=menu_afficher)
menu_afficher.add_command(label="Listes des articles",command=liste_article)

window.config(menu=menuprinci)
window.mainloop() 