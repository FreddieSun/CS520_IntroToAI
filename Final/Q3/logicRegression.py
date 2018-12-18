from sklearn import svm, tree
from sklearn.linear_model import Perceptron
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
from sklearn.svm import SVR
from sklearn.linear_model import LogisticRegression
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

clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X, y)

result = clf.predict(Mystery)
print(result)