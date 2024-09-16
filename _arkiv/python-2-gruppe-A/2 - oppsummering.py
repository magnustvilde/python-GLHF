# bruk operatoren and
# sann = ((True and False) and True) and True
# -> False

# bruk operatoren or
# ny = (4 > 5) or False
# endaEn = (6 >= 6) or False
# print(sann)
# print(ny)
# print(endaEn)

# # bruk operatoren not
# print(not(not False))
# print(not True)

# sett sammen flere operatorer


# lag en variabel som representerer alder, og lag en boolsk variabel
#trafikaltGrunnkurs. Lag forskjellige kombinasjoner, der du skriver
#hva man kan gjøre med de forskjellige kombinasjonene
#(kjøpe alkohol, ta førerkortet, lærekjøre, etc)
alder = 16
traf = False
if (alder >= 16) and traf:
    print('Du kan lærekjøre.')
elif(alder < 16):
    print('Du er ikke gammel nok')
elif((alder >= 16) and not traf):
    print('Du mangler traf')
else:
    print('Lykke til!')