from google.colab import drive
drive.mount('/content/drive')

cd '/content/drive/MyDrive/test script/pythondatabase'

import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

folders=['pointage_Linear_Regression.xlsx']
folder_combine=pd.DataFrame()
for folder in folders:
  df=pd.read_excel(folder)
  print(df)

plt.scatter(df['JP'], df['JA'], color='red')
plt.title('JP Vs JA', fontsize=14)
plt.xlabel('JP', fontsize=14)
plt.ylabel('JA', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['JP'], df['JC'], color='green')
plt.title('JP Vs JC', fontsize=14)
plt.xlabel('JP', fontsize=14)
plt.ylabel('JC', fontsize=14)
plt.grid(True)
plt.show()

x = df[['JC','JA']]
y = df['JP']

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(x, y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# with statsmodels
x = sm.add_constant(x) # adding a constant

model = sm.OLS(y, x).fit()
predictions = model.predict(x)

print_model = model.summary()
print(print_model)
