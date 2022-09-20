# datatyper: string, int, float og bool
# lag en av hver datatype
tekst = "min tekst"
tekst2 = "2"
tall = 3
komma = 2.3127637
print(int(tekst2) + tall)
print(type(tall + komma))

sann = True
usant = False

# legge sammen to tall fra bruker, og gjøre om
#til streng igjen og skrive ut

tekst1 = input("Skriv inn ett tall: ")
tekst2 = input("Skriv inn enda ett tall: ")

print(tekst1, "+", tekst2, "=", int(tekst1)+int(tekst2))