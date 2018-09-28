#Oppgave 3

print(" ")
print("Vi skal beregne dyrebefolkningen t år fra i dag.")
print(" ")
print("Formelen for dett er B_ny=B_nåværende*(1+(p/100)) eller B_ny=B_nåværende*(1-(p/100))")
#Informerer brukeren om hva programmet gjør.

B_nåværende=float(input("Hva er B_nåværende?"))
p=float(input("Hvor mye vokser eller synker prosenten av dyrebefolkningen med per år? Skriv inn minustegn foran hvis den synker."))
t=int(input("Etter hvor mange år vil du vite befolkningen?"))
#Spør brukeren om hva B_nåværende, p og t.

for t in range (1,t+1):
    B_ny=(B_nåværende*(1+(p/100))**t)
#Lager en løkke hvor jeg regner ut den nye befolkningen fra 1 til t ganger.    

print("Befolkningen er",(B_ny),"etter", t,"år")
#Skriver ut den nye befolkningen etter t år.




