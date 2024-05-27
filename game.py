import os
import time

zapisy=[]
save=[]
mikstury=[0,0,0,0]
upgrade=[0,0,0]
attacks=[0,0]
p=1
q=1

autozapis = 0
przegrana = False

zycie=5
obrazenia=3

try:
    file=open("zapisy.txt", "r", encoding="utf8")

    for line in file.readlines():
        if line!="\n":
            zapisy.append(line.strip())
    file.close()

except FileNotFoundError:
    file=open("zapisy.txt", "w", encoding="utf8")
    file.close()

class postac:
    def __init__(self, name, hp, points, money):
        self.name=name
        self.hp=hp
        self.points=points
        self.money=money
    
    def Menu(self):
        global autozapis, przegrana
        while True:
            print("""
Co chcesz zrobić?
    1. Idź dalej 
    2. Otwórz sklep 
    3. Zobacz swoje statystyki i ekwipunek
    4. Włącz / wyłącz autozapis
    5. Usuń zapis
    6. Zapisz grę (max 5 zapisów)
    7. Zapisz grę i wyjdź""")
            
            x=input()
            if x!="1" and x!="2" and x!="3" and x!="4" and x!="5" and x!="6" and x!="7":
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                break

        os.system('cls')

        if x=="1":
            potwor.Appear()

        elif x=="2":
            gracz.Shop()

        elif x=="3": 
            gracz.Statistics()

        elif x=="4": 
            gracz.Autosave()

        elif x=="5":
            gracz.DeleteRecord() 

        elif x=="6" or x=="7":
            if len(zapisy)>=5:
                print("Masz już komplet zapisów! Przejdź do podpunktu '5. Usuń zapis', aby usunąć jeden z nich. Dopiero po tym będziesz mógł zapisać obecny progres!\n")
                gracz.Menu()
            else:
                gracz.Save()
                print("Pomyślnie zapisano!\n")
                if x=="6":
                    gracz.Menu()
                elif x=="7":
                    przegrana=True

#========================================================

    def Shop(self):
        while True:
            print("\nWitamy w sklepie!")
            print(f"Twój obecny stan konta: {gracz.money}$")
            print("""
Nasz asortyment: (aby wyjść wpisz 0)
    1. Mikstury
    2. Ulepszenia 
    3. Ataki
    """)
            x=input("Czego potrzebujesz? ")
            if x!="0" and x!="1" and x!="2" and x!="3":
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                break

        os.system('cls')
  
        if x=="0":
            gracz.Menu()

        elif x=="1":
            gracz.BuyPotions()

        elif x=="2":
            gracz.BuyUpgrades()

        elif x=="3": 
            gracz.BuyAttacks()

#========================================================

    def BuyPotions(self):
        while True:
            print(f"\nTwój obecny stan konta: {gracz.money}$")
            print("""
NASZE MIKSTURY: 

    1. Mikstura życia - odnawia HP do pełna - 2$
    2. Miktrura szczęscia - podwójny loot z potwora - 2$
    3. Mikstura siły - podwójne obrażenia (przy atakach z oślepieniem działa na oba ataki) - 2$""")
            if gracz.name=="Mag":
                print("    4. Mikstura energi - odnawia 10 many - 2$")
            if gracz.name=="Rycerz":
                print("    4. Mikstura energi - odnawia 10 punktów ataku - 2$")
            if gracz.name=="Tank":
                print("    4. Mikstura energi - odnawia 10 punktów obrony - 2$")

            odp=input("\nKtórą miksturę chcesz kupić? (aby wyjść wpisz 0) ")

            if odp!="0" and odp!="1" and odp!="2" and odp!="3" and odp!="4":
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                if odp!="0" and gracz.money<2:
                    os.system('cls')
                    print("NIE STAĆ CIĘ NA TĄ MIKSTURĘ!")
                    continue
                break
        
        os.system('cls')

        if odp=="0":
            gracz.Shop()

        else:
            if odp=="1":
                print("Pomyślnie zakupiono miksturę życia!")
                mikstury[0]+=1

            elif odp=="2":
                print("Pomyślnie zakupiono miksturę szczęścia!")
                mikstury[1]+=1

            elif odp=="3":
                print("Pomyślnie zakupiono miksturę siły!")
                mikstury[2]+=1

            elif odp=="4":
                print("Pomyślnie zakupiono miksturę energii!")
                mikstury[3]+=1

            gracz.money-=2
            gracz.BuyPotions()

#========================================================

    def BuyUpgrades(self):
        while True:
            print(f"\nTwój obecny stan konta: {gracz.money}$")
            print("""
NASZE ULEPSZENIA: 

    1. Ulepszenie HP - dodatkowe 2 HP - 3$
    2. Ulepszenie ataku - zabiera 1HP więcej przy atakowaniu - 3$""")
            if gracz.name=="Mag":
                print("    3. Ulepszenie lootu - dodatkowy 1$ i dodatkowa 1 mana - 4$")   
            if gracz.name=="Rycerz":
                print("    3. Ulepszenie lootu - dodatkowy 1$ i dodatkowy 1 punkt ataku - 4$") 
            if gracz.name=="Tank":
                print("    3. Ulepszenie lootu - dodatkowy 1$ i dodatkowy 1 punkty obrony - 4$")   

            odp=input("\nKtóre ulepszenie chcesz kupić? (aby wyjść wpisz 0) ")

            if odp!="0" and odp!="1" and odp!="2" and odp!="3":
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                if ((odp=="1" or odp=="2") and gracz.money<3) or (odp=="3" and gracz.money<4):
                    os.system('cls')
                    print("NIE STAĆ CIĘ NA TO ULEPSZENIE!")
                    continue
                break
            
        os.system('cls')

        if odp=="0":
            gracz.Shop()
        
        if odp=="1":
            print("Pomyślnie zakupiono ulepszenie HP!\n")
            upgrade[0]+=1
            gracz.money-=3
            if gracz.hp<10+upgrade[0]*2:
                gracz.hp=10+upgrade[0]*2
            gracz.BuyUpgrades()

        elif odp=="2":
            print("Pomyślnie zakupiono ulepszenie ataku!\n")
            upgrade[1]+=1
            gracz.money-=3
            gracz.BuyUpgrades()
        
        elif odp=="3":
            print("Pomyślnie zakupiono ulepszenie lootu!\n")
            upgrade[2]+=1
            gracz.money-=4
            gracz.BuyUpgrades()

#========================================================

    def BuyAttacks(self):
        while True:
            print(f"\nTwój obecny stan konta: {gracz.money}$")
            if gracz.name=="Mag":
                print(f"""
NASZE ATAKI: 

    1. Deadzone - zabiera całe HP przeciwnika - 5$
    2. Masterlight - regenerujesz {(10+upgrade[1])*q}HP i atakujesz ponownie - 5$""")
            
            if gracz.name=="Rycerz":
                print(f"""
NASZE ATAKI: 

    1. Hellforce - zabiera całe HP przeciwnika - 5$
    2. Brutalrage - regenerujesz {(10+upgrade[1])*q}HP i atakujesz ponownie - 5$""")
            
            if gracz.name=="Tank":
                print(f"""
NASZE ATAKI: 

    1. Fusionblast - zabiera całe HP przeciwnika - 5$
    2. Datalife - zadajesz 3CP, regenerujesz {(10+upgrade[1])*q}HP i atakujesz ponownie- 5$""")
                
            odp=input("\nKtóry atak chcesz kupić? (aby wyjść wpisz 0) ")

            if odp!="0" and odp!="1" and odp!="2":
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                if (odp=="1" or odp=="2") and gracz.money<5:
                    os.system('cls')
                    print("NIE STAĆ CIĘ NA TEN ATAK!")
                    continue
                if (odp=="1" and attacks[0]==1) or (odp=="2" and attacks[1]==1):
                    os.system('cls')
                    print("JUŻ POSIADASZ TEN ATAK!")
                    continue
                break

        os.system("cls")

        if odp=="0":
            gracz.Shop()

        elif odp=="1":
            if gracz.name=="Mag":
                print("Pomyślnie zakupiono atak Deadzone!")
            if gracz.name=="Rycerz":
                print("Pomyślnie zakupiono atak Hellforce!")
            if gracz.name=="Tank":
                print("Pomyślnie zakupiono atak Fusionblast!")
            attacks[0]+=1

        elif odp=="2":
            if gracz.name=="Mag":
                print("Pomyślnie zakupiono atak Masterlight!")
            if gracz.name=="Rycerz":
                print("Pomyślnie zakupiono atak Brutalrage!")
            if gracz.name=="Tank":
                print("Pomyślnie zakupiono atak Datalife!")
            attacks[1]+=1

        gracz.money-=5
        gracz.BuyAttacks()

#========================================================

    def Statistics(self):
        print(f"""
TWOJE STATYSTYKI:
                      
Klasa: {gracz.name}
HP: {10+upgrade[0]*2}
Pieniądze: {gracz.money}""")
        
        if gracz.name=="Mag":
            print(f"Mana: {gracz.points}")

        if gracz.name=="Rycerz":
            print(f"Punkty ataku: {gracz.points}")
            
        if gracz.name=="Tank":
            print(f"Punkty obrony: {gracz.points}")   
                
        print("\n\nTWOJE MIKSTURY: \n")
        if mikstury[0]==0 and mikstury[1]==0 and mikstury[2]==0 and mikstury[3]==0:
            print("Nie masz żadnych mikstur!")
        else:
            print(f"1. Mikstura życia ({mikstury[0]})")
            print(f"2. Mikstura szczęścia ({mikstury[1]})")
            print(f"3. Mikstura siły ({mikstury[2]})")
            print(f"4. Mikstura energii ({mikstury[3]})")

        print("\n\nTWOJE ULEPSZENIA: \n")
        if upgrade[0]==0 and upgrade[1]==0 and upgrade[2]==0:
            print("Nie masz żadnych ulepszeń!")
        else:
            print(f"1. Ulepszenie HP ({upgrade[0]})")
            print(f"2. Ulepszenie ataku ({upgrade[1]})")
            print(f"3. Ulepszenie lootu ({upgrade[2]})")


        print("\n\nTWOJE ATAKI: \n")
        if gracz.name=="Mag":
            print("1. Fireball\n2. Stun\n3. Automatyczny atak")
            u=4
            if attacks[0]==1:
                print(f"{u}. Deadzone")
                u+=1
            if attacks[1]==1:
                print(f"{u}. Masterlight")
        if gracz.name=="Rycerz":
            print("1. Swing\n2. Slay\n3. Automatyczny atak")
            u=4
            if attacks[0]==1:
                print(f"{u}. Hellforce")
                u+=1
            if attacks[1]==1:
                print(f"{u}. Brutalrage")
        if gracz.name=="Tank":
            print("1. Heal\n2. Wall\n3. Automatyczny atak")
            u=4
            if attacks[0]==1:
                print(f"{u}. Fusionblast")
                u+=1
            if attacks[1]==1:
                print(f"{u}. Datalife")

        input("\n\nKliknij enter, aby wyjść.")
        os.system("cls")
        gracz.Menu()

#=======================================================

    def Autosave(self):
        global autozapis
        while True:
            odp = input("""
Co chcesz zrobić? (aby wyjść wpisz 0)

    1. Włączyć autozapis
    2. Wyłączyć autozapis
""")
            if odp !="0" and odp != "1" and odp!= "2":
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                break
        
        os.system("cls")

        if odp=="0":
            gracz.Menu()
        
        elif odp=="1":
            if autozapis != 0:
                print("Autozapis jest już włączony! \n")
                gracz.Autosave()
            else:
                if len(zapisy)<5:
                    print("""Pomyślnie włączono autozapis!
Po zabiciu potwora twoja gra będzie automatycznie zapisana, więc nie musisz bać się utraty postępu!\nFunkcja autozapis jest domyślnie wyłączona, więc po ponownym włączeniu gry progres nie będzie się zapisywać automatycznie. \n""")
                    gracz.Save()
                    autozapis = len(zapisy)
                    gracz.Menu()
                    
                else:
                    print("Masz już komplet zapisów! Przejdź do podpunktu '5. Usuń zapis', aby usunąć jeden z nich. Dopiero po tym będziesz mógł zapisać obecny progres!\n")
                    gracz.Menu()

        elif odp=="2":
            if autozapis == 0:
                print("Autozapis nie został jeszcze włączony!\n")
                gracz.Autosave()
            else:
                print("Pomyślnie wyłączono autozapis!\n")
                autozapis = 0
                gracz.Menu()

#========================================================

    def DeleteRecord(self):
        global autozapis
        if len(zapisy)==0:
            print("Nie masz żadnych zapisów!\n")
            gracz.Menu()   
        else:
            while True:
                print("\nLista zapisów:\n") 
                for q in range(len(zapisy)):
                    save= zapisy[q].split(", ")
                    if q==autozapis-1:
                        print("AUTOZAPIS ", end="")
                    if save[0]=="Mag":
                        print(f"{q+1}. Postać: Mag, HP: {save[1]}, Mana: {save[2]}, Stan konta: {save[3]}\nStatystyki potwora: HP: {save[4]}, CP: {save[5]}\n")
                    if save[0]=="Rycerz":
                        print(f"{q+1}. Postać: Rycerz, HP: {save[1]}, Punkty ataku: {save[2]}, Stan konta: {save[3]}\nStatystyki potwora: HP: {save[4]}, CP: {save[5]}\n")
                    if save[0]=="Tank":
                        print(f"{q+1}. Postać: Tank, HP: {save[1]}, Punkty obrony: {save[2]}, Stan konta: {save[3]}\nStatystyki potwora: HP: {save[4]}, CP: {save[5]}\n")

                try:
                    pyt=int(input("Który zapis chcesz usunąć? (aby wyjść wpisz 0) "))
                except ValueError:
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue

                if pyt<0 or pyt>len(zapisy):
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

            os.system("cls")

            if pyt==0:
                gracz.Menu()

            else:
                if pyt==autozapis:
                    print("Nie możesz usunąć autozapisu.") 
                    gracz.DeleteRecord()
                else:
                    odp = input("Czy jesteś pewien? t/n\n")
                    while odp!="t" and odp!="T" and odp!="n" and odp!="N":
                        os.system("cls")
                        print("Niepoprawna odpowiedź!\n")
                        odp = input("Czy jesteś pewien? t/n\n")

                    os.system("cls")
                    
                    if odp=="t" or odp=="T":
                        if pyt<autozapis:
                            autozapis= autozapis-1
                        zapisy.pop(int(pyt)-1)
                        file=open("zapisy.txt", "w", encoding="utf8")
                        for i in range(len(zapisy)):
                            print(f"{zapisy[i]}\n")
                            file.write(f"{zapisy[i]}\n")
                        file.close()
                        os.system("cls")
                        print("Pomyślnie usunięto zapis.\n")
                        gracz.Menu()

                    if odp=="n" or odp=="N":
                        gracz.DeleteRecord()

#========================================================

    def Save(self):
        file= open("zapisy.txt", "a", encoding="utf8")
        save = f"{gracz.name}, {gracz.hp}, {gracz.points}, {gracz.money}, {potwor.hp}, {potwor.cp}, {mikstury[0]}, {mikstury[1]}, {mikstury[2]}, {mikstury[3]}, {upgrade[0]}, {upgrade[1]}, {upgrade[2]}, {attacks[0]}, {attacks[1]}\n"
        file.write(save) 
        zapisy.append(save)
        file.close()

#========================================================

    def Potions(self):
        global p,q

        if mikstury[0]==0 and mikstury[1]==0 and mikstury[2]==0 and mikstury[3]==0:
            print("Nie masz żadnych mikstur!")
            gracz.PlayerAttack()

        else:
            while True:
                print(f"\n1. Mikstura życia - odnawia HP do pełna ({mikstury[0]})")
                print(f"2. Mikstura szczęścia - podwójny loot ({mikstury[1]})") ##p
                print(f"3. Mikstura siły - podwójne obrażenia (przy atakach z oślepieniem działa na dwie tury) ({mikstury[2]})") ##q
                if gracz.name=="Mag":
                    print(f"4. Mikstura energii - odnawia 10 many ({mikstury[3]})")
                if gracz.name=="Rycerz":
                    print(f"4. Mikstura energii - odnawia 10 punktów ataku  ({mikstury[3]})")
                if gracz.name=="Tank":
                    print(f"4. Mikstura energii - odnawia 10 punktów obrony ({mikstury[3]})")

                g=input("Którą miksturę chcesz wypić? (aby wyjść wpisz 0) ")
                
                if g!="0" and g!="1" and g!="2" and g!="3" and g!="4":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

            os.system("cls")

            if g=="0":
                gracz.PlayerAttack()

            elif g=="1":
                if mikstury[0]==0:
                    print("Nie masz tej mikstury!\n")
                    gracz.Potions()
                else:
                    print("Używasz mikstury życia!\n")
                    mikstury[0]-=1
                    gracz.hp=10+upgrade[0]*2
                    gracz.PlayerAttack()
            
            elif g=="2":
                if p==2:
                    print("Już użyto tej mikstury!\n")
                    gracz.Potions()
                else:
                    if mikstury[1]==0:
                        print("Nie masz tej mikstury!\n")
                        gracz.Potions()
                    else:
                        print("Używasz mikstury szczęścia!\n")
                        mikstury[1]-=1
                        p+=1
                        gracz.PlayerAttack()
                        
            elif g=="3":
                if q==2:
                    print("Już użyto tej mikstury!\n")
                    gracz.Potions()
                else:
                    if mikstury[2]==0:
                        print("Nie masz tej mikstury!\n")
                        gracz.Potions()
                    else: 
                        print("Używasz mikstury siły!\n")
                        mikstury[2]-=1
                        q+=1
                        gracz.PlayerAttack()
            
            if g=="4":
                if mikstury[3]==0:
                    print("Nie masz tej mikstury!\n")
                    gracz.Potions()
                else:
                    print("Używasz mikstury energii!\n")
                    mikstury[3]-=1
                    gracz.points+=10
                    gracz.PlayerAttack()

#========================================================

    def KillMonster(self):
        global p, q, zycie, obrazenia
        if ((2+upgrade[2])*p)<5:
            print(f"Potwór umiera! Otrzymujesz {(2+upgrade[2])*p} monety", end="")
        else:
            print(f"Potwór umiera! Otrzymujesz {(2+upgrade[2])*p} monet", end="")

        if gracz.name=="Mag":
            if ((4+upgrade[2])*p)<5:
                print(f" i {(4+upgrade[2])*p} many!\n")
            else:
                print(f" i {(4+upgrade[2])*p} man!\n")

        if gracz.name=="Rycerz":
            if ((4+upgrade[2])*p)<5:
                print(f" i {(4+upgrade[2])*p} punkty ataku!\n")
            else:
                print(f" i {(4+upgrade[2])*p} punktów ataku!\n")

        if gracz.name=="Tank":
            if ((4+upgrade[2])*p)<5:
                print(f" i {(4+upgrade[2])*p} punkty obrony!\n")
            else:
                print(f" i {(4+upgrade[2])*p} punktów obrony!\n")
        
        zycie+=1
        obrazenia+=1
        potwor.hp=zycie
        potwor.cp=obrazenia 
        if gracz.hp<10+upgrade[0]*2:
            gracz.hp=10+upgrade[0]*2
        gracz.money+= (2+upgrade[2])*p 
        gracz.points += (4+upgrade[2])*p
        p=1
        q=1
        if autozapis != 0:
            zapisy[autozapis-1]=f"{gracz.name}, {gracz.hp}, {gracz.points}, {gracz.money}, {potwor.hp}, {potwor.cp}, {mikstury[0]}, {mikstury[1]}, {mikstury[2]}, {mikstury[3]}, {upgrade[0]}, {upgrade[1]}, {upgrade[2]}, {attacks[0]}, {attacks[1]}"
            file= open("zapisy.txt", "w", encoding="utf8")
            for x in range(len(zapisy)):
                file.write(zapisy[x]+"\n")
            file.close()
        gracz.Menu()

#========================================================

    def UseRecord(self):
        global gracz, przegrana
        while True:
            print("\nLista zapisów:\n") 
            for q in range(len(zapisy)):
                save= zapisy[q].split(", ")        
                if save[0]=="Mag":
                    print(f"{q+1}. Postać: Mag, HP: {save[1]}, Mana: {save[2]}, Stan konta: {save[3]}\nStatystyki potwora: HP: {save[4]}, CP: {save[5]}\n")
                if save[0]=="Rycerz":
                    print(f"{q+1}. Postać: Rycerz, HP: {save[1]}, Punkty ataku: {save[2]}, Stan konta: {save[3]}\nStatystyki potwora: HP: {save[4]}, CP: {save[5]}\n")
                if save[0]=="Tank":
                    print(f"{q+1}. Postać: Tank, HP: {save[1]}, Punkty obrony: {save[2]}, Stan konta: {save[3]}\nStatystyki potwora: HP: {save[4]}, CP: {save[5]}\n")
            try:
                pyt=int(input("Którego zapisu chcesz użyć? (aby wyjść wpisz 0) "))
            except ValueError:
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue

            if pyt<0 or pyt>len(zapisy):
                os.system('cls')
                print("NIEPOPRAWNY NUMER!")
                continue
            else:
                break

        os.system("cls")

        if pyt==0:
            print()
        else:
            przegrana = False
            zapis=zapisy[int(pyt)-1].split(", ")
            if zapis[0]=="Mag":
                gracz=mag()
            if zapis[0]=="Rycerz":
                gracz=rycerz()
            if zapis[0]=="Tank":
                gracz=tank()
            gracz.name=zapis[0]
            gracz.hp=int(zapis[1])
            gracz.points=int(zapis[2])
            gracz.money=int(zapis[3])
            potwor.hp=int(zapis[4])
            potwor.cp=int(zapis[5])
            mikstury[0]=int(zapis[6])
            mikstury[1]=int(zapis[7])
            mikstury[2]=int(zapis[8])
            mikstury[3]=int(zapis[9])
            upgrade[0]=int(zapis[10])
            upgrade[1]=int(zapis[11])
            upgrade[2]=int(zapis[12])
            attacks[0]=int(zapis[13])
            attacks[1]=int(zapis[14])
            os.system('cls')
            print("Pomyślnie wgrano zapis.") 
            gracz.Menu()            

class monster:
    def __init__(self, hp, cp):
        self.hp=hp
        self.cp=cp

    def Appear(self):
        print("Idziesz przed siebie.")
        time.sleep(0.3)
        os.system('cls')
        print("Idziesz przed siebie..")
        time.sleep(0.3)
        os.system('cls')
        print("Idziesz przed siebie...")
        time.sleep(0.3)
        os.system('cls')
        print("Idziesz przed siebie.")
        time.sleep(0.3)
        os.system('cls')
        print("Idziesz przed siebie..")
        time.sleep(0.3)
        os.system('cls')
        print("Idziesz przed siebie...")
        time.sleep(0.3)
        os.system('cls')
        print("POJAWIŁ SIĘ POTWÓR")
        print("")
        gracz.PlayerAttack()

#========================================================

    def MonsterAttack(self):
        global przegrana, gracz
        print("\nPotwór kontraatakuje!")
        print(f"Zabiera {self.cp}HP!!")
        gracz.hp-=self.cp
        if gracz.hp<=0:  
            przegrana = True        
            while przegrana==True:
                print("Przegrywasz grę! Mam nadzieję, że się podobało!\n")
                while True:
                    x = input("""
    Co chcesz zrobić? 
        1. Wyjść
        2. Rozpocząć grę od początku
        3. Wgrać zapis
    """)
                    
                    if x!="1" and x!="2" and x!="3":
                        os.system('cls')
                        print("NIEPOPRAWNY NUMER!")
                        continue
                    else:
                        break

                os.system("cls")

                if x=="3":
                    if autozapis != 0:
                        print("Autozapis jest włączony. Zostanie wgrany ostatni save.")
                        przegrana = False 
                        zapis=zapisy[autozapis-1].split(", ")
                        if zapis[0]=="Mag":
                            gracz=mag()
                        if zapis[0]=="Rycerz":
                            gracz=rycerz()
                        if zapis[0]=="Tank":
                            gracz=tank()
                        gracz.name=zapis[0]
                        gracz.hp=int(zapis[1])
                        gracz.points=int(zapis[2])
                        gracz.money=int(zapis[3])
                        potwor.hp=int(zapis[4])
                        potwor.cp=int(zapis[5])
                        mikstury[0]=int(zapis[6])
                        mikstury[1]=int(zapis[7])
                        mikstury[2]=int(zapis[8])
                        mikstury[3]=int(zapis[9])
                        upgrade[0]=int(zapis[10])
                        upgrade[1]=int(zapis[11])
                        upgrade[2]=int(zapis[12])
                        attacks[0]=int(zapis[13])
                        attacks[1]=int(zapis[14])
                        os.system('cls')
                        print("Pomyślnie wgrano zapis.") 
                    else:
                        if len(zapisy)==0:
                            print("Niestety nie masz żadnych zapisów.")
                            while True:
                                x=input("""
    Co chcesz zrobić? 
        1. Wyjść
        2. Rozpocząć grę od początku
    """)
                                
                                if x!="1" and x!="2":
                                    os.system('cls')
                                    print("NIEPOPRAWNY NUMER!")
                                    continue
                                else:
                                    break
                        else:
                            gracz.UseRecord()

                if x=="1":  
                    print("\nPapa, miło było! :)")
                    break

                if x=="2":
                    os.system("python game.py") 
                    break

        else:
            gracz.PlayerAttack()

class mag(postac):
    
    def __init__(self):
        super().__init__("Mag", 10, 10, 0)

    def Instrukcja(self):
        os.system('cls')
        print("WYBRAŁEŚ MAGA!")
        print("Pokonuj pojawiające się potwory używając magicznych ataków!")
        print("Na start otrzymujesz 10 many, używaj jej mądrze atakując przeciwników!")
        print(f"Twoje ataki: \n · Fireball - zadaje 3 obrażenia, kosztuje 2 many \n · Stun - zadaje 2 obrażenia i oślepia przeciwnika co pozwala ci zaatakować ponownie, kosztuje 3 many")
        print(f"Jeżeli nie stać cię na żaden atak, możesz zaatakować potwora darmowym atakiem zabierając 1HP!")
        print("Statystyki potworów są zależne od zaawansowania gry.")
        print("Po pokonaniu przeciwnika twoje HP odnawia się do 10 oraz otrzymujesz 2 monety i 4 many!")
        print("Za monety możesz kupować przeróżne mikstury, ulepszenia wyposażenia, a nawet dodatkowe ataki!")

#========================================================

    def PlayerAttack(self):
        global p, q, zycie, obrazenia
        while True:
            print(f"\nStatystyki potwora \nHP: {potwor.hp}, CP: {potwor.cp} \n")
            print(f"Twoje statystyki \nHP: {gracz.hp}, mana: {self.points}")
            print(f"""
Którego ataku chcesz użyć? Możliwe ataki:
    1. Fireball - {(3+upgrade[1])*q}CP: 2 many
    2. Stun - {(2+upgrade[1])*q}CP, oślepienie: 3 many 
    3. Darmowy atak - {(1+upgrade[1])*q}CP""")
            u=0
            if attacks[0]==1:
                print(f"    {u+4}. Deadzone - zabiera całe HP przeciwnika: 6 man")
                u+=1                          
            if attacks[1]==1:
                print(f"    {u+4}. Masterlight - regenerujesz {(10+upgrade[1])*q}HP i atakujesz ponownie: 6 man")
            print("\n    Wpisz M, aby użyć mikstur")

            x=input()

            if attacks[0]==0 and attacks[1]==0:
                if x!="1" and x!="2" and x!="3" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

            if (attacks[0]==1 and attacks[1]==0) or (attacks[0]==0 and attacks[1]==1):
                if x!="1" and x!="2" and x!="3" and x!="4" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

            if attacks[0]==1 and attacks[1]==1:
                if x!="1" and x!="2" and x!="3" and x!="4" and x!="5" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break
   
        os.system('cls')

        if x=="1":
            gracz.Fireball()
        elif x=="2":
            gracz.Stun()
        elif x=="3":
            gracz.FreeAttack()
        elif x=="4":
            if attacks[0]==1:
                gracz.Deadzone()
            else:
                gracz.Masterlight()
        elif x=="5":
            gracz.Masterlight()
        elif x=="M" or x=="m":
            gracz.Potions()

#========================================================

    def Fireball(self):
        global p, q, zycie, obrazenia
        if self.points<2:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=2
            print("Mag używa ataku Fireball!!")
            potwor.hp-=(3+upgrade[1])*q
            if potwor.hp<=0:
                gracz.KillMonster()
                                  
            else:
                print(f"Zabierasz {(3+upgrade[1])*q}HP!!")
                q=1
                potwor.MonsterAttack()

#========================================================

    def Stun(self):
        global p, q, zycie, obrazenia
        if self.points<3:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=3
            print("Mag używa ataku Stun!!")
            potwor.hp-=(2+upgrade[1])*q
            if potwor.hp<=0:
                gracz.KillMonster()
            else:
                print(f"Zabierasz {(2+upgrade[1])*q}HP i atakujesz ponownie!")
                gracz.PlayerAttack()

#========================================================

    def FreeAttack(self):
        global p, q, zycie, obrazenia
        print(f"Mag używa darmowego ataku!!")
        potwor.hp-=(1+upgrade[1])*q
        if potwor.hp<=0:
            gracz.KillMonster()
        else:
            print(f"Zabierasz {(1+upgrade[1])*q}HP!!")
            q=1
            potwor.MonsterAttack()

#========================================================

    def Deadzone(self):
        global p, q, zycie, obrazenia
        if self.points<6:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=6
            print("Mag używa ataku Deadzone!!")
            gracz.KillMonster()

#========================================================

    def Masterlight(self):
        global p, q, zycie, obrazenia
        if self.points<6:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=6
            print("Mag używa ataku Masterlight!!") 
            print(f"Otrzymujesz dodatkowe {(10+upgrade[1])*q}HP i atakujesz ponownie!")
            gracz.hp+=(10+upgrade[1])*q
            gracz.PlayerAttack()

class rycerz(postac):
    
    def __init__(self):
        super().__init__("Rycerz", 10, 10, 0)

    def Instrukcja(self):
        os.system('cls')
        print("WYBRAŁEŚ RYCERZA!")
        print("Pokonaj potwory dzięki swoim świetnym umiejętnościom walki wręcz i posługiwania się mieczem!")
        print("Na start otrzymujesz 10 punktów ataku, używaj ich mądrze atakując przeciwników!")
        print(f"Twoje ataki: \n · Swing - zadaje 3 obrażenia, kosztuje 2 punkty ataku \n · Slay - zadaje 2 obrażenia i dezorientuje przeciwnika, co pozwala ci zaatakować ponownie, kosztuje 3 punkty ataku")
        print(f"Jeżeli nie stać cię na żaden atak, możesz zaatakować darmowym atakiem zabierając 1HP!")
        print("Statystyki potworów są zależne od zaawansowania gry.")
        print("Po pokonaniu przeciwnika twoje HP odnawia się do 10 oraz otrzymujesz 2 monety i 4 punkty ataku!")
        print("Za monety możesz kupować przeróżne mikstury, ulepszenia wyposażenia, a nawet dodatkowe ataki!")

#========================================================

    def PlayerAttack(self):
        global p, q, zycie, obrazenia
        while True:
            print(f"\nStatystyki potwora \nHP: {potwor.hp}, CP: {potwor.cp} \n")
            print(f"Twoje statystyki \nHP: {gracz.hp}, mana: {self.points}")
            print(f"""
Którego ataku chcesz użyć? Możliwe ataki:
    1. Swing - {(3+upgrade[1])*q}CP: 2 punkty ataku
    2. Slay - {(2+upgrade[1])*q}CP, dezorientacja przeciwnika: 3 punkty ataku
    3. Darmowy atak - {(1+upgrade[1])*q}CP""")
            u=0
            if attacks[0]==1:
                print(f"    {u+4}. Hellforce - zabiera całe HP przeciwnika: 6 punktów ataku")
                u+=1                          
            if attacks[1]==1:
                print(f"    {u+4}. Brutalrage - regenerujesz {(10+upgrade[1])*q}HP i atakujesz ponownie: 6 punkty ataku")

            print("\n    Wpisz M, aby użyć mikstur")

            x=input()

            if (attacks[0]==1 and attacks[1]==0) or (attacks[0]==0 and attacks[1]==1):
                if x!="1" and x!="2" and x!="3" and x!="4" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break
            
            if attacks[0]==0 and attacks[1]==0:
                if x!="1" and x!="2" and x!="3" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

            if attacks[0]==1 and attacks[1]==1:
                if x!="1" and x!="2" and x!="3" and x!="4" and x!="5" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

        os.system('cls')

        if x=="1":
            gracz.Swing()
        elif x=="2":
            gracz.Slay()
        elif x=="3":
            gracz.FreeAttack()
        elif x=="4":
            if attacks[0]==1:
                gracz.Hellforce()
            else:
                gracz.Brutalrage()
        elif x=="5":
            gracz.Brutalrage()            
        elif x=="M" or x=="m":
            gracz.Potions()

#========================================================

    def Swing(self):
        global p, q, zycie, obrazenia
        if self.points<2:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=2
            print("Rycerz używa ataku Swing!!")
            potwor.hp-=(3+upgrade[1])*q
            if potwor.hp<=0:
                gracz.KillMonster()
            else:
                print(f"Zabierasz {(3+upgrade[1])*q}HP!!")
                q=1
                potwor.MonsterAttack()

#========================================================

    def Slay(self):
        global p, q
        if self.points<3:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=3
            print("Rycerz używa ataku Slay!!")
            potwor.hp-=(2+upgrade[1])*q
            if potwor.hp<=0:
                gracz.KillMonster()
            else:
                print(f"Zabierasz {(2+upgrade[1])*q}HP i atakujesz ponownie!")
                gracz.PlayerAttack()

#========================================================

    def FreeAttack(self):
        global p, q, zycie, obrazenia
        print(f"Rycerz używa darmowego ataku!!")
        potwor.hp-=(1+upgrade[1])*q
        if potwor.hp<=0:
            gracz.KillMonster()
        else:
            print(f"Zabierasz {(1+upgrade[1])*q}HP!!")
            q=1
            potwor.MonsterAttack()

#========================================================

    def Hellforce(self):
        global p, q, zycie, obrazenia
        if self.points<6:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=6
            print("Rycerz używa ataku Hellforce!!")
            gracz.KillMonster()

#========================================================

    def Brutalrage(self):
        global p, q, zycie, obrazenia
        if self.points<6:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=6
            print("Rycerz używa ataku Brutalrage!!")
            print(f"Otrzymujesz dodatkowe {(10+upgrade[1])*q}HP i atakujesz ponownie!")
            gracz.hp+=(10+upgrade[1])*q
            gracz.PlayerAttack()

class tank(postac):
    
    def __init__(self):
        super().__init__("Tank", 10, 10, 0)

    def Instrukcja(self):
        os.system('cls')
        print("WYBRAŁEŚ TANKA!")
        print("Stawiaj czoła potworom, dzięki dodatkowym punktom życia!")
        print("Na start otrzymujesz 10 punktów obrony, używaj ich mądrze atakując przeciwników!")
        print(f"Twoje ataki: \n · Heal - regenerujesz 10HP i atakujesz ponownie, kosztuje 3 punkty obrony \n · Wall - zadajesz 3 obrażenia, kosztuje 2 punkty obrony!")
        print(f"Jeżeli nie stać cię na żaden atak, możesz zaatakować darmowym atakiem zabierając 1HP!")
        print("Statystyki potworów są zależne od zaawansowania gry.")
        print("Po pokonaniu przeciwnika twoje HP odnawia się do 10 oraz otrzymujesz 2 monety i 4 punkty obrony!")
        print("Za monety możesz kupować przeróżne mikstury, ulepszenia wyposażenia, a nawet dodatkowe ataki!")

#========================================================

    def PlayerAttack(self):
        global p, q, zycie, obrazenia  
        while True:
            print(f"\nStatystyki potwora \nHP: {potwor.hp}, CP: {potwor.cp} \n")
            print(f"Twoje statystyki \nHP: {gracz.hp}, mana: {self.points}")
            print(f"""
Którego ataku chcesz użyć? Możliwe ataki:
    1. Heal - regenerujesz {(10+upgrade[1])*q}HP i atakujesz ponownie: 3 punkty obrony
    2. Wall - {(3+upgrade[1])*q}CP: 2 punkt obrony
    3. Darmowy atak - {(1+upgrade[1])*q}CP""")
            u=0
            if attacks[0]==1:
                print(f"    {u+4}. Fusionblast - zabiera całe HP przeciwnika: 6 punktów obrony")
                u+=1                          
            if attacks[1]==1:
                print(f"    {u+4}. Datalife - {(3+upgrade[1])*q}CP, regenerujesz {(5+upgrade[1])*q}HP, atakujesz ponownie: 6 punkty obrony")

            print("\n    Wpisz M, aby użyć mikstur")

            x=input()

            if (attacks[0]==1 and attacks[1]==0) or (attacks[0]==0 and attacks[1]==1):
                if x!="1" and x!="2" and x!="3" and x!="4" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break
            
            if attacks[0]==0 and attacks[1]==0:
                if x!="1" and x!="2" and x!="3" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break

            if attacks[0]==1 and attacks[1]==1:
                if x!="1" and x!="2" and x!="3" and x!="4" and x!="5" and x!="M" and x!="m":
                    os.system('cls')
                    print("NIEPOPRAWNY NUMER!")
                    continue
                else:
                    break
 
        os.system('cls')
        
        if x=="1":
            gracz.Heal()
        elif x=="2":
            gracz.Wall()
        elif x=="3":
            gracz.FreeAttack()
        elif x=="4":
            if attacks[0]==1:
                gracz.Fusionblast()
            else:
                gracz.Datalife()
        elif x=="5":
            gracz.Datalife()            
        elif x=="M" or x=="m":
            gracz.Potions()

#========================================================

    def Heal(self):
        global p, q, zycie, obrazenia
        if self.points<3:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=3
            print("Tank używa ataku Heal!!")
            print(f"Otrzymujesz dodatkowe {(10+upgrade[1])*q}HP i atakujesz ponownie!")
            gracz.hp+=(10+upgrade[1])*q
            gracz.PlayerAttack()

#========================================================

    def Wall(self):
        global p, q, zycie, obrazenia
        if self.points<2:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=2
            print("Tank używa ataku Wall!!")
            potwor.hp-=(3+upgrade[1])*q
            if potwor.hp<=0:
                gracz.KillMonster()
            else:
                print(f"Zabierasz {(3+upgrade[1])*q}HP!!")
                q=1
                potwor.MonsterAttack()

#========================================================

    def FreeAttack(self):
        global p, q, zycie, obrazenia
        print(f"Tank używa darmowego ataku!!")
        potwor.hp-=(1+upgrade[1])*q
        if potwor.hp<=0:
            gracz.KillMonster()
        else:
            print(f"Zabierasz {(1+upgrade[1])*q}HP!!")
            q=1
            potwor.MonsterAttack()

#========================================================

    def Fusionblast(self):
        global p, q, zycie, obrazenia
        if self.points<6:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=6
            print("Tank używa ataku Fusionblast!!")
            gracz.KillMonster()

#========================================================

    def Datalife(self):
        global p, q, zycie, obrazenia
        if self.points<6:
            print("Nie stać cię na ten atak!")
            gracz.PlayerAttack()
        else:
            self.points-=6
            print("Tank używa ataku Datalife!!")
            gracz.hp+=(5+upgrade[1])*q
            potwor.hp-=(3+upgrade[1])*q
            if potwor.hp<=0:
                gracz.KillMonster()
            else:
                print(f"Otrzymujesz dodatkowe {(5+upgrade[1])*q}HP i zadajesz potworowi {(3+upgrade[1])*q}CP i atakujesz ponownie!")
                gracz.PlayerAttack()

#======================================================= 
 
os.system('cls')

while przegrana == False:

    while True:
        print("\nWITAJ W GRZE BLOODCHASE!\n")
        print("Wybierz postać:")
        print("1. TAJEMNICZY MAG")
        print("2. WALECZNY RYCERZ")
        print("3. NIEPOKONANY TANK")
        print("\n4. UŻYJ POPRZEDNIEGO ZAPISU\n")

        character= input("Co Wybierasz? (podaj liczbę) ")

        if character!="1" and character!="2" and character!="3" and character!="4":
            os.system('cls')
            print("NIEPOPRAWNY NUMER!")
            continue
        else:
            break

    potwor=monster(zycie, obrazenia)
        
    if character=="1":
        mag().Instrukcja()
        gracz=mag()

    elif character=="2":
        rycerz().Instrukcja()
        gracz=rycerz()

    elif character=="3":
        tank().Instrukcja()
        gracz=tank()
            
    elif character=="4":
        if len(zapisy)==0:
            os.system('cls')
            print("Nie masz żadnych zapisów!")
            continue

        else:
            os.system("cls")
            mag().UseRecord()
            try:
                gracz = gracz
            except NameError:
                continue    

    while przegrana == False:
        input("\n\nGotowy na wyprawę? Kliknij klawisz enter, aby rozpocząć przygodę!") 
        os.system('cls')

        potwor.Appear()