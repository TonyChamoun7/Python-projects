

# Ce programme affiche la plus longue séquence d’éléments consécutifs égaux selon l'entrer de l'usager

def sequenceMax(chaine): # fonction pour trouver la plus longue séquence d’éléments consécutifs égaux
    sequence = 1 #initialize les variables
    maxsequence = 1
    b = chaine[0] #b = premiere element dans la liste
    for i in range(1,len(chaine)): # for loop de 1 a la longeur de la liste
        c = chaine[i] # c = element dans la liste
        if b == c: #si b = c
            sequence += 1 #sequence devient sequence + 1
        if sequence > maxsequence: #si sequence est plus grand que maxsequence
            maxsequence = sequence #maxsequence devient sequence
        if b!= c: # si b n'egale pas c
            sequence = 1 #sequence est 1
        b = c #b devient la valeur de c
    return maxsequence #retourne maxsequence
                
        
#Usager entre des nombres séparés par des virgules
chaine = input(" Veuillez entrer une liste d'entiers séparées par des virgules: " ).split(',') 

print(sequenceMax(chaine)) #Affiche le résultat
