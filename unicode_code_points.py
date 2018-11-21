#! /usr/bin/python3

def hexadecimal_string(name):
    '''Програма виводить ім’я в бінарному представленні'''
    print(f"Ваше ім’я в шістнадцятковому представленні - {' '.join(hex(ord(x)) for x in name)}")


print("Натисніть 'Enter' для виходу з програми.")
while True:
    name = input("Введіть ваше ім'я: ")
    if name:
        hexadecimal_string(name)
    else:
        break
