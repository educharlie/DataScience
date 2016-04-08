#get your data
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

gen = np.random.RandomState(42)
num_samples = 40

x = 10 * gen.rand(num_samples)
y = 3 * x + 7+ gen.randn(num_samples)
X = pd.DataFrame(x)

#fit model to data

model = LinearRegression(fit_intercept=True)
model.fit(X, y)

print('Slope: {}, Intercept: {}'.format(model.coef_, model.intercept_))

#check your model

Xtest = pd.DataFrame(np.linspace(-1, 11))
predicted = model.predict(Xtest)

plt.scatter(x, y)
plt.plot(Xtest, predicted)
