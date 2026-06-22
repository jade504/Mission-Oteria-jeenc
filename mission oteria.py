fichier="chiffrement.txt"
chiffrement=[]
try :
    with open(fichier,"r") as f :
        fichier=f.read().splitlines()
        pass
except FileNotFoundError:
    print("Ce fichier est vide")
key={"a":"¤","b":":","c":">","d":"<","f":"~","g":"/","h":".","i":"¨","j":"#","k":"+","l":"=","m":"_","n":"-","o":"°","p":"^","q":"{","r":"@","s":"§","t":"&","u":"%","v":"?","w":"!","x":"µ","y":"²","z":"*"}
