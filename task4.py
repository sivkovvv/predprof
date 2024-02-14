import csv

def make_promocode(name, date):
    '''
    функция создаёт промокод на основе названия продукта и его даты
    promocode - строка в которой будет храниться промокод для заданного имени и даты
    '''
    promocode = ''
    promocode += name[:2].upper()
    promocode += date[:2]
    promocode += str(name[-2:])[::-1].upper()
    promocode += str(date[3:5])[::-1]
    return promocode

with open('products.csv', encoding = 'utf-8-sig') as file:
    data = list(csv.reader(file, delimiter = ';'))[1:]
    for product in data:
        name = product[1]
        date = product[2]
        product.append(make_promocode(name, date))

with open('product_promo.csv', 'w', encoding = 'utf-8-sig') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writerows(data)
        
