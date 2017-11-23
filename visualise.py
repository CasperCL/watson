import pandas
import matplotlib.pyplot as plt

X = pandas.read_csv('users_products.gen.csv')

# Hist
user_order_count = X.groupby('user_id').apply(lambda x: sum(x['orders'] ))
plt.hist(user_order_count, bins=100)
plt.xlabel('users')
plt.ylabel('orders')
plt.show()

# Hist
product_order_count = X.groupby('product_id').apply(lambda x: sum(x['orders'] ))
plt.hist(product_order_count, bins=100)
plt.xlabel('products')
plt.ylabel('orders')
plt.show()
