# Oppgave:
'''
1. Hent inn navnet til bruker. Hent inn tre forskjellige tall fra bruker. De to første
    skal være heltall (integer), det siste skal være et flyttall (float).

2. Lag en variabel der de to heltallene tallene blir addert,
    og så delt på det siste tallet.

3. Print ut igjen en beskrivende tekst til brukeren.
'''

navn = input('Navn: ')
tall1, tall2, tall3 = int(input('Tall1: ')), int(input('Tall2: ')), float(input('Tall3: '))
regnestykke = (tall1+tall2)/tall3
print(type(regnestykke))
print(f'({tall1} + {tall2}) / {tall3} = {regnestykke}' )