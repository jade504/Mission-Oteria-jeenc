from random import random
import unicodedata

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*", "e"]

cle={symbole: lettre for lettre, symbole in zip(alphabet, symboles)}

message=""
choix = [ ]
choix = input ("vous voulez chiffrer ou déchiffrer un message? (chiffrer/déchiffrer) : ").lower()
if choix == 'chiffré':
    message = input("quel est le message que vous voulez chiffrer?")
      
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
    message: str = message.replace(" ", "e")


    message_chiffre = resultat[::-1]
    print("Message chiffré :", message_chiffre)


elif choix == 'déchiffré':
    message = input("quel est le message que vous voulez déchiffrer?")

    resultat = []
    for caractere in message:
        if caractere == "$" or caractere == "£":
           nouveau_symbole = "e"
        else:
             nouveau_symbole = cle.get(caractere, "")
    resultat.append(nouveau_symbole)
    resultat = "".join(resultat)
    message_dechiffre=resultat[::-1]

print("message_dechiffre :", message_dechiffre)