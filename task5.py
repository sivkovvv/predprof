import csv

def get_hash(name):
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alf += alf.upper()
    alf += ' '
    dictionary = {}
    for i in range(len(alf)):
        dictionary[alf[i]] = i + 1
    power = 1
    find_hash = 0
    p, m = 67, 10**9 + 9
    for i in range(len(name)):
        find_hash = (find_hash + dictionary[name[i]] * power) % m
        power = (power * p) % m
    return find_hash
        


    
    
    
