# Another math game

import random


def effectuezTest():
    correct = 0
    for i in range(0,10):
        x = random.randint(0,1)
        if x == 0:
            term1 = random.randint(1, 9)
            term2 = random.randint(1, 9)
            result = int(input('{} + {} = '.format(term1, term2)))
            if result == term1 + term2:
                correct = correct + 1
            else:
                print("Incorrect – la reponse est", term1 + term2)

        if x == 1:
            term1 = random.randint(1, 9)
            term2 = random.randint(1, 9)
            result = int(input('{} * {} = '.format(term1, term2)))
            if result == term1 * term2:
                    correct = correct + 1
            else:
                print("Incorrect – la reponse est", term1 * term2)
    print(correct, "reponses correctes.")
    return correct


print("Ce logiciel va effectuez un test avec 10 questions …… ")



y = effectuezTest()

if y >= 6:
    print("Felicitations!")

else:
    print("Demandez à votre enseignant(e) de vous aider.")




