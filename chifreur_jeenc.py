





import random
import unicodedata


cle = {"a":"¤", "b" : ":" }

message = input("quel est le message que vous voulez chiffrer?").lower()

message = unicodedata.normalize("NFD", message)
message = "".join(c for c in message if unicodedata.combining(c) == 0)

resultat = []
for caractere in message:
    if caractere == "e":
        nouveau_symbole = random.choice(["$", "£"])
    else:
        nouveau_symbole = cle.get(caractere, "")
    resultat.append(nouveau_symbole)
resultat = "".join(resultat)

