from random import choice, random
import unicodedata

while True: 
    choix = input("Vous voulez chiffrer ou dechiffrer un message? (pour arreter, tapez 'quitter') : ").lower()

    if choix == 'chiffrer':

        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*", "e"]
        cle = {lettre: symbole for lettre, symbole in zip(alphabet, symboles)}

        message = input("Quel est le message que vous voulez chiffrer ? ")
        message = unicodedata.normalize("NFD", message)
        message = "".join(c for c in message if unicodedata.combining(c) == 0)

        resultat = []
        for caractere in message:
            if caractere == "e":
                nouveau_symbole = choice(["$", "£"])
            else:
                nouveau_symbole = cle.get(caractere, "")
            resultat.append(nouveau_symbole)

        message_chiffre = "".join(resultat)[::-1]
        print("Message chiffré :", message_chiffre)

        with open("messchifrés.txt", "a") as f:  
            f.write(message_chiffre + "\n")
        print("Message sauvegardé !")

    elif choix == 'dechiffrer':

        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*","e"]
        cle = {symbole: lettre for symbole, lettre in zip(symboles, alphabet)}

        try:
            with open("messchifrés.txt", "r") as f:
                secretsmesschifrés = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("Aucun message sauvegardé pour l'instant. Chiffrez d'abord un message !")
            continue

        if len(secretsmesschifrés) == 0:
            print("La liste est vide !")
            continue

        print("Vos messages chiffrés :")
        for i in range(len(secretsmesschifrés)):
            print(str(i + 1) + ". " + secretsmesschifrés[i])

        message = int(input("Quel est le message que vous voulez déchiffrer ? "))

        if 1 <= message <= len(secretsmesschifrés):
            selectioné = secretsmesschifrés[message - 1]
            message_inverse = selectioné[::-1]

            resultat = []
            for caractere in message_inverse:
                if caractere in ("$", "£"):
                    resultat.append("e")
                else:
                    resultat.append(cle.get(caractere, caractere))

            print("Message déchiffré :", "".join(resultat))

        else:
            print("Numéro invalide.")

    elif choix == 'quitter':
        print("Au revoir !")
        break

    else:
        print("Choix invalide, tapez 'chiffrer', 'dechiffrer' ou 'quitter'.")