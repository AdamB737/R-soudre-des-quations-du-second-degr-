# Crée par Adam Benaissa. Ce programme simple permet de résoudre des équation de la forme ax^2+bx+c=0.
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
    Numérateur1= -b+math.sqrt(delta)
    Numérateur2= -b-math.sqrt(delta)
#Alpha et beta sont les deux fractions qui comportent les numérateurs etles dénominteurs:
    alpha=beta=(Numérateur1)/(2*a)
    beta= (Numérateur2)/(2*a)
    x1= alpha
    x2= beta
    print ("Les solutions sont:","(",format(x1,".4f"),";0)", "et" ,"(",format(x2,".4f"),";0)")
#Redémarrage du scipt:
while True:
    réponse1 = str(input('Voulez-vous relancer le script? (o/n): '))
    if réponse1 != "o" and réponse1 != "n":
        print("Pour relancer, appuiez sur o (oui) sinon appuyez sur n (non)")
    if réponse1 == 'o': 
        os.execl(sys.executable, sys.executable, *sys.argv)
    if réponse1=="n" or réponse2=="n":
        print("Merci, à bientôt !")
        break
    réponse2= str(input('Voulez-vous relancer le script? (o/n): '))
    if réponse2=="o":
        os.execl(sys.executable, sys.executable, *sys.argv)
#Fin du script, merci !