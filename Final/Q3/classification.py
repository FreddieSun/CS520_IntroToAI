from sklearn import svm, tree
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelBinarizer

A1 = [255, 0, 0, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 0, 0, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255]
A2 = [0, 0, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0]
A3 = [255, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 255]
A4 = [0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0]
A5 = [0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255]


A11 = [255,255,0,0,255,0,0,255,255,255,0,0,255,255,255,255]

Train_A_data = [A1, A2, A3, A4, A5]

Train_A_tag = [0, 0, 0, 0, 0]

B1 = [255, 255, 0, 0, 255, 255, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 0, 0, 255, 255, 255, 0, 0, 255, 255]
B2 = [255, 0, 0, 255, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255, 255, 0, 0, 255, 0, 255, 255, 255, 255, 0]
B3 = [255, 0, 255, 0, 0, 255, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 255]
B4 = [255, 255, 255, 255, 0, 255, 0, 0, 255, 0, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 255, 255, 0]
B5 = [255, 0, 255, 255, 0, 0, 0, 0, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 255, 255, 0, 255, 0]

Train_B_data = [B1, B2, B3, B4, B5]
Train_B_tag = [1, 1, 1, 1, 1]

X = [B1, A2, B2, A3, B3, A4, B4, A5, B5, A1]
y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
y = LabelBinarizer().fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

M1 = [255, 0, 0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 255, 0, 255, 255, 0, 255, 0, 255]
M2 = [255, 255, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 255, 0, 0, 0, 255, 0, 255, 0, 255, 255, 255, 255]
M3 = [0, 0, 255, 255, 255, 255, 255, 255, 0, 255, 0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255]
M4 = [255, 0, 0, 0, 255, 255, 0, 0, 0, 255, 0, 0, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0]
M5 = [0, 255, 255, 255, 255, 0, 255, 0, 0, 255, 255, 255, 255, 255, 0, 255, 0, 0, 255, 0, 255, 255, 255, 255, 255]
Mystery = [M1, M2, M3, M4, M5]
'''
model = svm.SVC(C=0.1, cache_size=200, class_weight=None, coef0=0.0,
 decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
 max_iter=-1, probability=False, random_state=None, shrinking=True,
 tol=0.001, verbose=False)  # class
 '''
model = svm.LinearSVC(penalty='l2', loss='squared_hinge', dual=True,
                       tol=1e-4)
#model = tree.DecisionTreeClassifier()
#model = MLPClassifier()
#model = RandomForestClassifier()
model.fit(X, y)
result = model.predict(Mystery)
print(result)

