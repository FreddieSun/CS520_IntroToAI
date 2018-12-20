import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.model_selection import validation_curve
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from get_data import getData
from get_mystery import get_mystery

[X, y] = getData()

scaler = StandardScaler()

scaler.fit(X)
x_train_std = scaler.transform(X)


model = svm.SVC(gamma=0.004)

model.fit(x_train_std, y)

Mystery = get_mystery()

# scaler.fit_transform(Mystery)
Mystery_std = scaler.transform(Mystery)

result = model.predict(Mystery_std)
print(result)

# validation curve using the validation curve to modify the model
'''
param_range = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
train_score, test_score = validation_curve(RandomForestClassifier(),
                                           X,y,
                                           param_name='n_estimators',
                                           param_range=param_range,
                                           cv=None,scoring='accuracy')
'''

param_range = [0.001 * i for i in range(10)]
train_score, test_score = validation_curve(
    SVC(), X, y, param_name='gamma', param_range=param_range, cv=None, scoring='mean_squared_error')

train_score = 1 - np.mean(train_score, axis=1)
test_score = 1 - np.mean(test_score, axis=1)
plt.plot(param_range, train_score, 'o-', color='r', label='training')
plt.plot(param_range, test_score, 'o-', color='g', label='testing')
plt.legend(loc='best')
plt.xlabel('gamma')
plt.ylabel('accuracy')
plt.show()
