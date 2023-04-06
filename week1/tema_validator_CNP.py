string_CNP = list(input("Introdu CNP-ul pe care doresti sa il verifici:"))
CNP = [] #initializez o lista in care o sa introduc pe rand toate elementele din input
         #dupa ce au fost convertite ca numere, folosind for-ul de mai jos

try:
    #convertim elementele listei din string in number
    for i in string_CNP:
        n = int(i)
        CNP.append(n)

    if CNP[0] != 0:
        if len(CNP) == 13:
            LL = CNP[3:5]#lista formata din cele doua cifre care alcatuiesc codul lunii (LL)
            LL = int(str(LL[0]) + str(LL[1]))#convertesc lista intr-un number
            #verific codul lunii
            if LL <= 12:
                ZZ = CNP[5:7]#lista formata din cele doua cifre care alcatuiesc codul zilei (ZZ)
                ZZ = int(str(ZZ[0]) + str(ZZ[1]))#convertesc lista intr-un number
                #verific codul zilei
                if ZZ <= 31:
                    JJ = CNP[7:9]  # lista formata din cele doua cifre care alcatuiesc codul judetului (JJ)
                    JJ = int(str(JJ[0]) + str(JJ[1]))  # convertesc lista intr-un number
                    #verific codul judetului
                    if JJ <= 52:
                        #verific cifra de control
                        C = 2 * CNP[0] + 7 * CNP[1] + 9 * CNP[2] + 1 * CNP[3] + 4 * CNP[4] + 6 * CNP[5] + 3 * CNP[6] + 5 * CNP[7] + 8 * CNP[8] + 2 * CNP[9] + 7 * CNP[10] + 9 * CNP[11]
                        rest = C % 11
                        if (CNP[12] == 1) and (rest == 10):
                            print("CNP-ul este valid.")
                        elif CNP[12] == 9 and rest == 9:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 8 and rest == 8:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 7 and rest == 7:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 6 and rest == 6:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 5 and rest == 5:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 4 and rest == 4:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 3 and rest == 3:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 2 and rest == 2:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 1 and rest == 1:
                            print("CNP-ul este valid.")
                        elif CNP[12] == 0 and rest == 0:
                            print("CNP-ul este valid.")
                        else:
                            print("Cifra de control este gresita. CNP-ul nu este valid.")
                    else:
                        print("Codul judetului este gresit.")
                else:
                    print("Codul zilei este gresit.")
            else:
                print("Codul lunii este gresit.")

        else:
            print("CNP-ul introdus nu are exact 13 cifre.")
    else:
        print("CNP-ul nu poate sa inceapa cu cifra 0")

except ValueError:
    print("CNP-ul nu poate contine litere.")

