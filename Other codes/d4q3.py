

#Ce programme affiche les nombres cubes entre 100 et 499

print('Les nombres cubes sont :') #Affiche message
for i in range(100,500): #for loop entre 100 et 499
    num = str(i) #Convertis i en un string
    a = int(num[0]) # a = premier chiffre du nombre
    b = int(num[1]) # b = deuxieme chiffre du nombre
    c = int(num[2]) # c = troisieme chiffre du nombre
    ap = a**3 # ap = a^3
    bp = b**3 # bp = b^3
    cp = c**3 # cp = c^3
    tot = ap + bp + cp #tot = a^3 + b^3 + c^3
    if i == tot: # si le nombre dans le for range = tot
        print(i, "=", a, "**3 +", b, "**3 +", c, "**3 =", ap, "+", bp, "+", cp) #Affiche nombre cubes
