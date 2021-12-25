

# Ce programme trouve le nombre d'éléments de la liste qui sont divisibles par un entier selon l'entrer de l'usager


def nombre_divisible(liste,n): #Fonction pour trouver le nombre d'éléments de la liste qui sont divisibles par n
    compteur = 0 #initialize compteur
    for i in range(0,len(liste)): #for loop de 0 a la longeur de la liste
        if int(liste[i]) % n == 0: # si le nombre dans la liste est divisible par l'entier
            compteur += 1 # compteur augmente de 1
    return compteur # retourne valeur de compteur



n = int(input('SVP, Entrez un entier : ')) #Usager entre un entier

#Usager entre une liste de valeurs séparées par des virgules
liste = input('Veuillez entrer une liste des valeurs séparées par des virgules: ').split(',')

#Affiche le résultat
print("Le nombre d'élements divisibles par", n, "dans la liste est :", nombre_divisible(liste,n))
