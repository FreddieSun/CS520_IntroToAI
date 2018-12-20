from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler

from get_data import getData
from get_mystery import get_mystery

[X, y] = getData()

scaler = StandardScaler()

scaler.fit(X)
x_train_std = scaler.transform(X)

Mystery = get_mystery()


ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)
ppn.fit(x_train_std, y)


scaler.transform(Mystery)
Mystery_std = scaler.transform(Mystery)

result = ppn.predict(Mystery_std)
print(result)

