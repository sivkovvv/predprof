import csv

with open('products.csv', encoding = 'utf-8-sig') as file:
    data = list(csv.reader(file, delimiter = ';'))[1:]
    find_category = input()
    while find_category != 'молоко':
        products_all = {}
        for category, product, date, price_per_unit, count in data:
            if find_category in category:
                if product in products_all:
                    products_all[product] += int(count[:-2]) 
                else:
                    products_all[product] = int(count[:-2]) 

        name_minimum_product = ''
        count_minimum_product = 10**9
        for i in products_all:
            if products_all[i] < count_minimum_product:
                name_minimum_product = i
                count_minimum_product = products_all[i]
        
        if len(name_minimum_product) == 0:
            print('Такой категории не существует в нашей БД')
        else:
            print(f'В категории: {find_category} товар: {name_minimum_product} был куплен {count_minimum_product} раз')
        find_category = input()
