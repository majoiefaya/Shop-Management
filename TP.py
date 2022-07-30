
class Article:
    
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
        """resultat = StringVar()
        sortie = Label(cadre, textvariable = montant_total)
        resultat.set(eval(montant_total.get()))
        sortie.pack()"""


"""def retirer(self,index):
        del(self._collection[index])
        for achat in self._collection:
            print("Les achats restants sont:",achat)"""
    
            
facture1=Facture(1,"2 juin 2017",[achat1,achat2])#facture1=(1,"2 juin 2017",[(1,(1,"eponge",450,"solide"),4),(4,(4,"savon",3000,"solide"),9))
facture1.Ajouter_achat(achat3)
facture1._set_collection([achat1,achat2])
#facture1.retirer([0])
facture1.Ajouter_achat(achat3)
facture1.montantTotal()
facture1.Ajouter_achat(achat4)

facture1.detailsFacture()
facture1._get_collection()
facture1.__contains__(Achat(1,article1,4))


from tkinter import *


window=Tk()
window.title("boutique")
window.geometry("1080x720")
window.iconbitmap("ico1.ico")
window.config(background="#ffffff")



def fenetre2():
     fenetre2=Toplevel(window)
     fenetre2.title("facture")
     fenetre2.geometry("1000x600")
     fenetre2.iconbitmap("ico1.ico")
     fenetre2.config(background="#031536")
     def recuperation():
         Numero_achat=Numero_achat2.get()
         Article=Article2.get()
         Quantite=Quantite2.get()
         
         numero_lab=Label(fenetre2,text=Numero_achat,font=("arial",15),bg="#ffffff",fg='black')
         numero_lab.pack(expand=YES,side=LEFT)
         
         Article_lab=Label(fenetre2,text=Article,font=("arial",15),bg="#ffffff",fg='black')
         Article_lab.pack(expand=YES,side=LEFT)
         
         Quantite_lab=Label(fenetre2,text=Quantite,font=("arial",15),bg="#ffffff",fg='black')
         Quantite_lab.pack(expand=YES,side=LEFT)

     frame=Frame(fenetre2,bg="#ffffff")
     frame.pack(expand=YES,pady=25,fill=X)
     
     frame1=Frame(fenetre2,bg="#ffffff")
     frame1.pack(side=TOP)
        
     

     libelle_2=Label(frame ,text= "Numero d achat",font=("Helvetica-serif",20),bg="#ffffff",fg='black')
     libelle_2.pack()
     
     num_Lab=Label(frame,text="Numero_achat",font=("arial",25),bg="#ffffff",fg='black')
     Numero_achat1=StringVar()
     Numero_achat2=Entry(frame,textvariable=Numero_achat1,width=20)
     Numero_achat2.pack()
     
     
     libelle_3=Label(frame ,text= "Article",font=("arial",20),bg="#ffffff",fg='black')
     libelle_3.pack()
     
     Article1=StringVar()
     Article2=Entry(frame,textvariable=Article,width=20)
     Article2.pack()
     
     
     libelle_4=Label(frame ,text= "Quantité de l article",font=("arial",20),bg="#ffffff",fg='black')
     libelle_4.pack()
     
     Quantite1=IntVar()
     Quantite2=Entry(frame,textvariable=Quantite1,width=20)
     Quantite2.pack()
     
    
         
     boutton3=Button(frame,text="Terminer",font=("arial",5),bg='black',fg="#ffffff",command=recuperation)
     boutton3.pack(side=TOP)
     boutton2=Button(fenetre2,text="Details facture",font=("arial",10),bg='#ffffff',fg="black",command=Details_facture)
     boutton2.pack(side=TOP)
     
     
         
    
def Afficher_Article():
            
        fenetre3=Toplevel(window)
       
            
        width=100
        height=100
        image=PhotoImage(file="ico1.png")
        canvas=Canvas(fenetre3, width=width,height=height,bg="#031536",)
        canvas.create_image(width/2,height/2, image=image)
        canvas.pack(expand=YES)

        fenetre3.title("Gestion Vente")
        def recuperation_valeur():
            code=texte1.get()
            design=texte5.get()
            article=texte3.get()
            Quantite=texte4.get()
            

            label1=Label(fenetre3,text=code)
            label1.pack(side=LEFT)

            label2=Label(fenetre3,text=article)
            label2.pack(side=LEFT)

            label3=Label(fenetre3,text=Quantite)
            label3.pack(side=LEFT)

            label4=Label(fenetre3,text=design)
            label4.pack(side=LEFT)

            label5=Label(fenetre3,text="")
            label5.pack(side=LEFT)
            
        fenetre3.geometry("800x600")
        fenetre3.iconbitmap("ico1.ico")
        fenetre3.config(background="#031536")
        
        libelle_1=Label(fenetre3,text= "Création des Articles",font=("arial",10),bg="#ffffff",fg='black',bd=3)
        libelle_1.pack(side=TOP)


        frame=Frame(fenetre3,bg="#ffffff")
        frame.pack(side=LEFT)

        frame1=Frame(fenetre3,bg="#ffffff")
        frame1.pack(side=RIGHT)

        libelle_2=Label(frame ,text= "code",font=("arial",10),bg="#ffffff",fg='black')
        libelle_2.pack()

        var1=IntVar()
        texte1=Entry(frame,textvariable=var1,width=40)
        texte1.pack()

        libelle_3=Label(frame ,text= "Prix",font=("arial",10),bg="#ffffff",fg='black')
        libelle_3.pack()

        var3=StringVar()
        texte3=Entry(frame,textvariable=var3,width=40)
        texte3.pack()

        libelle_4=Label(frame1 ,text= "Désignation",font=("arial",10),bg="#ffffff",fg='black')
        libelle_4.pack()

        var4=IntVar()
        texte4=Entry(frame1,textvariable=var4,width=40)
        texte4.pack()

        libelle_5=Label(frame1 ,text= "Catégorie",font=("arial",10),bg="#ffffff",fg='black')
        libelle_5.pack()

        var5=StringVar()
        texte5=Entry(frame1,textvariable=var5,width=40)
        texte5.pack()

        
        
        boutton1=Button(fenetre3,text="Ajouter Achat",font=("arial",10),bg='#ffffff',fg="black",command=recuperation_valeur)
        boutton1.pack(expand=YES)
        fenetre3.pack()
        

     

def Ajouter_achat():
        fenetre5=Toplevel(window)
        fenetre5.title("facture")
        fenetre5.geometry("1000x600")
        fenetre5.iconbitmap("ico1.ico")
        fenetre5.config(background="#031536")
        libelle_1=Label(fenetre5,text= "Création des Articles",font=("arial",10),bg="#ffffff",fg='black',bd=3)
        libelle_1.pack(side=TOP)

        def get():
            numero_achat=Numero_achat2.get()
            article=Article2.get()
            Quantite=Quantite2.get()
            
            code=text1.get()
            prix=texte3.get()
            design=texte4.get()
            categorie=texte5.get()

            label1=Label(fenetre5,text=numero_achat)
            label1.pack(side=LEFT)

            label2=Label(fenetre5,text=article)
            label2.pack(side=LEFT)

            label3=Label(fenetre5,text=Quantite)
            label3.pack(side=LEFT)
            
        

            label4=Label(fenetre5,text=code)
            label4.pack(side=LEFT)

            label5=Label(fenetre5,text=design)
            label5.pack(side=LEFT)


            label6=Label(fenetre5,text=prix)
            label6.pack(side=LEFT)

            label7=Label(fenetre5,text=categorie)
            label7.pack(side=LEFT)
        frame=Frame(fenetre2,bg="#ffffff")
        frame.pack(expand=YES,pady=25,fill=X)
         
        frame1=Frame(fenetre2,bg="#ffffff")
        frame1.pack(side=TOP)
        
         
        num_Lab=Label(frame,text="Numero_achat",font=("arial",25),bg="#ffffff",fg='black')
        Numero_achat1=StringVar()
        Numero_achat2=Entry(frame,textvariable=Numero_achat1,width=20)
        Numero_achat2.pack()
         
         
        libelle_3=Label(frame ,text= "Article",font=("arial",20),bg="#ffffff",fg='black')
        libelle_3.pack()
         
        Article1=StringVar()
        Article2=Entry(frame,textvariable=Article,width=20)
        Article2.pack()
         
         
        libelle_4=Label(frame ,text= "Quantité de l article",font=("arial",20),bg="#ffffff",fg='black')
        libelle_4.pack()
         
        Quantite1=IntVar()
        Quantite2=Entry(frame,textvariable=Quantite1,width=20)
        Quantite2.pack()
         
        libelle_2=Label(frame1,text= "code",font=("arial",10),bg="#ffffff",fg='black')
        libelle_2.pack()

        var1=StringVar()
        texte1=Entry(frame,textvariable=var1,width=40)
        texte1.pack()

        libelle_3=Label(frame1,text= "Prix",font=("arial",10),bg="#ffffff",fg='black')
        libelle_3.pack()

        var3=StringVar()
        texte3=Entry(frame1,textvariable=var3,width=40)
        texte3.pack()

        libelle_4=Label(frame1 ,text= "Désignation",font=("arial",10),bg="#ffffff",fg='black')
        libelle_4.pack()

        var4=StringVar()
        texte4=Entry(frame1,textvariable=var4,width=40)
        texte4.pack()

        libelle_5=Label(frame1 ,text= "Catégorie",font=("arial",10),bg="#ffffff",fg='black')
        libelle_5.pack()

        var5=IntVar()
        texte5=Entry(frame1,textvariable=var5,width=40)
        texte5.pack()

        
        def Details_facture():
            fenetre1=Toplevel(fenetre5)
            fenetre1.title("facture")
            fenetre1.geometry("1000x600")
            fenetre1.iconbitmap("ico1.ico")
            fenetre1.config(background="#031536")
                               
            import datetime   
            x=datetime.datetime.now()
            heure=(x.strftime("%X"))
            date=(x.strftime("%x"))
            date2=heure,date
            argument1=design,prix,quantite,(prix*quantite)
            text1=Label(fenetre1,text="Numero facture:",font=("arial",15),bg="#ffffff",fg='black')
            text1.pack(side=LEFT)
            text2=Label(fenetre1,text=Numero_achat,font=("arial",15),bg="#ffffff",fg='black')
            text2.pack(side=LEFT)
            text3=Label(fenetre1,text="Date Facture:",font=("arial",15),bg="#ffffff",fg='black')
            text3.pack(side=LEFT)
            text4=Label(fenetre1,text=date2,font=("arial",15),bg="#ffffff",fg='black')
            text4.pack(side=LEFT)
            text4=Label(fenetre1,text=argument1,font=("arial",15),bg="#ffffff",fg='black')
            text4.pack(ipadx=10,ipady=50)
        
             
        boutton3=Button(frame,text="Terminer",font=("arial",5),bg='black',fg="#ffffff",command=recuperation)
        boutton3.pack(side=TOP)
        boutton2=Button(fenetre5,text="Details facture",font=("arial",10),bg='#ffffff',fg="black",command=Details_facture)
        boutton2.pack(side=TOP)
         
        def Ajouter_achat_princi():
            
            
            
  
            self._collection2=[]
            for achat in self._collection2:
                newarticle=Achat(numero_achat,article,Quantite)
                if achat==newarticle:
    
                    print("error,Article se trouvant deja dans la collection")
                else:
                   self._collection2.append(newarticle)
                label5=Label(fenetre5,text=newarticle)
                label5.pack(side=LEFT)
            print(self._collection2)
        
        boutton1=Button(fenetre5,text="Ajouter Achat",font=("arial",10),bg='#ffffff',fg="black",command=Ajouter_achat_princi)
        boutton1.pack(expand=YES)

def fenetre4():

    fenetre4=Toplevel(window)
    fenetre4.title("Consultation")
    fenetre4.geometry("800x600")
    fenetre4.iconbitmap("ico1.ico")
    fenetre4.config(background="#031536")

    frame=Frame(fenetre4,bg='',relief=SUNKEN)

    label_title=Label(frame,text="WELCOME",font=("Helvetica",20),bg="#DAE5E8")
    label_subtitle=Label(frame,text="Ici vous pouvez consulter les differents elements suivant",font=("Arial",25),bg="#DAE5E8")
    label_title.pack(expand=YES)
    label_subtitle.pack(expand=YES)
    frame.pack(expand=YES)

    a_button=Button(frame,text="Montant Total Facture",font=("courrier",10),bg="#DAE5E8",fg="black",command=facture1.montantTotal)
    b_button=Button(frame,text="Details facture",font=("courrier",10),bg="#DAE5E8",fg="black",command=facture1.detailsFacture)
    c_button=Button(frame,text="Afficher l article",font=("courrier",10),bg="#DAE5E8",fg="black",command=article1.afficher1)
    d_button=Button(frame,text="Afficher l achat",font=("courrier",10),bg="#DAE5E8",fg="black",command=achat1.afficher2)
    a_button.pack(expand=YES,pady=25,fill=X)
    b_button.pack(expand=YES,pady=15,fill=X)
    c_button.pack(expand=YES,pady=15,fill=Y)
    d_button.pack(expand=YES,pady=15,fill=Y)
    
def helper():
    fenetre5=Toplevel(window)
    label_title2=Label(fenetre5,text="Ceci est une Application de gestion de boutique vous disposez des onglets suivants",font=("Helvetica",12),bg="#DAE5E8")
    fenetre5.geometry("300x100")
    fenetre5.iconbitmap("ico1.ico")
    fenetre5.config(background="#031536")
    label_title2.pack()
    label_title3=Label(fenetre5,text="Gestion article:Qui vous permet de gerer les differents articles de votre boutiqueGestion vente:\narticle:Qui vous permet de gerer les differentes ventes de votre boutique\nAfficher:Qui vous permet d afficher les differents operations et achats\nEdition:c est le menu edition\nOutil:c est le menu outil\nhelp:fenetre d aide...\nQuitter:pour sortir de l application",font=("Helvetica",12),bg="#DAE5E8")
    label_title3.pack()
                
    #fond d ecran de l image
    width=1000
    height=1000
    image=PhotoImage(file="help.png")
    canvas=Canvas(fenetre5, width=width,height=height,bg="#031536",bd=0, highlightthickness=0)
    canvas.create_image(width/2,height/2, image=image)
    canvas.pack(expand=YES)
    fenetre5.mainloop()             
#configuration de la barre de menu
"""Creation du Menu principal"""
menuprinci=Menu(window,tearoff=0)



"""Creation des sous-Menus"""

menu_afficher=Menu(menuprinci,tearoff=0)

menu_modifier=Menu(menuprinci,tearoff=0)

menu_outil=Menu(menuprinci,tearoff=0)

menu_help=Menu(menuprinci,tearoff=0)

Quitter_menu=Menu(menuprinci,tearoff=0)#Ajout du sous menu Quitter au menu principale

Article_menu=Menu(menuprinci,tearoff=0)#Ajout du sous Article_menu au menu principale

vente_menu=Menu(menuprinci,tearoff=0)#Ajout du sous vente_menu au menu principale
#***************************************************************************************
"""creation des references des differents menu sur l interface graphique"""

menuprinci.add_cascade(label="Gerer une vente",menu=vente_menu)#Creation du menu vente_menu sur l interface graphique avec pour nom "Gerer une vente"

menuprinci.add_cascade(label="Gerer un Article",menu=Article_menu)#Creation du menu vente_menu sur l interface graphique avec pour nom "Gerer un article"

menuprinci.add_cascade(label="Afficher",menu=menu_afficher)

menuprinci.add_cascade(label="Edition",menu=menu_modifier)

menuprinci.add_cascade(label="Outil",menu=menu_outil)

menuprinci.add_cascade(label="help",menu=menu_help)

menuprinci.add_cascade(label="Quitter l application",menu=Quitter_menu)#Creation du menu vente_menu sur l interface graphique avec pour nom "Quitter l application"

#*************************************************************************************************************

""""Ajout des commandes"""
Quitter_menu.add_command(label="Quitter",command=window.quit)#Ajout de la commande Quitter au sous menu Quitter

Article_menu.add_command(label="Article",command= Afficher_Article)#Ajout de la commande Afficher_Article au sous menu Article


vente_menu.add_command(label="Vente",command=fenetre2)#Ajout de la commande ouvrir fenetre2  au sous menu Article


menu_afficher.add_command(label="Afficher article",command=article1.afficher1)

menu_afficher.add_command(label="Afficher l achat",command=Ajouter_achat)

menu_afficher.add_command(label="details Facture",command=fenetre4)

menu_help.add_command(label="Fenetre d aide",command=helper)

#********************************************************************************************************

#fond d ecran de l image
width=1000
height=1000
image=PhotoImage(file="supermarche.png")
canvas=Canvas(window, width=width,height=height,bg="#031536",bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2, image=image)
canvas.pack(expand=YES)
#*****************************************************************************************************************





window.config(menu=menuprinci)#configuration finale du Menu principal

window.mainloop()#creation de la fenetre principale window

