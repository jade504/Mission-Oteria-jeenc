

import random
import unicodedata

cle={"a":"¤","b":":","c":">","d":"<","f":"~","g":"/","h":".","i":"¨","j":"#","k":"+","l":"=","m":"_","n":"-","o":"°","p":"^","q":"{","r":"@","s":"§","t":"&","u":"%","v":"?","w":"!","x":"µ","y":"²","z":"*"}

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

message = message.replace(" ", "e")


message_chiffre = resultat[::-1]
print("Message chiffré :", message_chiffre)