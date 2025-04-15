""" Projet 5 JeuDevin.py Version 4 (finale)
"""

import random
INVITE = 'Propose un nombre : '

# NOUVELLES CONSTANTES
QUITTER    = -1
QUIT_TXT   = 'q'
QUIT_MSG = 'Merci pour tout !'
QUIT_CONFIRMER = "Es-tu certain de vouloir quitter (O/n) ?"

#NOUVELLE FONCTION POUR CONFIRMER QU'ON VEUT QUITTER
def confirmer_quitter():
    """On sort seulement si saisie de la
    lettre n minuscule par renvoi de la False. """
    confi = input(QUIT_CONFIRMER)
    if confi == 'n':
        return False
    else:
        return True

def jouer_tour():
    """ Choix d'un nombre, demande au joueur de le
    trouver et reboucle tant qu'il ne l'a pas. """
    nbr_secret = random.randint(1,100)
    nbr_saisies = 0                               #AJOUT
    while True:
        nbr_joueur = input(INVITE)
        # AJOUT BLOC IF POUR SORTIE CONFIRMER
        if nbr_joueur == QUIT_TXT:                #AJOUT
            if confirmer_quitter():               #AJOUT
                return QUITTER                    #AJOUT
            else:
                continue # Tour de boucle suivant #AJOUT
        nbr_saisies = nbr_saisies + 1             #AJOUT
        if nbr_secret == int(nbr_joueur):
            print('Correct !')
            return nbr_saisies                    #MODIF
        elif nbr_secret > int(nbr_joueur):
            print('Trop petit')
        else:
            print('Trop grand')

# Section PRINCIPALE MAIN
total_tours   = 0                     #AJOUT
total_saisies = 0                     #AJOUT
msg_stat = 0

while True:
    total_tours = total_tours + 1                        #AJOUT
    print("Onpasse au tour " +str(total_tours))          #MODIF
    print("En avant pour les devinettes !")              #AJOUT
    
    ce_tour = jouer_tour()

    #AJOUT BLOC IF POUR TESTER SI QUITTER
    if ce_tour == QUITTER:                               #AJOUT
        total_tours = total_tours -1                     #AJOUT
        if total_tours == 0:                             #AJOUT
            msg_stat = "1er tour pas fini ! " +\
                    " Tu veux recommencer ?"             #AJOUT
        else:                                            #AJOUT
            moy = str(total_saisies / float(total_tours)) #A
            msg_stat = "Tu as fait " + str (total_tours) +\
                       " tours. Moyenne de " + str(moy)  #AJOUT
        break                                            #AJOUT
    

    total_saisies = total_saisies + ce_tour          
    print("Tu as fait "+str(ce_tour) + "saisies. ")  
    moy = str(total_saisies / float(total_tours))    
    print("Ta moyenne de saisies/tours = " + moy)    
    print("")

#AJOUT MESSAGE DE SORTIE
print(QUIT_MSG)
print(msg_stat)

