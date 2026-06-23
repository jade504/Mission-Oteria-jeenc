#dechiffrage
symbole=["¤",":",">","<","~","/",".","¨","#","+","=","_","-","°","^","{","@","§","&","%","?","!","µ","²","*","e"]
alphabet=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
cle = dict(zip(alphabet, symbole))
print(cle)
#cle={"a":"¤","b":":","c":">","d":"<","f":"~","g":"/","h":".","i":"¨","j":"#","k":"+","l":"=","m":"_","n":"-","o":"°","p":"^","q":"{","r":"@","s":"§","t":"&","u":"%","v":"?","w":"!","x":"µ","y":"²","z":"*"}


message_chiffre = input("Quel est le message que vous voulez déchiffrer ?")

resultat = []
for caractere in message_chiffre :
    if caractere == "$" or "£" :
        nouveau_symbole = "e"
    else :
        nouveau_symbole = cle.get(caractere,"")
    resultat.append(nouveau_symbole)
resultat = "".join(resultat)
message_dechiffre = resultat[::-1]

print ("Message déchiffré :", message_chiffre)
