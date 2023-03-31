
nula = 0
vzorec1 = ('Hustota látky - ρ = m/V (ρ-kg/m3, m-kg, V-m3), \nRychlost rovnoměrného pohybu - v = s/t (v- m/s, s-m, t-s), \nGravitační síla - Fg = m*g (Fg-N, m-kg, g = 10N/kg), \nTlak - p = F/S (p-Pa, F-N, S-m2), \nMechanická práce - W = F*s (W- J, F-N, s-m), \nVýkon - P = W/t (P-W, W-J, t-s), \nVýkon - P = F*v (P-W, F-N, v-m/s), \nVýhřevnost paliva - h = Q/m (h-J/kg,Q-J,m-kg), \nSkupenské teplo tání - Lt = lt*m (Lt-J,lt-J/kg,m-kg), \nSkupenské teplo varu - Lv = lv*m (Lv-J,lv-J/kg,m-kg), \nElektrický odpor vodiče - R = U/I (R-Ω,U-V,I-A)')
vzorce_seznam = vzorec1

#vzorce - čísla
číslo1m = 0
číslo2Q = 0
číslo3h = 0
číslo4ρ = 0
číslo5V = 0
číslo6v = 0
číslo7s = 0
číslo8t = 0
číslo9Fg = 0
číslo10p = 0
číslo11F = 0
číslo12S = 0
číslo13W = 0
číslo14P = 0
číslo15Lt = 0
číslo16lt = 0
číslo17Lv = 0
číslo18lv = 0
číslo19I = 0
číslo20R = 0
číslo21U = 0
číslo22g = 10
seznam_čísla = [číslo1m, číslo2Q, číslo3h]
print("Nabídka pro program Fyzikální vzorce:")
print("Jednotky, které používá tento program jsou kg, m, m2, m3, s, N, J, C, V, A, Ω, kg/m3, m/s, Pa, W, J/kg ")
print("Jiné jednotky program nepoužívá!")
print("Zadejte jen samotné číslo bez podporovaných jednotek")
print("Dávejte pozor na velké a malé písmena!")
print("Zadejte 'kontrola' pro zjištění jaké veličiny byly zadány (jen při zadání veličin (písmeno))")
print("Zadejte 'vzorce' pro zjištění dostupných vzorců a zkontrolujte si jaké vzorce můžeš vypočítat")
print("Pro ukončení zadej: 'konec'")





















while True:
    hodnota1 = input("Zadej první známou veličinu (její písmeno)")
    while hodnota1 == ("m") or ("Q") or ("g") or ("h") or ("ρ") or ("V") or ("v") or ("s") or ("t") or ("Fg") or ("p") or ("F") or ("S") or ("W") or ("P") or ("Lt") or ("lt") or ("Lv") or ("lv") or ("I") or ("R") or ("U") or ("konec"): 
        
        hodnota2 = ("nezadaná veličina")
        hodnota3 = ("nezadaná veličina")
        if hodnota1 == ("m"):
            číslo1m = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif hodnota1 == ("Q"):
            číslo2Q = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif hodnota1 == ("h"):
            číslo3h = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("ρ"):
            číslo4ρ = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("V"):
            číslo5V = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("v"):
            číslo6v = int(input("Teď zadej její hodnotu (číslo)"))
            break    
        elif  hodnota1 == ("d"):
            číslo7s = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("t"):
            číslo8t = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("Fg"):
            číslo9Fg = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("p"):
            číslo10p = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("F"):
            číslo11F = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("S"):
            číslo12S = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("W"):
            číslo13W = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("P"):
            číslo14P = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("Lt"):
            číslo15Lt = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("lt"):
            číslo16lt = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("Lv"):
            číslo17Lv = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("lv"):
            číslo18lv = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("I"):
            číslo19I = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("R"):
            číslo20R = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("U"):
            číslo21U = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("g"):
            číslo22g = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota1 == ("konec"):
            exit();



    #kontrola
        elif hodnota1 == ('kontrola'):
            hodnota1 = ("nezadaná veličina")
            seznam1 = [hodnota1, hodnota2, hodnota3]
            print(seznam1, seznam_čísla)
        elif hodnota1 == ("vzorce"):
            print(vzorce_seznam)
            
        hodnota1 = input("Zadej první známou veličinu (její písmeno)")
    else: 
        print("Nerozumím")
        

    hodnota2 = input("Zadej druhou známou veličinu (její písmeno)")
    while hodnota2 == ("m") or ("Q") or ("g") or ("h") or ("ρ") or ("V") or ("v") or ("s") or ("t") or ("Fg") or ("p") or ("F") or ("S") or ("W") or ("P") or ("Lt") or ("lt") or ("Lv") or ("lv") or ("I") or ("R") or ("U") or ("konec"):
        seznam_čísla = [číslo1m, číslo2Q, číslo3h]
        seznam2 = [hodnota1, hodnota2]
        if hodnota2 == ("m"):
            číslo1m = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("Q"):
            číslo2Q = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif hodnota2 == ("h"):
            číslo3h = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("ρ"):
            číslo4ρ = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("V"):
            číslo5V = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("v"):
            číslo6v = int(input("Teď zadej její hodnotu (číslo)"))
            break    
        elif  hodnota2 == ("d"):
            číslo7s = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("t"):
            číslo8t = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("Fg"):
            číslo9Fg = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("p"):
            číslo10p = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("F"):
            číslo11F = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("S"):
            číslo12S = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("W"):
            číslo13W = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("P"):
            číslo14P = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("Lt"):
            číslo15Lt = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("lt"):
            číslo16lt = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("Lv"):
            číslo17Lv = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("lv"):
            číslo18lv = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("I"):
            číslo19I = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("R"):
            číslo20R = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("U"):
            číslo21U = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("g"):
            číslo22g = int(input("Teď zadej její hodnotu (číslo)"))
            break
        elif  hodnota2 == ("konec"):
            exit();



        elif hodnota1 == hodnota2:
            print("Zadal jsi dvě stejné hodnoty :/")

        elif hodnota2 == ("vzorce"):
            print(vzorce_seznam)
            hodnota1 = input("Zadej první známou veličinu (její písmeno)")
        



        
        elif hodnota2 == ("kontrola"):
            hodnota2 = ("nezadaná veličina")
            hodnota3 = ("nezadaná veličina") 
            if číslo1m > 0:
                seznam_čísla1 = číslo1m
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla1, nula, nula)
            elif číslo2Q > 0:
                seznam_čísla2 = číslo2Q
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla2, nula, nula)
            elif číslo3h > 0:
                seznam_čísla3 = číslo3h
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla3, nula, nula)
            elif číslo4ρ > 0:
                seznam_čísla4 = číslo4ρ
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla4, nula, nula)
            elif číslo5V > 0:
                seznam_čísla5 = číslo5V
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla5, nula, nula)
            elif číslo6v > 0:
                seznam_čísla6 = číslo6v
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla6, nula, nula)
            elif číslo7s > 0:
                seznam_čísla7 = číslo7s
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla7, nula, nula)
            elif číslo8t > 0:
                seznam_čísla8 = číslo8t
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla8, nula, nula)
            elif číslo9Fg > 0:
                seznam_čísla9 = číslo9Fg
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla9, nula, nula)
            elif číslo10p > 0:
                seznam_čísla10 = číslo10p
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla10, nula, nula)
            elif číslo11F > 0:
                seznam_čísla11 = číslo11F
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla11, nula, nula)
            elif číslo12S > 0:
                seznam_čísla12 = číslo12S
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla12, nula, nula)
            elif číslo13W > 0:
                seznam_čísla13 = číslo13W
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla13, nula, nula)
            elif číslo14P > 0:
                seznam_čísla14 = číslo14P
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla14, nula, nula)
            elif číslo15Lt > 0:
                seznam_čísla15 = číslo15Lt
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla15, nula, nula)
            elif číslo16lt > 0:
                seznam_čísla16 = číslo16lt
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla16, nula, nula)
            elif číslo17Lv > 0:
                seznam_čísla17 = číslo17Lv
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla17, nula, nula)
            elif číslo18lv > 0:
                seznam_čísla18 = číslo18lv
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla18, nula, nula)
            elif číslo19I > 0:
                seznam_čísla19 = číslo19I
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla19, nula, nula)
            elif číslo20R > 0:
                seznam_čísla20 = číslo20R
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla20, nula, nula)
            elif číslo21U > 0:
                seznam_čísla21 = číslo21U
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla21, nula, nula)


            elif číslo22g > 0:
                seznam_čísla22 = číslo22g
                seznam2 = [hodnota1, hodnota2, hodnota3]
                print(seznam2, seznam_čísla22, nula, nula)
            #seznam_čísla = seznam_čísla1 + seznam_čísla2 + seznam_čísla3 + seznam_čísla4 + seznam_čísla5 + seznam_čísla6 + seznam_čísla7 + seznam_čísla8 + seznam_čísla9 + seznam_čísla10 + seznam_čísla11 + seznam_čísla12 + seznam_čísla13 + seznam_čísla14 + seznam_čísla15 + seznam_čísla16 + seznam_čísla17 + seznam_čísla18 + seznam_čísla19 + seznam_čísla20 + seznam_čísla21 
            #seznam2 = [hodnota1, hodnota2]
            #print(seznam2, seznam_čísla, nula)
        
            
        else:
            print("Nerozumím")
        hodnota2 = input("Zadej druhou známou veličinu (její písmeno)")


    hodnota3 = input("Zadej třetí známou veličinu, kterou chceš vypočítat ")

    while hodnota3 == ("m") or ("Q") or ("g") or ("h") or ("ρ") or ("V") or ("v") or ("s") or ("t") or ("Fg") or ("p") or ("F") or ("S") or ("W") or ("P") or ("Lt") or ("lt") or ("Lv") or ("lv") or ("I") or ("R") or ("U"):
        seznam3 = [hodnota1, hodnota2, hodnota3]
        if hodnota3 == ("m"): # prodloužit 5x
            if hodnota2 == ("V"):
                vysledek1 = číslo5V * číslo4ρ
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("ρ"):
                vysledek1 = číslo5V * číslo4ρ
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("Fg"):
                vysledek1 = číslo9Fg / číslo22g
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("g"):
                vysledek1 = číslo9Fg / číslo22g
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("h"):
                vysledek1 = číslo2Q / číslo3h
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("Q"):
                vysledek1 = číslo2Q / číslo3h
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("Lt"):
                vysledek1 = číslo15Lt / číslo16lt
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("lt"):
                vysledek1 = číslo15Lt / číslo16lt
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("Lv"):
                vysledek1 = číslo17Lv / číslo16lt
                celkem = vysledek1
                print(celkem, "kg")
                break
            elif hodnota2 == ("lt"):
                vysledek1 = číslo15Lt / číslo16lt
                celkem = vysledek1
                print(celkem, "kg")
                break

        elif hodnota3 == ("Q"): # 1x
            
            if hodnota2 == ("h"):
                vysledek1 = číslo3h * číslo1m
                celkem = vysledek1
                print(celkem, "J")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo3h * číslo1m
                celkem = vysledek1
                print(celkem, "J")
                break
        elif hodnota3 == ("h"): #1x
            if hodnota2 == ("Q"):
                vysledek1 = číslo2Q / číslo1m
                celkem = vysledek1
                print(celkem, "J/kg")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo2Q / číslo1m
                celkem = vysledek1
                print(celkem, "J/kg")
                break
            
        elif hodnota3 == ("ρ"): #1x
            if hodnota2 == ("m"):
                vysledek1 = číslo1m / číslo5V
                celkem = vysledek1
                print(celkem, "Kg/m3")
                break
            elif hodnota2 == ("V"):
                vysledek1 = číslo1m / číslo5V
                celkem = vysledek1
                print(celkem, "kg/m3")
                break
            
        elif hodnota3 == ("V"): # 1x
            if hodnota2 == ("m"):
                vysledek1 = číslo1m / číslo4ρ
                celkem = vysledek1
                print(celkem, "m3")
                break
            elif hodnota2 == ("ρ"):
                vysledek1 = číslo1m / číslo4ρ
                celkem = vysledek1
                print(celkem, "m3")
                break
            
        elif hodnota3 == ("v"): # 2x
            if hodnota2 == ("s"):
                vysledek1 = číslo7s / číslo8t
                celkem = vysledek1
                print(celkem, "m/s")
                break
            elif hodnota2 == ("t"):
                vysledek1 = číslo7s / číslo8t
                celkem = vysledek1
                print(celkem, "m/s")
                break
            elif hodnota2 == ("P"):
                vysledek1 = číslo14P / číslo11F
                celkem = vysledek1
                print(celkem, "m/s")
                break
            elif hodnota2 == ("F"):
                vysledek1 = číslo14P / číslo11F
                celkem = vysledek1
                print(celkem, "m/s")
                break
            
            
        elif hodnota3 == ("s"): # 2x
            if hodnota2 == ("v"):
                vysledek1 = číslo6v * číslo8t
                celkem = vysledek1
                print(celkem, "m")
                break
            elif hodnota2 == ("t"):
                vysledek1 = číslo6v * číslo8t
                celkem = vysledek1
                print(celkem, "m")
                break
            elif hodnota2 == ("F"):
                vysledek1 = číslo13W / číslo11F
                celkem = vysledek1
                print(celkem, "m")
                break
            elif hodnota2 == ("W"):
                vysledek1 = číslo13W / číslo11F
                celkem = vysledek1
                print(celkem, "m")
                break
            
        elif hodnota3 == ("t"): # 2x
            if hodnota2 == ("s"):
                vysledek1 = číslo7s / číslo6v
                celkem = vysledek1
                print(celkem, "s")
                break
            elif hodnota2 == ("v"):
                vysledek1 = číslo7s / číslo6v
                celkem = vysledek1
                print(celkem, "s")
                break
            elif hodnota2 == ("W"):
                vysledek1 = číslo13W / číslo14P
                celkem = vysledek1
                print(celkem, "s")
                break
            elif hodnota2 == ("P"):
                vysledek1 = číslo13W / číslo14P
                celkem = vysledek1
                print(celkem, "s")
                break
            
        elif hodnota3 == ("Fg"): #1x
            
            if hodnota2 == ("m"):
                vysledek1 = číslo1m * číslo22g
                celkem = vysledek1
                print(celkem, "N")
                break
            elif hodnota2 == ("ρ"):
                vysledek1 = číslo1m * číslo22g
                celkem = vysledek1
                print(celkem, "N")
                break
        elif hodnota3 == ("p"): #1x
            
            if hodnota2 == ("F"):
                vysledek1 = číslo11F / číslo12S
                celkem = vysledek1
                print(celkem, "Pa")
                break
            elif hodnota2 == ("S"):
                vysledek1 = číslo11F / číslo12S
                celkem = vysledek1
                print(celkem, "Pa")
                break
        elif hodnota3 == ("F"): #3x
            
            if hodnota2 == ("p"):
                vysledek1 = číslo10p * číslo12S
                celkem = vysledek1
                print(celkem, "N")
                break
            elif hodnota2 == ("S"):
                vysledek1 = číslo10p * číslo12S
                celkem = vysledek1
                print(celkem, "N")
                break
            elif hodnota2 == ("W"):
                vysledek1 = číslo13W / číslo7s
                celkem = vysledek1
                print(celkem, "N")
                break
            elif hodnota2 == ("s"):
                vysledek1 = číslo13W / číslo7s
                celkem = vysledek1
                print(celkem, "N")
                break
            elif hodnota2 == ("P"):
                vysledek1 = číslo14P / číslo6v
                celkem = vysledek1
                print(celkem, "N")
                break
            elif hodnota2 == ("v"):
                vysledek1 = číslo14P / číslo6v
                celkem = vysledek1
                print(celkem, "N")
                break
        elif hodnota3 == ("S"): #1x
            if hodnota2 == ("F"):
                vysledek1 = číslo11F / číslo12S
                celkem = vysledek1
                print(celkem, "m2")
                break
            elif hodnota2 == ("p"):
                vysledek1 = číslo11F / číslo12S
                celkem = vysledek1
                print(celkem, "m2")
                break
            
        elif hodnota3 == ("W"): #2x
            
            if hodnota2 == ("F"):
                vysledek1 = číslo11F * číslo7s
                celkem = vysledek1
                print(celkem, "J")
                break
            elif hodnota2 == ("s"):
                vysledek1 = číslo11F * číslo7s
                celkem = vysledek1
                print(celkem, "J")
                break
            elif hodnota2 == ("P"):
                vysledek1 = číslo14P * číslo8t
                celkem = vysledek1
                print(celkem, "J")
                break
            elif hodnota2 == ("t"):
                vysledek1 = číslo14P * číslo8t
                celkem = vysledek1
                print(celkem, "J")
                break
        elif hodnota3 == ("P"): #2x
            
            
            if hodnota2 == ("W"):
                vysledek1 = číslo13W / číslo8t
                celkem = vysledek1
                print(celkem, "W")
                break
            elif hodnota2 == ("t"):
                vysledek1 = číslo13W / číslo8t
                celkem = vysledek1
                print(celkem, "W")
                break
            elif hodnota2 == ("F"):
                vysledek1 = číslo11F * číslo6v
                celkem = vysledek1
                print(celkem, "W")
                break
            elif hodnota2 == ("v"):
                vysledek1 = číslo11F * číslo6v
                celkem = vysledek1
                print(celkem, "W")
                break
        elif hodnota3 == ("Lt"): #1x
            
            if hodnota2 == ("lt"):
                vysledek1 = číslo16lt * číslo1m
                celkem = vysledek1
                print(celkem, "J")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo16lt * číslo1m
                celkem = vysledek1
                print(celkem, "J")
                break
        elif hodnota3 == ("lt"): #1x
            if hodnota2 == ("Lt"):
                vysledek1 = číslo15Lt / číslo1m
                celkem = vysledek1
                print(celkem, "J/kg")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo15Lt / číslo1m
                celkem = vysledek1
                print(celkem, "J/kg")
                break
            
        elif hodnota3 == ("Lv"): #1x
            if hodnota2 == ("lv"):
                vysledek1 = číslo18lv * číslo1m
                celkem = vysledek1
                print(celkem, "J")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo18lv * číslo1m
                celkem = vysledek1
                print(celkem, "J")
                break

        elif hodnota3 == ("lv"): #1x
            if hodnota2 == ("Lv"):
                vysledek1 = číslo17Lv / číslo1m
                celkem = vysledek1
                print(celkem, "J/kg")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo17Lv / číslo1m
                celkem = vysledek1
                print(celkem, "J/kg")
                break
            
        elif hodnota3 == ("I"): #1x
            if hodnota2 == ("U"):
                vysledek1 = číslo21U / číslo20R
                celkem = vysledek1
                print(celkem, "A")
                break
            elif hodnota2 == ("R"):
                vysledek1 = číslo21U / číslo20R
                celkem = vysledek1
                print(celkem, "A")
                break
            
        elif hodnota3 == ("R"): #1x
            if hodnota2 == ("U"):
                vysledek1 = číslo21U / číslo19I
                celkem = vysledek1
                print(celkem, "Ω")
                break
            elif hodnota2 == ("I"):
                vysledek1 = číslo21U / číslo19I
                celkem = vysledek1
                print(celkem, "Ω")
                break
            
        elif hodnota3 == ("U"): #1x
            
            if hodnota2 == ("R"):
                vysledek1 = číslo20R * číslo19I
                celkem = vysledek1
                print(celkem, "V")
                break
            elif hodnota2 == ("I"):
                vysledek1 = číslo20R * číslo19I
                celkem = vysledek1
                print(celkem, "V")
                break
        elif hodnota3 == ("g"): # 1x
            if hodnota2 == ("Fg"):
                vysledek1 = číslo9Fg / číslo1m
                celkem = vysledek1
                print(celkem, "N/Kg")
                break
            elif hodnota2 == ("m"):
                vysledek1 = číslo9Fg / číslo1m
                celkem = vysledek1
                print(celkem, "N/Kg")
                break













        elif hodnota3 == ("kontrola"):
                hodnota3 = ("nezadaná veličina") 
                seznam3 = [hodnota1, hodnota2, hodnota3]
                seznam_čísla = [číslo1m, číslo2Q, číslo3h]
                print(seznam3, seznam_čísla)
            
        elif hodnota3 == hodnota2:
            print("Zadal jsi dvě stejné hodnoty :/")
        elif hodnota3 == hodnota1:
            print("Zadal jsi dvě stejné hodnoty :/")
        
        hodnota3 = input("Zadej třetí známou veličinu, kterou chceš vypočítat")
        
    else:
        print("Nerozumím")




