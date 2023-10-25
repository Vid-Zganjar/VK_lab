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


def fnVigenere(cistopis,kljuc,smer):
    i=0
    kripta=""
    for char in cistopis:
    
        kljuc_N=ord(kljuc[i])-ord("A")
        if smer==0:
            kljuc_N=-kljuc_N
        i=i+1
        i=i%len(kljuc)
        codec_char=fnCezar(char,kljuc_N,1)
        kripta+=codec_char
    return kripta
   
print(fnVigenere("OHVIWYXIEIRQAICEIVGSFZTYBRGYZNTEMHMDNXNZHAVBVGWUMZXKOMMLDNXNGWKDEJBTAGOEIJCNXICRRGSKXIGUSJL","VARNOST",0))
