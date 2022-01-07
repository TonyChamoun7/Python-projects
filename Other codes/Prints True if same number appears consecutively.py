
# Prints True if same number appears consecutively


def sequenceDeDeux(x):
    a = len(x)
    b = x[0]
    consecutif = False
    for i in range(1,a):
        c = x[i]
        if b ==c:
            consecutif = True
        else:
            b = c
    if consecutif == True:
        return print("True")
    else:
        return print("False")


x = input("Veuillez entrer une liste de valeurs séparées par des virgules: ").split(",")

sequenceDeDeux(x)
