

from random import choice
import unicodedata

while True: 

    message=""
    choix = [ ]
    choix = input ("vous voulez chiffrer (1) ou dechiffrer (2) un message? (pour arreter, tapez 'quitter') : ").lower()

    messchifrés = "messchifrés.txt"
    mot_de_passe = []

    if choix == ('1'):

        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " ",".",",",";","!",":","?"]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*", "e","a","b","c","d","f"]
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
        demande=input("Voulez-vous enregistrer le message chiffré dans le fichier messchifrés.txt ? (oui/non) : ").lower()
        if demande == "oui":
            messchifrés = open("messchifrés.txt", "a")
            messchifrés.write(message_chiffre + "\n")
            messchifrés.close()
            print("Le message chiffré a été enregistré dans le fichier messchifrés.txt.")
        else:
            print("Le message chiffré n'a pas été enregistré.")

    if choix == '2':

        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " ",".",",",";","!",":","?"]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*", "e","a","b","c","d","f"]
        cle = {symbole: lettre for symbole, lettre in zip(symboles, alphabet)}

        demande2=input("Voulez-vous voir la liste des messages chiffrés enregistrés dans le fichier messchifrés.txt ? (oui/non) : ").lower()
        if demande2 == "oui":
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

        if demande2 == "non":
            selectioné = input("Vous avez choisi de ne pas voir la liste des messages chiffrés. Veuillez entrer le message chiffré que vous souhaitez déchiffrer.")
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
    else :
        choix=input("Choix invalide. Veuillez entrer 'chiffrer', 'dechiffrer' ou 'quitter'.")




        