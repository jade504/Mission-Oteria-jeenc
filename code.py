
from random import choice
import unicodedata

while True: 

    message=""
    choix = [ ]
    choix = input ("vous voulez chiffrer ou dechiffrer un message? (pour arreter, tapez 'quitter') : ").lower()

    messchifrés = "messchifrés.txt"
    mot_de_passe = []

    if choix == ('chiffrer'):

        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*", "e"]
        cle={lettre: symbole for lettre, symbole in zip(alphabet, symboles)}

        message = input("quel est le message que vous voulez chiffrer?")
        message = unicodedata.normalize("NFD", message)
        message = "".join(c for c in message if unicodedata.combining(c) == 0)
        resultat = []
        for caractere in message:
            if caractere == "e":
                nouveau_symbole = choice(["$", "£"])
            else:
                nouveau_symbole = cle.get(caractere, "")
            resultat.append(nouveau_symbole)
        resultat = "".join(resultat)
        message_chiffre = resultat[::-1]
        print("Message chiffré :", message_chiffre)
    
    messchifrés = open("messchifrés.txt", "a")
    messchifrés.write(message_chiffre + "\n")
    messchifrés.close()
    print("Le message chiffré a été enregistré dans le fichier messchifrés.txt.")


    if choix == 'dechiffrer':

        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*","e"]
        cle = {symbole: lettre for symbole, lettre in zip(symboles, alphabet)}

        print("vos chifrements")
        messchifrés = open("messchifrés.txt", "r")
        secretsmesschifrés = [line.strip() for line in messchifrés]
        messchifrés.close()

        for i in range(len(secretsmesschifrés)):
            print(str(i + 1) + ". " + secretsmesschifrés[i])

        choix = int(input("Quel est le message que vous voulez déchiffrer ? ").lower())
        message = int(choix) 
       
        if 1 <= message <= len(secretsmesschifrés):
            selectioné = secretsmesschifrés[message - 1]
    
       
        message_inverse = selectioné[::-1]
        resultat = []
        for caractere in message_inverse:
            if caractere in ("$", "£"):
                resultat.append("e")
            else:
                resultat.append(cle.get(caractere, caractere))

        message_dechiffre = "".join(resultat)
        print("Message déchiffré :", message_dechiffre)

    elif choix == 'quitter':
        print("Au revoir !")
        open("messchifrés.txt", "w").close() 
        break


