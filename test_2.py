
"""class Article:
    
    #creation de la classe article
    def __init__(self,code,designation,prix,categorie):
        self._code=code
        self._designation=designation
        self._prix=prix
        self._categorie=categorie
    def _get_code(self):
        return(self._code)
    def _set_code(self):
        newcode=input("nouveau code....>")
        self._code=newcode
    code=property(_get_code,_set_code)
    
    
    def _get_design(self):
        return(self._designation)
    def _set_design(self):
        newdesign=input("nouveau design...>")
        self._designation=newdesign
    design=property(_get_design,_set_design)
     
    def _get_prix(self):
        return(self._prix)
    def _set_prix(self):
        newprix=input("nouveau prix...>")
        self._prix=newprix
    prix=property(_get_prix,_set_prix)
    
    def _get_categorie(self):
        return(self._categorie)
    def _set_categorie(self):
        newcategorie=input("nouvelle categorie...>")
        self._categorie=newcategorie
    categorie=property(_get_categorie,_set_categorie)
    
    def afficher1(self):
        print("le code de l article:",self._code,"le design est:",self._designation,"le prix est de :",self._prix,"la categorie est:",self._categorie)
    def comparer(self,objet2):
        if self.code==objet2.code and self.design==objet2.design and self.prix==objet2.prix and self.categorie==objet2.categorie:
            return(True)
            print("Egal")
        else:
            return(False)
            print("different")
    
    
    
    

article1=Article(1,"eponge",450,"solide")
article2=Article(4,"savon",3000,"solide")
article3=Article(1,"eau",2000,"liquide")
article4=Article(1,"gaz",2000,"gazeux")
article1.comparer(article3)
article1.afficher1()
article2.afficher1()
article3.afficher1()


class Achat:
    def __init__(self,numero,Article,quantite):
        self._numero=numero
        self._Article=Article
        self._quantite=quantite
        
        
    def _get_numero(self):
        return(self._numero)
    def _set_numero(self):
        newnum=input("nouveau numero...>")
        self._numero=newnum
    numero=property(_get_numero,_set_numero)
        
    def _get_Article(self):
        return(self._Article)
    def _set_Article(self):
        newart=input("nouveau article...>")
        self._Article=newart
    article=property(_get_Article,_set_Article)    
    
        
    def _get_quantite(self):
        
        return(self._quantite)
    def _set_quantite(self):
        newquantite=input("nouveau quantite...>")
        self._quantite=newquantite
    quantite=property(_get_quantite,_set_quantite)
        
    def modifier(self):
        choix=input("ajoutez ou modifier:...>")
        if choix=="ajouter":
            newvalue=int(input("Entrez la quantite a ajouter...>"))
            self._quantite+=newvalue
            print("la nouvelle quantite est :",newvalue)
        elif choix=="modifier":
            newvalue=int(input("Entrez la nouvelle quantite...>"))
            self._quantite=newvalue
            print("la nouvelle quantite est :",newvalue)
            
        
        
    def afficher2(self):
        print("le numero est:",self._numero,"l article est:",self._Article._categorie,"et la quantite est:",self._quantite)
    def __add__(self,achat):
        if self._Article.comparer(achat._Article):
            self._quantite=self._quantite
            achat=Achat(achat._numero,achat._Article,achat._quantite)
            self._quantite=achat.quantite+self._quantite
            achat._quantite=self._quantite
            achat.afficher2()
            return(achat)
        else:
            print("\nImpossible d additionner ses achats\n")
    def __ne__(self,achat):
        if self.quantite*self.article.prix!=achat.quantite*achat.article.prix:
            return(True)
        else:
            return(False)
#i!nstanciation de la classe achat   
achat1=Achat(1,article1,4)#numero ,Article ,Quantite#achat1==Achat(1;1,"eponge",450,"solide"
achat2=Achat(4,article2,9)
achat3=Achat(3,article3,9)
achat4=Achat(5,article3,4)
achat4.afficher2()
achat2.afficher2()
achat2._Article.afficher1()
achat3.afficher2()
achat4.afficher2()
achat3.__add__(achat2)
test1=achat1!=achat2

class Facture:
    
    
    def __init__(self,numerofa,date,collection):
        self._numerofa=numerofa
        self._date=date
        self._collection=collection
    def _get_numerofa(self):
        return(self._numerofa)
    def _set_numerofa(self):
        newnumerofa=input("nouveau numerofa")
        self._numerofa=newnumerofa
    numerofa=property(_get_numerofa,_set_numerofa)
    
    def _get_date(self):
         return(self._date)
    def _set_date(self):
        newdate=input("jj/mois/anne")
        self._date=newdate
    date=property(_get_date,_set_date)   
        
    def _get_collection(self):
        for achat in self._collection:
            print("la collection d achat est:",achat._Article.design)
        return(achat._Article.design)
    def _set_collection(self,newcolection=[]):
        self._collection=newcolection
        for achat in self._collection:
            print("la nouvelle collection d achat est:",achat._Article.design)
    colection=property(_get_collection,_set_collection)
        
    def Ajouter_achat(self,newarticle):
        for achat in self._collection:
            if achat==newarticle:

                print("error,Article se trouvant deja dans la collection")
        else:
           self._collection.append(newarticle)
    
    def detailsFacture(self):
        print("\nNumero facture:....{}......\t\tDate facture:{}".format(self._numerofa,self._date))
        print("\n\t\tListes des achats\n")
        print("Designation\tRemise\tprix(enDH)\tquantite\tPrix total")
        for achat in self._collection:
            print("{}\t\t.....\t   {}\t\t   {}\t\t   {}".format(achat._Article.design,achat._Article.prix,achat.quantite,(achat._Article.prix*achat.quantite)))
        print("\nle montant total de la facture est:\t",(facture1.montantTotal()))
            
    def __getitem__(self,index):
        print(self._collection[index])
        return(self._collection[index])
    
    def __contains__(self,newachat):
        for achat in self._collection:
            if achat.numero==newachat.numero:
                print("Error article existant deja dans la collection")
                break
            else:
                self._collection.append(newachat)
                
    def montantTotal(self):
        montant_total=0
        for achat in self._collection:
            montant_total+=(achat.quantite)*(achat._Article.prix)
        print("Le montant total de la facture est:",montant_total)
        resultat = StringVar()
        sortie = Label(cadre, textvariable = montant_total)
        resultat.set(eval(montant_total.get()))
        sortie.pack()


def retirer(self,index):
        del(self._collection[index])
        for achat in self._collection:
            print("Les achats restants sont:",achat)
    
            
facture1=Facture(1,"2 juin 2017",[achat1,achat2])#facture1=(1,"2 juin 2017",[(1,(1,"eponge",450,"solide"),4),(4,(4,"savon",3000,"solide"),9))
facture1.Ajouter_achat(achat3)
facture1._set_collection([achat1,achat2])
#facture1.retirer([0])
facture1.Ajouter_achat(achat3)
facture1.montantTotal()
facture1.Ajouter_achat(achat4)

facture1.detailsFacture()
facture1._get_collection()
facture1.__contains__(Achat(1,article1,4))"""


"""import mysql.connector as mysql

database=mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="boutique2"
    )
cursor=database.cursor()
#cursor.execute("CREATE TABLE Article(code INT NOT NULL PRIMARY KEY AUTO_INCREMENT,design VARCHAR(30)NOT NULL,Prix INT NOT NULL,categorie VARCHAR(25) NOT NULL)")
#cursor.execute("CREATE TABLE Facture(numerofa INT NOT NULL PRIMARY KEY AUTO_INCREMENT,date_fa DATETIME,collection VARCHAR(200) NOT NULL)")
#cursor.execute("CREATE TABLE Achat(Numero INT NOT NULL PRIMARY KEY AUTO_INCREMENT,Article VARCHAR(30)NOT NULL,quantite INT NOT NULL,numerofa INT NOT NULL,CONSTRAINT numerofa_fk FOREIGN KEY(numerofa) REFERENCES Facture(numerofa),code INT NOT NULL,CONSTRAINT code_fk FOREIGN KEY(code) REFERENCES Article(code))")


cursor.execute("SHOW TABLES")"""
from tkinter import *
from tkinter.messagebox import showerror,showinfo
import tkinter.font as font

window=Tk()
window.title("Ma Boutique ")
window.geometry("720x360")
window.config(background="#11719e")
#
#fond d ecran de l image
width=800
height=600
image=PhotoImage(file="supermarche.png")
canvas=Canvas(window, width=width,height=height,bg="#031536",bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2, image=image)
canvas.pack(expand=YES)
window.iconbitmap("ico1.ico")

def article():
    class Article:
    
        #creation de la classe article
        def __init__(self,code,designation,prix,categorie,quantite,date,numerofa):
            self._code=code
            self._designation=designation
            self._prix=prix
            self._categorie=categorie
            self._quantite=quantite
            self._date=date
            self._numerofa=numerofa
    liste_art=[]
    def verifie1(liste_art,value):
        for i in range(len(liste_art)):
            if liste_art[i].__eq__(value):
                return False
            else:
                return True
    def Valider():
        if codeEntry.get() and designationEntry.get() and\
           prixEntry.get() and categorieEntry.get() and quantiteEntry.get() and dateEntry.get() and numerofaEntry.get():
            newarticle=Article(codeEntry.get(),designationEntry.get,prixEntry.get(),categorieEntry.get(),\
                               quantiteEntry.get(),dateEntry.get(),numerofaEntry.get())
            if verifie1(liste_art,newarticle):
                showerror(title="Formulaire invalide",message="Article deja Ajouté")


            else:

                """fichier=open("boutique.txt","w")
                fichier.write("Numero facture:   \t")
                fichier.write(str(numerofaEntry.get()))
                fichier.write("\t\t")
                fichier.write("Date facture: \t  ")
                fichier.write(str(dateEntry.get()))
                fichier.write("\n\t\tListes des achats\n")
                fichier.write("Designation\tRemise\tprix(enDH)\tquantite\tPrix total")                    
                fichier.write("\n")
                fichier.write(str(designationEntry.get()))
                fichier.write("\t\t\t")
                fichier.write(str(prixEntry.get()))
                fichier.write("\t\t")
                fichier.write(str(quantiteEntry.get()))
                prix=prixEntry.get()
                quantite=quantiteEntry.get()
                prixtotal=(prix*quantiteEntry.get())
                fichier.write("\t")
                #fichier.write(str(prixtotal))
                fichier.write("\nle montant total de la facture est:\t")
                montant_total=0
                for achat in liste_art:
                    montant_total+=(achat.quantiteEntry.get())*(achat.prixEntry.get())
                
                fichier.write("\t")
                fichier.write(str(montant_total))
                fichier.close()"""
                
                """insert="INSERT INTO Article(code) VALUES(%s)"

                valeurs=(codeEntry.get())

                cursor.execute(insert,valeurs)

                database.commit()"""
                liste_art.append(newarticle)
                showinfo(title="validation reusie",message="Article bien inseré")
                
                fenetre_facture=Toplevel(window)
                fenetre_facture.title("Ma Boutique ")
                fenetre_facture.geometry("720x360")
                fenetre_facture.config(background="#11719e")
                fenetre_facture.iconbitmap("ico1.ico")
                
                facture =Text(fenetre_facture, height = 50,width = 100,fg="white",bg="black",bd=5)
                #img =PhotoImage(file = "panier.png")
                #facture.image_create(END,image=img)
                facture.insert(END,"code")
                facture.insert(END," ")
                facture.insert(END,"designation")
                facture.insert(END," ")
                facture.insert(END,"Prix")
                facture.insert(END," ")
                facture.insert(END,"Categorie")
                facture.insert(END," ")
                facture.insert(END,"Quantite")
                facture.insert(END," ")
                facture.insert(END,"Date")
                facture.insert(END," ")
                facture.insert(END,"Numero_fa")
                facture.insert(END,"\n")
                facture.insert(END,codeEntry.get())
                facture.insert(END,"\t")
                facture.insert(END,designationEntry.get())
                facture.insert(END,"\t")
                facture.insert(END,prixEntry.get())
                facture.insert(END,"\t")
                facture.insert(END,categorieEntry.get())
                facture.insert(END,"\t")
                facture.insert(END,quantiteEntry.get())
                facture.insert(END,"\t")
                facture.insert(END,dateEntry.get())
                facture.insert(END,"\t")
                facture.insert(END, numerofaEntry.get())
                facture.place(x=100,y=200)
        else:
            showerror(title="Formulaire invalide",message="Tous les champs doivent etre renseignés")
        #code=codeEntry.get()
        #designation=designationEntry.get()
        #prix=prixEntry.get()
        #categorie=categorieEntry.get()
    def Annuler():
        code=codeEntry.delete(0,END)
        designation=designationEntry.delete(0,END)
        prix=prixEntry.delete(0,END)
        categorie=categorieEntry.delete(0,END)
        quantite=quantiteEntry.delete(0,END)
        date=dateEntry.delete(0,END)
        numerofa=numerofaEntry.delete(0,END)
    def facture():
  
        facture =Text(window, height = 9,width = 55)
        #img =PhotoImage(file = "panier.png")
        #facture.image_create(END,image=img)
        facture.insert(END,"code")
        facture.insert(END," ")
        facture.insert(END,"designation")
        facture.insert(END," ")
        facture.insert(END,"Prix")
        facture.insert(END," ")
        facture.insert(END,"Categorie")
        facture.insert(END," ")
        facture.insert(END,"Quantite")
        facture.insert(END," ")
        facture.insert(END,"Date")
        facture.insert(END," ")
        facture.insert(END,"Numero_fa")
        facture.insert(END,"\n")
        facture.insert(END,codeEntry.get())
        facture.insert(END,"\t")
        facture.insert(END,designationEntry.get())
        facture.insert(END,"\t")
        facture.insert(END,prixEntry.get())
        facture.insert(END,"\t")
        facture.insert(END,categorieEntry.get())
        facture.insert(END,"\t")
        facture.insert(END,quantiteEntry.get())
        facture.insert(END,"\t")
        facture.insert(END,dateEntry.get())
        facture.insert(END,"\t")
        facture.insert(END, numerofaEntry.get())
        facture.place(x=0,y=200)

    #creation des label
    f = font.Font(family='Freestyle Script', size=22, weight="bold")
    title= font.Font(family='BRUSH', size=22, weight="bold")
    label=Label(text="AJOUT D'ARTICLE",font=("curvy",22),bg="#11719e",fg="white")
    label["font"]=f
    label.place(x=560,y=10)
    labelcode=Label(text="code:",font=("courrier",15),bg="#11719e",fg="white")
    labelcode["font"]=f
    labelcode.place(x=340,y=160)
    labeldesignation=Label(text="designation:",font=("courrier",15),bg="#11719e",fg="white")
    labeldesignation["font"]=f
    labeldesignation.place(x=340,y=230)
    labelprix=Label(text="prix:",font=("courrier",15),bg="#11719e",fg="white")
    labelprix["font"]=f
    labelprix.place(x=340,y=300)
    labelcategorie=Label(text="categorie:",font=("courrier",15),bg="#11719e",fg="white")
    labelcategorie["font"]=f
    labelcategorie.place(x=340,y=370)
    labelquantite=Label(text="Quantite:",font=("courrier",15),bg="#11719e",fg="white")
    labelquantite["font"]=f
    labelquantite.place(x=340,y=440)
    labeldate=Label(text="Date:",font=("courrier",15),bg="#11719e",fg="white")
    labeldate["font"]=f
    labeldate.place(x=340,y=510)
    labelnumerofa=Label(text="Numero_fact:",font=("courrier",15),bg="#11719e",fg="white")
    labelnumerofa["font"]=f
    labelnumerofa.place(x=340,y=580)
    #creation des entrer
    codeEntry=Entry(window,textvariable=IntVar(),width=70)
    codeEntry.place(x=470,y=160)
    designationEntry=Entry(window,textvariable=StringVar(),width=70)
    designationEntry.place(x=470,y=230)
    prixEntry=Entry(window,textvariable=IntVar(),width=70)
    prixEntry.place(x=470,y=300)
    categorieEntry=Entry(window,textvariable=StringVar(),width=70)
    categorieEntry.place(x=470,y=370)
    quantiteEntry=Entry(window,textvariable=IntVar(),width=70)
    quantiteEntry.place(x=470,y=440)
    dateEntry=Entry(window,textvariable=StringVar(),width=70)
    dateEntry.place(x=470,y=510)
    numerofaEntry=Entry(window,textvariable=IntVar(),width=70)
    numerofaEntry.place(x=470,y=580)
    
    
    #boutton image
    #img_btn=PhotoImage(file="bouton.png")    
    #creation button
    buttonvalider=Button(window,text="Valider",font=("courrier",15),bg="white",fg="#11719e",command=Valider)
    buttonvalider.place(x=540,y=640)

    buttonannuler=Button(window,text="Annuler",font=("courrier",15),bg="white",fg="#11719e",command=Annuler)
    buttonannuler.place(x=750,y=640)


"""Creation du Menu principal"""
menuprinci=Menu(window,tearoff=0)

"""Creation des sous-Menus"""

menu_afficher=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Article",menu=menu_afficher)
menu_afficher.add_command(label="Ajouter un article",command=article)
menu_afficher.add_command(label="Listes des articles")

menu_achat=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Achat",menu=menu_achat)
menu_achat.add_command(label="Ajout de vente")
menu_achat.add_command(label="Liste des ventes")

menu_facture=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Facture",menu=menu_facture)
menu_facture.add_command(label="Ajout de vente")
menu_facture.add_command(label="Liste des ventes")


window.config(menu=menuprinci)#configuration finale du Menu principal

window.mainloop()
