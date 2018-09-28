#Oppgave 4


print(" ")
while True:
    n=float(input("Hvilket tall vil du ta fakultet av?"))
    if n>=0 and n%1==0:
        break
    else:
        print("Tallet ditt er ikke ett positivt heltall, så du kan ikke ta fakultet av det.")
#Lager en while-løkke for å sjekke om n er et positivt heltall.
#Hvis ikke kommer det feilmelding og du må skrive inn på nytt helt til du får ett positivt heltall.

fakultet=1
tall=n
if n>0:    
    while tall > 0:
        fakultet*=tall
        tall-=1
    
    print(n,"!=",fakultet)

#Lager en for-løkke for å printe ut fakultet av det positive heltallet.

elif n==0:
    print("0!=1")        
#Formelen fungerer ikke for n=0 så lager en egen elif for 0!=1.

    