from sklearn import svm, tree
from sklearn.svm import LinearSVC, SVC
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, validation_curve, learning_curve
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelBinarizer, StandardScaler
import numpy as np
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
from get_data import getData

[X, y] = getData()

#
scaler = StandardScaler()

scaler.fit(X)
x_train_std = scaler.transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=True)

M1 = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
M2 = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
M3 = [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
M4 = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0]
M5 = [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]
Mystery = [M1, M2, M3, M4, M5]


ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)
ppn.fit(x_train_std, y)


# scaler.fit_transform(Mystery)
Mystery_std = scaler.transform(Mystery)

result = ppn.predict(Mystery_std)
print(result)

