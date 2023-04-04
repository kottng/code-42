import numpy as np
import matplotlib.pyplot as plt

data_train = np.loadtxt('train.txt', delimiter=',')
data_test = np.loadtxt('test.txt', delimiter=',')

X_train = data_train[:,0]
y_train = data_train[:,1]

X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)

X_test = data_test[:,0]
y_test = data_test[:,1]

X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

class PolynomialRegression:
    def __init__(self, degree):
        if degree < 1:
            raise ValueError('Разве?')
        self.degree = degree
        self.coeffs = 0

    def fit(self, X, y):
        _X = X**0
        
        # Добавим нужные степени
        for i in range(1, self.degree + 1):  # с чего до чего, не включая последнее
            _X = np.hstack((X**i, _X))
        
        X_cross = np.matmul(np.linalg.pinv(np.matmul(_X.T, _X)), _X.T)
        
        # print(f'Умножаем {X_cross.shape} x {y.shape}')
        
        self.coeffs = np.matmul(X_cross, y)

    def predict(self, X):
        _X = X**0
        # Опять добавим нужные степени | Главное в том же порядке что и в fit
        for i in range(1, self.degree + 1):  # с чего до чего, не включая последнее
            _X = _X = np.hstack((X**i, _X))
        y_pred = _X * self.coeffs.T[0]
        return np.sum(y_pred, axis=1)

    def abs_error(self, X, y):
        return np.sum(np.abs(self.predict(X) - y.T[0]))
    
    def mean_square_error(self, X, y):
        return np.sum((self.predict(X) - y.T[0])**2 / X.shape[0])
    def print_polynomial(self):
        word = ""
        arr_of_x = []
        for i in range(self.degree+1):
            mini_word = "x^" + str(i)
            arr_of_x += [mini_word]
        for i in range(self.degree + 1):
            if(self.coeffs[i] < 0):
                word += "(" + str(float(self.coeffs[i])) + ")"
            else:
                word += str(float(self.coeffs[i]))
            if i > 0:
                word += arr_of_x[i]
            if(self.degree > i):
                word += "+"
        print(word)
        return word
def plot(x, y, x_prediction, y_prediction):
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    ax.plot(x_prediction, y_prediction)

    plt.show()
pr = PolynomialRegression(degree=5)  
pr.fit(X_train, y_train)
pr.print_polynomial()
plot(X_test, y_test, X_test, pr.predict(X_test))
    #╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
