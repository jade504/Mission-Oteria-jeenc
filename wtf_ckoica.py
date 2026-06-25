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
            with open("messchifrés.txt", "r") as fichier:
                ancien_contenu = fichier.read()
       
        nouveau_bloc = "".join(symboles) + "\n" + message_chiffre + "\n"

        with open("messchifrés.txt", "w") as fichier:
            fichier.write(nouveau_bloc + ancien_contenu)
        print("Le message chiffré a été enregistré dans le fichier messchifrés.txt avec la clé de dechifrement.")

    if choix == '2':

       

        demande2 = input("Voulez-vous voir la liste des messages sauvegardés ? (oui/non) : ").lower()

        if demande2 == "oui":

            with open('messchifrés.txt', 'r') as fichier:
                lignes = [line.strip() for line in fichier if line.strip()]

            if not lignes or len(lignes) % 2 != 0:
                print("Le fichier est vide ou corrompu.")
                continue

            nombre_messages = len(lignes) // 2
            for i in range(nombre_messages):
                msg_chiffre = lignes[(i * 2) + 1]
                print(str(i + 1) + ". " + msg_chiffre)

            choix_message = int(input("Quel est le numéro du message que vous voulez déchiffrer ? "))

            if 1 <= choix_message <= nombre_messages:
                index_cle = (choix_message - 1) * 2
                index_msg = index_cle + 1

                symboles_sauvegardes = lignes[index_cle]
                selectioné = lignes[index_msg]

                cle = dict(zip(symboles_sauvegardes, alphabet))


            else:
                print("Numéro invalide.")
                continue

        elif demande2 == "non":

             # Reconvertit la clé collée en vrai dictionnaire, puis l'inverse (symbole → lettre)
            cle = ast.literal_eval(input("Entrez votre clé de chiffrement : "))
            cle = {v: k for k, v in cle.items()}

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













