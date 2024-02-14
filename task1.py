import csv

with open('products.csv', encoding = 'utf-8-sig') as file:
    '''
    price_per_unit - цена за единицу товара
    count - количество проданного товара
    '''
    data = list(csv.reader(file, delimiter = ';'))[1:]
    for product in data:
        price_per_unit = product[-2][:-2]
        count = product[-1][:-2]
        product.append(int(price_per_unit) * int(count))
    find_product_sum = 0
    for category, product, date, price_per_unit, count, total in data:
        if 'Закуски' in category:
            find_product_sum += int(total)
    print(find_product_sum)
        
with open('products_new.csv', 'w', encoding = 'utf-8-sig') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    writer.writerows(data)
    
