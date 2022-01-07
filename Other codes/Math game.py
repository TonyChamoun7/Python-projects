# math game

import random

def effectuezTest(x):
    correct = 0
    if x == 0:
        print("SVP donnez les reponses aux additions suivantes:")
        for i in range(0,10):
            term1 = random.randint(1,9)
            term2 = random.randint(1,9)
            result = int(input('{} + {} = '.format(term1, term2)))
            if result == term1 + term2:
                correct = correct + 1
            else:
                print("Incorrect – la reponse est", term1 + term2)
        print(correct, "reponses correctes.")
        return correct
    if x == 1:
        print("SVP donnez les reponses aux multiplications suivantes:")
        for i in range(0,10):
            term1 = random.randint(1,9)
            term2 = random.randint(1,9)
            result = int(input('{} x {} = '.format(term1, term2)))
            if result == term1 * term2:
                correct = correct + 1
            else:
                print("Incorrect – la reponse est", term1 * term2)
        print(correct, "reponses correctes.")
        return correct

print("Ce logiciel va effectuez un test avec 10 questions …… ")
print("SVP choisissez l'operation 0) Addition 1) Multiplication (0 ou 1): ")
x = int(input())

y = effectuezTest(x)

if y >= 6:
    print("Felicitations!")

else:
    print("Demandez à votre enseignant(e) de vous aider.")

            
    
