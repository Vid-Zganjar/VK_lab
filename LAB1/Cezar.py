

def fnCezar(cistopis,kljuc,razd):
    kripta=""
    if razd:
        for i in cistopis:
            if i.islower():
                  crka=chr((ord(i)-ord('a')+kljuc)%26+ord('a'))
            elif i.isupper():
                  crka=chr((ord(i)-ord('A')+kljuc)%26+ord('A'))
            elif i.isnumeric():
                  crka=chr((ord(i)-ord('0')+kljuc)%10+ord('0')) 

            kripta +=crka
    else:
        for i in cistopis:
            crka=chr(((ord(i))-32+kljuc)%95+32)
            kripta +=crka
    return kripta

Sporocilo="l#,9b-zz|9g~1.)(9$~9(z*)0~}z&9%)(~|9-0~.z94z9&~.)9KIOIG"

#print("Sporocilo: ",enCezar(fnCezar(Sporocilo,2),2))
for kluc in range(96):
  print("Kripta: " ,kluc,fnCezar(Sporocilo,-kluc,0))

     
