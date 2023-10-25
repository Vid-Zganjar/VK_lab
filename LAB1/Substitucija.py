def fnSubstitucija(cistopis,smer):
    abeceda="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kljuc="OZUDJESIFTRGNPBHAVYWCXQLKM"
    kripta=""
    for char in cistopis:

        if char == " " or char == "." or char == ",":
            codec_char=char

        else:
            lower=0
            if char.islower():
                char=char.upper()
                lower=1
            if smer==1:
                codec_char=kljuc[abeceda.index(char)]
                
            if smer==0:
                codec_char=abeceda[kljuc.index(char)]
            if lower:
                codec_char=codec_char.lower()
        
        kripta+=codec_char
        
    return kripta

print(fnSubstitucija("TE.ST",1))
print(fnSubstitucija("JF.GJ",0))