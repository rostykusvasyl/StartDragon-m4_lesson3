#! /usr/bin/python3

def name_in_bytes(name):
    '''Програма виводить ім'я в байтах'''
    print(f"Ваше ім'я в байтах - {name.encode('utf-8')}")


print("Натисніть 'Enter' для виходу з програми.")
while True:
    name = input("Введіть ваше ім'я: ")
    if name:
        name_in_bytes(name)
    else:
        break
