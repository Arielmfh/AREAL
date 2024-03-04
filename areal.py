import os

# Funksjon for å tømme terminalen
def clear():
    os.system('cls')

# Funskjon for å skrive hovedmenyen til skjerm
def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Beregn areal for kvadrat")
    print("2. Beregn areal for rektangel")
    print("3. Beregn areal for trekant")
    print("4. Beregn areal for parallellogram")
    print("5. Beregn areal for rombe")
    print("6. Beregn areal for trapes")
    print("7. Beregn areal for sirkel")
    print("8. Avslutt")


# Funksjon for å beregne arealet av et kvadrat skrives her. Funsjonen skal ta imot et parameter (s)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def arealKvadrat(side): 
     areal = side * side
     return areal


# Funksjon for å beregne arealet av et rektangel skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def arealRektangel(grunnlinje, hoyde):
    areal = grunnlinje * hoyde
    return areal


# Funksjon for å beregne arealet av en trekant skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def arealTrekant(grunnlinje, hoyde):
    areal = grunnlinje * hoyde / 2
    return areal


# Funksjon for å beregne arealet av et parallellogram skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def arealParallellogram(grunnlinje, hoyde):
    areal = grunnlinje * hoyde
    return areal

# Funksjon for å beregne arealet av en rombe skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen
def areal_rombe(L, B):
    A = L * B
    return A

# Funksjon for å beregne arealet av en trapes skrives her. Funsjonen skal ta imot tre parameter (a, b og h)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen
def areal_trapes(a, b, høyde):
    A = a + b * høyde / 2
    return A

# Funksjon for å beregne arealet av en sirkel skrives her. Funsjonen skal ta imot et parameter (r)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen
def areal_sirkel(radius):
    A = 3.14 * radius * 2
    return A
   

# Programmet starter her
ans="Start"
while ans != "8":
    clear()
    skriv_meny()
    
    ans=input("Hva ønsker du å gjøre. Velg tall? ") 
    if ans=="1":
        clear()
        print("\nHer beregnes arealet av et kvadrat")
        side = int(input("Hva er lengden til sidene? (cm) "))
        areal = arealKvadrat(side)
        print("Arealet til kvadraten er",areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!")    
    elif ans=="2":
        clear()
        print("\nHer beregnes arealet av et rektangel")
        grunnlinje = int(input("Hva er grunnlinjen til rektangelen? (cm) "))
        hoyde = int(input("Hva er høyden til rektangelen? (cm) "))
        areal = arealRektangel(grunnlinje, hoyde)
        print("Arealet til rektangelen er", areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="3":
        clear()
        print("\nHer beregnes arealet av en trekant") 
        grunnlinje = int(input("Hva er grunnlinjen til trekanten? (cm) "))
        hoyde = int(input("Hva er høyden til trekanten? (cm) "))
        areal = arealTrekant(grunnlinje, hoyde)
        print("Arealet til trekanten er", areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="4":
        clear()
        print("\nHer beregnes arealet av et parallellogram")
        grunnlinje = int(input("Hva er grunnlinjen til parallellogramen? (cm) "))
        hoyde = int(input("Hva er høyden til parallellogramen? (cm) "))
        areal = arealParallellogram(grunnlinje, hoyde)
        print("Arealet til parallellogramen er", areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="5":
        clear()
        print("\nHer beregnes arealet av en rombe")
        grunnlinje = int(input("Hva er grunnlinjen til romben? (cm) "))
        hoyde = int(input("Hva er høyden til romben? (cm) "))
        areal = areal_rombe(grunnlinje, hoyde)
        print("Arealet til Rombe er", areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="6":
        clear()
        print("\nHer beregnes arealet av en trapes")
        a = int(input("Hva er a til trapes? (cm) "))
        b = int(input("Hva er b til trapes? (cm) "))
        hoyde = int(input("Hva er høyden til trapes? (cm) "))
        areal = areal_trapes(a, b, hoyde)
        print("Arealet til trapes er", areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!")         
    elif ans=="7":
        clear()
        print("\nHer beregnes arealet av en sirkel")
        radius = int(input("Hva er radius til sirkel? (cm) "))
        areal = areal_sirkel(radius)
        print("Arealet til sirkelen er", areal,"cm²")
        venter=input("Trykk ENTER for å fortsette!") 
    
print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")          
    
        