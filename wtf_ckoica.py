#crée par jeenc
#chiffrement de données

from random import choice, shuffle
import unicodedata
import ast  # utilisé pour reconvertir la clé (texte) en dictionnaire

while True: 

    message = ""
    choix = input("Vous voulez chiffrer (1) ou dechiffrer (2) un message? (pour arreter, tapez 'quitter') : ").lower()

    if choix == '1':

        # Associe chaque lettre à un symbole aléatoire
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",",",";","!",":","?"]
        symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*","a","b","c","d","f"]
        shuffle(symboles)  # clé différente à chaque fois
        cle = {lettre: symbole for lettre, symbole in zip(alphabet, symboles)}

        message = input("Quel est le message que vous voulez chiffrer ? ")
        # Supprime les accents (é → e, à → a, etc.)
        message = unicodedata.normalize("NFD", message)
        message = "".join(c for c in message if unicodedata.combining(c) == 0)

        resultat = []
        for caractere in message:
            if caractere == " ":
                nouveau_symbole = "e"                     # les espaces sont cachés en 'e'
            elif caractere == "e":
                nouveau_symbole = choice(["$", "£"])      # le vrai 'e' devient $ ou £ aléatoirement
            else:
                nouveau_symbole = cle.get(caractere, "")
            resultat.append(nouveau_symbole)

        # On inverse le résultat pour ajouter une couche de chiffrement
        message_chiffre = "".join(resultat)[::-1]
        print("Message chiffré :", message_chiffre)

        demande = input("Voulez-vous enregistrer le message ? (oui/non) : ").lower()
        if demande == "oui":
            with open("messchifrés.txt", "a") as f:
                f.write(message_chiffre + "\n")
            print("Message enregistré ! Voici votre clé :", cle)  # l'utilisateur doit sauvegarder la clé
        else:
            print("Message non enregistré. Voici votre clé :", cle)

    if choix == '2':

        # Reconvertit la clé collée en vrai dictionnaire, puis l'inverse (symbole → lettre)
        cle = ast.literal_eval(input("Entrez votre clé de chiffrement : "))
        cle = {v: k for k, v in cle.items()}

        demande2 = input("Voulez-vous voir la liste des messages sauvegardés ? (oui/non) : ").lower()

        if demande2 == "oui":
            with open("messchifrés.txt", "r") as f:
                secretsmesschifrés = [line.strip() for line in f if line.strip()]

            for i in range(len(secretsmesschifrés)):
                print(str(i + 1) + ". " + secretsmesschifrés[i])

            message = int(input("Quel est le message que vous voulez déchiffrer ? "))

            if 1 <= message <= len(secretsmesschifrés):
                selectioné = secretsmesschifrés[message - 1]
            else:
                print("Numéro invalide.")
                continue

        elif demande2 == "non":
            selectioné = input("Entrez le message chiffré : ")

        # On inverse d'abord, puis on décode chaque symbole
        message_inverse = selectioné[::-1]
        resultat = []
        for caractere in message_inverse:
            if caractere == "e":
                resultat.append(" ")        # 'e' était un espace caché
            elif caractere in ("$", "£"):
                resultat.append("e")        # $ ou £ était un vrai 'e'
            else:
                resultat.append(cle.get(caractere, caractere))

        print("Message déchiffré :", "".join(resultat))

    elif choix == 'quitter':
        print("Au revoir !")
        open("messchifrés.txt", "w").close()  # efface les messages sauvegardés à la fermeture
        break


