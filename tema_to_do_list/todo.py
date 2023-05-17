from operator import itemgetter
from datetime import datetime

def citeste_categorii():
    with open('categorii.txt', 'r') as file:
        categorii = file.read().splitlines()
    return categorii

def afiseaza_categorii():
    categorii = citeste_categorii()
    print(f"Categoriile disponibile sunt:\n {' '.join(categorii)}")

def afiseaza_taskuri():
    with open('taskuri.txt', 'r') as file:
        taskuri = file.read().splitlines()
    print('Alege metoda de sortare a task-urilor afisate mai jos:\n')
    taskuri_ordered = [task.split(',') for task in taskuri]
    alegere_sortare = int(input('1. sortare ascendentă task\n2. sortare descendentă task\n3. sortare ascendentă data\n4. sortare descendentă data\n5. sortare ascendentă persoana responsabilă\n6. sortare descendentă persoană responsabilă\n7. sortare ascendentă categorie\n8. sortare descendentă categorie:\n'))
    if alegere_sortare == 1:
        res = sorted(taskuri_ordered, key=itemgetter(0), reverse=False)
    elif alegere_sortare == 2:
        res = sorted(taskuri_ordered, key=itemgetter(0), reverse=True)
    elif alegere_sortare == 3:
        res = sorted(taskuri_ordered, key=lambda x: datetime.strptime(x[1].strip(), '%d.%m.%Y %H:%M') if len(x) > 1 and x[1].strip() != "test" else datetime.max, reverse=False)
    elif alegere_sortare == 4:
        res = sorted(taskuri_ordered, key=lambda x: datetime.strptime(x[1].strip(), '%d.%m.%Y %H:%M') if len(x) > 1 and x[1].strip() != "test" else datetime.min, reverse=True)
    elif alegere_sortare == 5:
        res = sorted(taskuri_ordered, key=itemgetter(2), reverse=False)
    elif alegere_sortare == 6:
        res = sorted(taskuri_ordered, key=itemgetter(2), reverse=True)
    elif alegere_sortare == 7:
        res = sorted(taskuri_ordered, key=itemgetter(3), reverse=False)
    elif alegere_sortare == 8:
        res = sorted(taskuri_ordered, key=itemgetter(3), reverse=True)
    print('\n'.join(' '.join(map(str, sl)) for sl in res))


def adauga_categorie():
    categorii = citeste_categorii()
    categorie_noua = input('Introdu noua categorie:')
    if categorie_noua in categorii:
        print('Categoria pe care vrei sa o adaugi exista deja.')
        print(f'Categoriile existente sunt: {categorii}.')
        return

    with open('categorii.txt', 'a') as file:
        file.write(f"{categorie_noua}\n")

    print(f'A fost adaugata categoria {categorie_noua}.')


def adauga_task():
    with open('categorii.txt', 'r') as file1:
        categorii = file1.read().splitlines()
    with open('taskuri.txt', 'r+') as file:
        taskuri = input('Introdu task-ul in formatul "[nume task], [DD.MM.YYYY HH:MM] [nume persoana responsabila] [categorie]: ')
        taskuri_check = taskuri.split(",")
        read_taskuri = file.read().splitlines()
        if len(taskuri_check) != 4:
            print('Formatul task-ului introdus este incorect.')
            return
        try:
            datetime.strptime(taskuri_check[1].strip(), '%d.%m.%Y %H:%M')
        except ValueError:
            print('Data introdusă nu respectă formatul corect. Asigură-te că utilizezi formatul DD.MM.YYYY HH:MM.')
            return
        if taskuri_check[3].strip() not in categorii:
            print('Categoria pe care încerci să o adaugi nu există.')
            print(f'Categoriile disponibile sunt: {categorii}')
            return
        if taskuri_check[0] in read_taskuri:
            print('Task-ul pe care vrei să-l adaugi există deja.')
            return
        file.write(f"{taskuri}\n")
    print(f'A fost adăugat task-ul: {taskuri}.')




while True:
    alegere = int(input('Alege dintre urmatoarele optiuni:\n1. Adauga categorii\n2. Adauga taskuri\n3. Afiseaza categoriile\n4. Afiseaza taskurile\n0. Exit\n'))

    if alegere == 1:
        adauga_categorie()
    elif alegere == 2:
        adauga_task()
    elif alegere == 3:
        afiseaza_categorii()
    elif alegere == 4:
        afiseaza_taskuri()
    elif alegere == 0:
        break