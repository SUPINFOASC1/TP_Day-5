from random import randint

"""crée une fonction avec deux paramètres nbColors et nbPawns initialisés respectivement à 6 et 4 qui va
 retourne un chiffre aléatoire entre 1 et 6 à chaque fois que le nombre "1" apparaît dans les pions du jeu"""

def initCache(nbColors=6,nbPawns=4):

    return [randint(1,nbColors) for i in range(nbPawns)]



def choose(nbColors=6,nbPawns=4):

    nocorrect = True

    while nocorrect:

        nocorrect = False  
        #tant que nocorrect est faux, la boucle propose à l'utilisateur de rentrer une suite de couleur.

        selected = input('Input your proposal: ')

        if len(selecte) == nbPawns: 
            #si le nombre de la proposition est le même que la quite de pions,alors à x est attribué la proposition de l'utilisateur.

            selected = [int(x) for x in list(selected)]

            for x in selected:  
                #pour x dans proposition, si x est inférieur à 1 ou x supérieur à nbColors, alors nocorrect devient vrai(True)

                if (x<1) or (x>nbColor):

                    nocorrect = True

        else:
            #si le nombre proposition est différent de nbPawns, nocorrect est égal à Vrai

            nocorrect = True

    return selected

 



def evaluation(selected,cache): #créer une fonction "evaluation" à deux paramètres(selected et cache)

    WellPut = 0 
#crée deux variables WellPut et Misplaced initialisés à 0 
    Misplaced = 0

    copySelected,copyCache = list(selected),list(cache) 

    for i in range(len(cache)):
        #pour le nombre de i dans len(cache) et le nombre de j, si copyslected et copycache sont égaux, 
        # alors Wellput gagne 1 ou Misplaced gagne 1 sinon copyslected et copycache retournent à -1

        if copySelected[i] == copyCache[i]:

            WellPut += 1

            copySelected[i],copyCache[i] = -1,-1

    for i in range(len(cache)):

        for j in range(len(cache)):

            if (copySelected[i] == copyCache[j]) and (copySelected[i] != -1):

                Misplaced += 1

                copySelected[i],copyCache[j] = -1,-1

    return WellPut,Misplaced

 

#créer une focntion qui affiche le nombre de couleurs bonnes et fausses dans la séquence

def display(well,bad):

    print(well,"well spot and",bad,"bad ",'\n')

 



def displayCache(cache):
#défini la fonction affichage cache.
    for x in cache:

        print(x,end='')

 



def gameParameters():
#défini les paramètres de jeux: le nombre de couleurs, la longueur de la séquence et le nombre d'essais.
    nbC = int(input('Input the number of colors: '))

    nbP = int(input(' Enter the length of the sequence to guess: '))

    nbTry = int(input(' Enter the number of trials: '))

    return nbC,nbP,nbTry

 

"""Give a name and make comments"""

def master():
#défini ules conditions de gagne ou de perte de la partie

    nbC,nbP,nbTry = gameParameters()

    cache = initCache(nbC,nbP)

    notFound = True

    tries = 1

    print()

    while notFound and (tries<=nbTry):
        #si l'utilisateur a gagné, aucun essais sont disponibles possible, sinon tries +=1

        print('try',tries)

        well,bad = evaluation(chose(nbC,nbP),cache)

        display(well,bad)

        if well == nbP:

            notFound = False

        else:

            tries += 1

    if tries ==nbTry+1:

        print("lost, we had to find:",end=' ')

        displayCache(cache)

    else:

        print("Congratulations, you have found well:", end=' ')

        displyCache(cache)

 



def chooseGame(S,possibles,results,tries):

    if tries==1:
        

        return [1,1,2,2]

    elif len(S)==1:

        return S.pop()

    else:

        return max(possibles, key=lambda x: min(sum(1 for p in S if evaluation(p,x) != res) for res in results))

 



def chooseGameBis(S,possibles,results,tries):

    if tries ==1:

        return [1,1,2,2]

    elif len(S)==1:

        return S.pop()

    else:

        Max = 0

        for x in possibles:

            Min = 1297

            for res in results:

                nb = 0

                for p in S:

                    if evaluation(p,x)!=res:

                        nb+=1

                if nb<Min:

                    Min=nb

            if Max<Min:

                Max = Min

                xx = x

        return xx

                


def game():

    nbC,nbP = 6,4

    cache = initCache(nbC,nbP)

    notFound = True

    tries = 1

    S = set((x,y,z,t) for x in range(1,7) for y in range(1,7) for z in range (1,7) for t in range(1,7))

    possible = frozenset(S)

    results = frozenset((well,bad) for well in range(5) for bad in range(5-well) if not (well==3 and bad==1))

    while notFound and (tries<=10):

        print('try',tries)

        selected = chooseGameBis(S,possible, results,tries)

        print('computer proposal: ',end='')

        displayCache(selected)

        print()

        well,bad = evaluation(selected,cache)

        display(well,bad)

        if well ==nbP:

            notFound = False

        else:

            tries +=1

            S.difference_update(set(coup for coup in S if (well,bad) != evaluation(coup,selected)))

    if tries == 11:

        print("lost, we had to find:",end=' ')

        displyCache(cache)

    else:

        print("He is strong, he found", end=' ')

        displayCache(cache)
#si l'utilisateur a perdu, message d'erreur s'affiche. S'il a gagné le message de la partie gagné s'affiche.
               

#Appelle la fonction game et lance le jeu

game()

