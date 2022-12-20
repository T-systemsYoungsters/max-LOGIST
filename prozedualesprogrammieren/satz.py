satz = "Am _______ besucht _____ seine Schwester in ____."
print(f"Lückentext: {satz}")
for i in range(3):
    temp=input(f"Wort{i+1}: ")
    l=len(temp)
    satz=satz.replace(" "+l*"_"+" "," "+temp+" ")
    satz=satz.replace(" "+l*"_"+"."," "+temp+".")
    print(satz)