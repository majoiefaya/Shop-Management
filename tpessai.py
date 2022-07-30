
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
facture1.__contains__(Achat(1,article1,4))

