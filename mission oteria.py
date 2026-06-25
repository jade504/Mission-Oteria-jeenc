#crée par jeenc
#chiifrement des données
from random import choice, shuffle
import unicodedata

while True:

    message = ""
    choix = input("vous voulez chiffrer ou dechiffrer un message? (pour arreter, tapez 'quitter') : ").lower()

    messchifrés = "messchifrés.txt"
    mot_de_passe = []

    if choix == 'chiffrer':

        alphabet = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", " "]
        symboles = ["¤", ":", ">", "<", "~", "/", ".", "¨", "#", "+", "=", "_", "-", "°", "^", "{", "@", "§", "&", "%",
                    "?", "!", "µ", "²", "*", "e"]

        shuffle(symboles)

        cle = {lettre: symbole for lettre, symbole in zip(alphabet, symboles)}

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

        try:
            with open("messchifrés.txt", "r") as fichier:
                ancien_contenu = fichier.read()
        except FileNotFoundError:
            ancien_contenu = ""

        nouveau_bloc = "".join(symboles) + "\n" + message_chiffre + "\n"

        with open("messchifrés.txt", "w") as fichier:
            fichier.write(nouveau_bloc + ancien_contenu)
        print("Le message chiffré a été enregistré dans le fichier messchifrés.txt.")

    elif choix == 'dechiffrer':

        alphabet = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", " "]

        try:
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

                message_inverse = selectioné[::-1]
                resultat = []
                for caractere in message_inverse:
                    if caractere in ("$", "£"):
                        resultat.append("e")
                    else:
                        resultat.append(cle.get(caractere, caractere))

                message_dechiffre = "".join(resultat)
                print("Message déchiffré :", message_dechiffre)
            else:
                print("Numéro de message invalide.")
        except FileNotFoundError:
            print("Aucun fichier de messages chiffrés trouvé.")

    elif choix == 'quitter':
        print("Au revoir !")
        try:
            open("messchifrés.txt", "w").close()
        except:
            pass
        break