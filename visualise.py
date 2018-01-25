import numpy as np
import pandas
import matplotlib.pyplot as plt

X = pandas.read_csv('users_products.gen.csv')

a = X.groupby(['product_id']).agg({'orders': np.sum})
top = a.sort_values(by='orders', ascending=False)[:10]

print(top)
