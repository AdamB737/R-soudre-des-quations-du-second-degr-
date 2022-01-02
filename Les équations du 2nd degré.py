# coding: utf-8
# Crée par Adam B. Ce programme simple permet de résoudre des équation de la forme ax^2+bx+c=0.
#Librairies utilisées:
import math
import fractions
import os
import sys
#Variables:
a=float (fractions.Fraction(input("Veuillez saisir une valeur pour a:")))
b=float (fractions.Fraction(input("Veuillez saisir une valeur pour b:")))
c=float (fractions.Fraction(input("Veuillez saisir une valeur pour c:")))
#Le discriminant noté delta est la formule qu'il y a dans la racine carré:
delta= b**2-4*a*c
#x0 est la formule simplifiée pour trouver la valeur de x si le discriminant est égal à 0:
x0=-b/2*a
#Conditions:
if delta < 0:
    print ("Désolé, il n'éxiste pas de solutions réelles car delta est inférieur à zéro, or on ne peut pas avoir une racine carré d'un nombre négatif")
elif delta==0:
    print ("La solution unique est:","(",x0,")")
else:
    Numerateur1= -b+math.sqrt(delta)
    Numerateur2= -b-math.sqrt(delta)
#Alpha et beta sont les deux fractions qui comportent les numérateurs etles dénominteurs:
    alpha=beta=(Numerateur1)/(2*a)
    beta= (Numerateur2)/(2*a)
    x1= alpha
    x2= beta
    print ("Les solutions sont:","(",format(x1,".4f"),";0)", "et" ,"(",format(x2,".4f"),";0)")
#Redémarrage du scipt:
while True:
    reponse1 = str(input('Voulez-vous relancer le script? (o/n): '))
    if reponse1 != "o" and reponse1 != "n":
        reponse2=str(input("Pour relancer, appuiez sur o (oui) sinon appuyez sur n (non)"))
    if reponse1 == 'o': 
        os.execl(sys.executable, sys.executable, *sys.argv)
    if reponse1=="n":
        print("Merci, à bientôt !")
        break
    reponse2= str(input('Voulez-vous relancer le script? (o/n): '))
    if reponse2=="o":
        os.execl(sys.executable, sys.executable, *sys.argv)
    if reponse2=="n":
        print("Merci, à bientôt !")
        break
    if reponse2 != "o" and reponse2 != "n":
        reponse2=str(input("Pour relancer, appuiez sur o (oui) sinon appuyez sur n (non)"))
#Fin du script, merci !