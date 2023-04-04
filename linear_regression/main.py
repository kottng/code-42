import numpy as np
import sympy as sp

import matplotlib.pyplot as plt

data_train = np.loadtxt('./train.txt', delimiter=',')
data_test = np.loadtxt('./test.txt', delimiter=',')

X_train = data_train[:,0]
y_train = data_train[:,1]

X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1) 

X_test = data_test[:,0]
y_test = data_test[:,1]

X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

#╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ

class LinearRegression:
    """
    k * x + b
    """
    def __init__(self):
        self.koeffs = None

    def fit(self, X, y):
        X = np.hstack((X, X**0))
        X_cross = np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T)  # ?  __ псевдообратные матрицы __  .pinv
        self.koeffs = np.matmul(X_cross, y).T[0]

    def predict(self, x):
        y_pred = self.koeffs[0] * x + self.koeffs[1] * 1
        return y_pred
    
    
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_prediction = [lr.predict(x) for x in X_train.T[0]]

def plot(x, y, x_prediction, y_prediction):
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    ax.plot(x_prediction, y_prediction)

    plt.show()
plot(X_train, y_train, X_train, lr_prediction)
