#Oppgave 2

import math
#Importerer matteliste for å bruke sqrt senere
print(" ")
print("Formelen for kinetisk energi er E=(1/2)*m*v^2")
variabel=input("Hvilken variabel vil du finne?")
#Spør brukeren om hvilken variabel som han/hun vil finne

if variabel=="E" or variabel=="e":
    m1=float(input("Hva er verdien for m i kg?"))
    v1=float(input("Hva er verdien for v i m/s?"))
    print("E=",0.5*m1*(v1**2),"J")
#Spør brukeren om verdien av m og v for å finne E. Output med verdien av E.
    
while variabel=="m" or variabel=="M":
    E2=float(input("Hva er verdien for E i J?"))
    v2=float(input("Hva er verdien for v i m/s?"))
    print("m",(2*E2)/(v2**2),"kg")
#Spør brukeren om verdien av E og v for å finne m. Output med verdien av m.
    
if variabel=="v" or variabel=="V":
    m3=float(input("Hva er verdien for m i kg?"))
    E3=float(input("Hva er verdien for E i J?"))
    print("v=",math.sqrt((E3*2)/m3),"m/s")
#Spør brukeren om verdien av m og E for å finne v. Output med verdien av v. 