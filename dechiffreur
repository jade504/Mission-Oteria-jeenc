alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
symboles = ["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*", "e"]

cle={symbole: lettre for lettre, symbole in zip(alphabet, symboles)}

message = input("quel est le message que vous voulez dechiffrer?").lower()


resultat = []
for caractere in message:
    if caractere == "$" or caractere == "£":
           nouveau_symbole = "e"
    else:
        nouveau_symbole = cle.get(caractere, "")
    resultat.append(nouveau_symbole)
resultat = "".join(resultat)
message_dechiffre = resultat[::-1]

print("message_dechiffre :", message_dechiffre)
