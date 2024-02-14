import csv

with open('products.csv', encoding = 'utf-8-sig') as file:
    data = list(csv.reader(file, delimiter = ';'))[1:]
    for i in range(len(data)):
        poz = i
        product = data[i]
        while poz > 0 and data[poz - 1][0] > product[0]:
            data[poz] = data[poz - 1]
            poz -= 1
        data[poz] = product
    find_category = data[0][0]
    max_price_product = ''
    max_price_per_unit = 0
    for category, product, date, price_per_unit, count in data:
        if find_category in category:
            if max_price_per_unit < int(price_per_unit[:-2]):
                max_price_per_unit = int(price_per_unit[:-2])
                max_price_product = product
        else:
            break
    print(f'В категории: {find_category} самый дорогой товар: {max_price_product} его цена за единицу товара составляет {max_price_per_unit}')
