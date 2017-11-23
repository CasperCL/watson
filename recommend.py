from math import sqrt

import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def preprocess(data, n_users, n_items):
    matrix = np.zeros((n_users, n_items))
    for line in data.itertuples():
        matrix[line[1]-1, line[2]-1] = line[3]
    return matrix


def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))


df = pd.read_csv('users_products.gen.csv')

n_users = df.user_id.unique().shape[0]
n_items = max(df.product_id)  # note: a remap of the indexes might prove to be more efficient.
print('Number of users = ' + str(n_users) + ' | Number of product = ' + str(n_items))

train_data, test_data = train_test_split(df, test_size=0.25)

# Feature scaling for the rating.
scaler = MinMaxScaler()
df[['orders']] = scaler.fit_transform(df[['orders']])

train_data_matrix = preprocess(train_data, n_users, n_items)
test_data_matrix = preprocess(test_data, n_users, n_items)

# Get SVD components from train matrix. Choose k.
u, s, vt = svds(train_data_matrix, k = 4)
s_diag_matrix=np.diag(s)
X_pred = np.dot(np.dot(u, s_diag_matrix), vt)
print('User-based CF RMSE: ' + str(rmse(X_pred, test_data_matrix)))
