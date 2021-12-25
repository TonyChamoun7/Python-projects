# Returns amount of positive numbers in a list

def compte_positifs(x):
   y = len(x)
   counter=0
   for i in range(0,y):
       b = int(x[i])
       if b >=0:
           counter = counter + 1
   return counter


print("Veuillez entrer une liste de valeurs séparées par des virgules: ")
x = input().split(',')
print(compte_positifs(x))
