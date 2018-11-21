#! /usr/bin/python3

def name_in_binary(name):
    '''Програма виводить ім’я в бінарному представленні'''
    print(f"Ваше ім’я в бінарному представленні - {' '.join(format(ord(x), 'b') for x in name)}")


print("Натисніть 'Enter' для виходу з програми.")
while True:
    name = input("Введіть ваше ім'я: ")
    if name:
        name_in_binary(name)
    else:
        break
