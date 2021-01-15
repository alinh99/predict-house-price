import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

houses = pd.read_csv("house-prices.csv")
sqrt = list(houses.SqFt.values)
x1 = np.array([sqrt]).T
bed = list(houses.Bedrooms.values)
x2 = np.array([bed]).T
bathroom = list(houses.Bathrooms.values)

price = list(houses.Price.values)
y = np.array([price]).T
# A = np.dot(Xbar.T, Xbar)
# b = np.dot(Xbar.T, y)

one = np.ones((x1.shape[0], 1))
X = np.concatenate((x1, x2, one), axis=1)

A = np.dot(X.T, X)
b = np.dot(X.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)

square = float(input("Nhập diện tích: "))
bed = int(input("Nhập số giường ngủ: "))

housesPrice = w[0][0] * square + w[1][0]*bed + w[2][0]
print("Giá tiền của căn nhà: %.2f" % housesPrice + '$')
