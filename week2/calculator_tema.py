def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    return a / b


rezultat = 0
operatie = ''
operatii_valide = ['+', '-', '*', '/']

while True:
    #afisam meniul
    print('Operatii disponibile: +, -, *, /, C (stergere)')
    print('Rezultat curent: ', rezultat)
    #citim inputul utilizatorului
    intrare = input('Introduceti cifra sau operatia: ')
    #verificam daca inputul este valid
    if intrare.isdigit():
        #dacă este cifra, convertim in int
        intrare = int(intrare)
        #verificam daca avem o operatie in asteptare
        if operatie == '':
            #daca nu avem, setam rezultatul ca fiind cifra introdusa
            rezultat = intrare
        else:
            #daca avem, aplicam operatia corespunzatoare si actualizam rezultatul
            if operatie == '+':
                rezultat = adunare(rezultat, intrare)
            elif operatie == '-':
                rezultat = scadere(rezultat, intrare)
            elif operatie == '*':
                rezultat = inmultire(rezultat, intrare)
            elif operatie == '/':
                #verificam daca incercam sa impartim la 0
                if intrare == 0:
                    print('Nu putem imparti la 0!')
                else:
                    rezultat = impartire(rezultat, intrare)
            #resetam operatia
            operatie = ''
    elif intrare in operatii_valide:
        #daca inputul este o operatie valida, o așteptam pentru a o aplica ulterior
        operatie = intrare
    elif intrare == 'C':
        #daca inputul este C, resetam totul
        rezultat = 0
        operatie = ''
    else:
        #daca inputul nu este valid, afisam un mesaj de eroare
        print('Input invalid!')
