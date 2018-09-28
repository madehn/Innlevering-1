#Oppgave 1


import math 
#Importerer matteliste for å kunne bruke log senere
print(" ")
print("Hvor mange H+ ioner er det i mol/liter?")
print("a*10^b")
#Spør brukeren hvor mange H+ ioner det er og på hvilken form det skal skrives inn på

a=int(input("a="))
b=int(input("b="))
pH=-(math.log10(a*(10**b)))
#Input på de to verdiene og formelen for å regen ut pH

if 0<=pH<7:
    print("pH-verdien er",pH,"Løsningen er sur!")
elif pH==7:
    print("pH-verdien er", pH, "Løsningen er nøytral!")
elif 14>=pH>7:
    print("pH-verdien er", pH, "Løsningen er basisk!")
else:
    print("pH-verdien er", pH, "Men det går jo ikke... Sikker på at du har skrevet inn riktig menge H+ ioner?" )    
#Output med pH verdien og om løsningen er sur, nøytral eller basisk. Gir feilmelding hvsi pH verdien er større enn 14 eller negativ.   
    