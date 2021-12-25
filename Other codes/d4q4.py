

# Ce programme nettoye une liste

def read_raw(file):
    '''str->list of str
    Renvoie une liste de chaînes qui ont été stockées dans un fichier.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str
    La fonction prend en entrée une liste de caractères.
    Elle renvoie une nouvelle liste contenant les mêmes caractères que l
    sauf que un de chaque caractère apparaissant un nombre impair de fois
    dans l est supprimé et tous les caractères * sont supprimés 

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''

    
    # renvoie une nouvelle liste contenant les mêmes caractères que l
    # sauf que un de chaque caractère apparaissant un nombre impair de fois dans l est supprimé
    clean_board= []

    clean = sorted(l)
    y = 0
    for ch in clean:
        x = clean.count(ch)
        if ch =='*': # Si l'élément est *,on continue
            continue
        if ch != y:
            if x % 2 == 0: #Si l'élément est paire on l'enleve
                for i in range(0,x):
                    clean_board.append(ch)
            else:
                for i in range(0, x-1): #On renvoie les éléments apparaissant un nombre impair de fois
                    clean_board.append(ch)
        y = ch
        
    
    return clean_board #retourne la valeur
    


def  is_rigorous(l):
    '''list of str->bool
    Renvoie True si chaque caractère de la liste apparaît exactement 2 fois ou si la liste est vide.
    Sinon, elle renvoie False. 
    
    Précondition: vous pouvez supposer que chaque élément de la liste apparaît un nombre pair de fois
    (c'est-à-dire que la liste est nettoyée par la fonction clean_up)
    >>>  is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>>  is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    
    value = False #Initialize value
    for ch in l: #for loop
        x = l.count(ch) #compte combien du meme element apparait dans la liste
        if x == 2: #Si chaque caractere apparaît exactement 2 fois, on renvoie true
            value = True
        else: #Sinon, on envoie false
            return False
    if l == []: # Si la liste est vide, on retourne true
        return True
    return value #retourne la valeur
            

    
#programme principal
file=input("Entrer le nom du fichier: ")
file=file.strip()
b=read_raw(file)
print("\nAvant clean-up:\n", b)
b=clean_up(b)
print("\nAprès clean-up:\n", b)
if is_rigorous(b):
    print("\nCette liste est maintenant rigoureuse; elle n’a aucun * et elle a "+str(len(b))+" caractères.")
else:
    print("\nCette liste n’a aucun * mais n'est pas rigoureuse et a "+str(len(b))+" caractères.")
     
