# Godteri koster 30, og brus koster 20.
# Skriv ut hva bruker kan kjøpe.

penger = int(input("Hvor mye penger har du: "))
godteri = 30
brus = 20

if(penger > brus+godteri):
    print("kjøp godteri OG brus")
elif(penger > godteri):
    print("kjøp godteri")
elif(penger > brus):
    print("kjøp brus")
else:
    print("du har ikke nok penger")
