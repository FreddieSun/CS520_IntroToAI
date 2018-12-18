from sklearn import svm, tree
from sklearn.svm import LinearSVC,SVC
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split,validation_curve,learning_curve
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelBinarizer,StandardScaler
import numpy as np
import matplotlib.pyplot as plt

A1 = [255, 0, 0, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 0, 0, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255]
A6 = [255, 255, 0, 0, 255, 0, 0, 255, 255, 255, 0, 0, 255, 255, 255, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0]
A2 = [0, 0, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0]
A7 = [255, 255, 255, 0, 0, 255, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255]
A3 = [255, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 255]
A8 = [255, 0, 0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 0, 0, 0, 0]
A4 = [0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0]
A9 = [255, 255, 255, 0, 0, 0, 0, 0, 0, 255, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255]
A5 = [0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255]
A10 = [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 255, 255]

Train_A_data = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]

Train_A_tag = [0, 0, 0, 0, 0]

B1 = [255, 255, 0, 0, 255, 255, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 0, 0, 255, 255, 255, 0, 0, 255, 255]
B6 = [255, 0, 0, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 255, 0, 255, 255, 0, 0, 0, 255, 255, 0, 0, 255]
B2 = [255, 0, 0, 255, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255, 255, 0, 0, 255, 0, 255, 255, 255, 255, 0]
B7 = [255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0, 255, 255, 255, 255]
B3 = [255, 0, 255, 0, 0, 255, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 255]
B8 = [0, 0, 255, 0, 255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 255, 0, 255, 255, 255]
B4 = [255, 255, 255, 255, 0, 255, 0, 0, 255, 0, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 255, 255, 0]
B9 = [0, 255, 255, 255, 255, 0, 255, 0, 0, 255, 255, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 255, 255, 0, 0]
B5 = [255, 0, 255, 255, 0, 0, 0, 0, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 255, 255, 0, 255, 0]
B10 = [0, 255, 255, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 255, 0, 255, 255, 0, 255, 0, 255, 255]

Train_B_data = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10]
Train_B_tag = [1, 1, 1, 1, 1]

X = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

X = StandardScaler().fit_transform(X)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=True)

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
 tol=0.001, verbose=False)  # class[1,1,1,1,1]
'''

#model = svm.LinearSVC(penalty='l2', loss='squared_hinge', dual=True,tol=1e-4)#[0,0,0,0,1]
#model = tree.DecisionTreeClassifier()#[0,0,0,0,0]
#model = MLPClassifier()#[1 0 1 0 1]
model = svm.SVC(gamma=0.004)
#model = RandomForestClassifier(n_estimators=30)#[1,0,0,0,0]
model.fit(X,y)
result = model.predict(Mystery)
print(result)



#validation curve 参数不同的取值下模型的性能
'''
param_range = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
train_score, test_score = validation_curve(RandomForestClassifier(),
                                           X,y,
                                           param_name='n_estimators',
                                           param_range=param_range,
                                           cv=None,scoring='accuracy')
'''

param_range =[0.001*i for i in range(10)]
train_score, test_score= validation_curve(
    SVC(), X, y, param_name='gamma', param_range=param_range, cv=None, scoring='mean_squared_error')

train_score =  1-np.mean(train_score,axis=1)
test_score = 1-np.mean(test_score,axis=1)
plt.plot(param_range,train_score,'o-',color = 'r',label = 'training')
plt.plot(param_range,test_score,'o-',color = 'g',label = 'testing')
plt.legend(loc='best')
plt.xlabel('number of tree')
plt.ylabel('accuracy')
plt.show()


'''
#learning curve 检视过拟合
train_sizes,train_score,test_score = learning_curve(SVC(),X,y,train_sizes=[0.1,0.2,0.4,0.6,0.8,1],cv=10,scoring='accuracy')
train_error = 1- np.mean(train_score,axis=1)
test_error = 1- np.mean(test_score,axis=1)
plt.plot(train_sizes,train_error,'o-',color = 'r',label = 'training')
plt.plot(train_sizes,test_error,'o-',color = 'g',label = 'testing')
plt.legend(loc='best')
plt.xlabel('traing examples')
plt.ylabel('error')
plt.show()
'''
'''
param_range =[0.001,0.002,0.003,0.004,0.005,0.006]
train_loss, test_loss = validation_curve(
SVC(), X, y, param_name='gamma', param_range=param_range, cv=10, scoring='mean_squared_error')

train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

#可视化图形
plt.plot(param_range, train_loss_mean, 'o-', color="r",
         label="Training")
plt.plot(param_range, test_loss_mean, 'o-', color="g",
        label="Cross-validation")

plt.xlabel("gamma")
plt.ylabel("Loss")
plt.legend(loc="best")
'''