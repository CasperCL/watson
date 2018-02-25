import sys
import csv
import random
import enum

import mimesis


N_USERS = 1000
N_PRODUCTS = 5000
PRODUCTS_FILE = 'products.csv'
USERS_FILE = 'users.gen.csv'
BUY_HISTORY_FILE = 'users_products.gen.csv'


class UserType(enum.Enum):
    BULK_INFREQUENT = 0
    BULK_FREQUENT = 1
    SMALL_FREQUENT = 2
    SMALL_INFREQUENT = 3


class Product:
    def __init__(self, id, name, brand):
        self.id = id
        self.name = name
        self.brand = brand


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.type = random.choice(list(UserType))

    def buy(self, products):
        order = []
        if self.type == UserType.BULK_INFREQUENT:
            for i in range(4, 8):
                order += [random.choice(products)] * random.randint(10, 20)
        if self.type == UserType.BULK_FREQUENT:
            for i in range(15, 40):
                order += [random.choice(products)] * random.randint(10, 20)
        if self.type == UserType.SMALL_INFREQUENT:
            for i in range(4, 8):
                order += [random.choice(products)] * random.randint(2, 10)
        if self.type == UserType.SMALL_FREQUENT:
            for i in range(15, 40):
                order += [random.choice(products)] * random.randint(2, 10)
        return order

def generate_users(limit: int):
    person_generator = mimesis.Personal('nl')
    users = []
    for i in range(0, limit):
        name = person_generator.full_name()
        users.append(User(i, name))
    return users

def read_products(products_file, limit=None):
    products = []
    valid_product_counter = 0
    with open(products_file, encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        for index, product_csv in enumerate(reader):
            ean = product_csv[header.index('EANNummer')].strip()
            name = product_csv[header.index('NaamRek')]
            brand = product_csv[header.index('Merk')]
            if not ean:
                continue
            products.append(Product(valid_product_counter, name, brand))
            valid_product_counter += 1
            if limit is not None and valid_product_counter >= limit:
                break
    return products

if __name__ == '__main__':
    users = generate_users(N_USERS)
    products = read_products(PRODUCTS_FILE, N_PRODUCTS)

    with open(USERS_FILE, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'brand'])
        for user in users:
            writer.writerow([user.id, user.name, user.type.value])

    products = products[:N_PRODUCTS]
    with open(BUY_HISTORY_FILE, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'product_id', 'orders'])
        for user in users:
            order = user.buy(products)
            p_ids = set()
            for product in order:
                if product.id not in p_ids:
                    rating = order.count(product)
                    p_ids.add(product.id)
                    writer.writerow([user.id, product.id, rating])


