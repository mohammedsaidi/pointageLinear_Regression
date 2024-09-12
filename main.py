import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('pointage_Linear_Regression.xlsx')
print(df)

# Descriptive scatter plots
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['Industrial_Products'], df['Agricultural_Products'], color='red')
plt.title('Industrial vs Agricultural Products', fontsize=14)
plt.xlabel('Industrial Products', fontsize=14)
plt.ylabel('Agricultural Products', fontsize=14)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(df['Industrial_Products'], df['Construction_Products'], color='green')
plt.title('Industrial vs Construction Products', fontsize=14)
plt.xlabel('Industrial Products', fontsize=14)
plt.ylabel('Construction Products', fontsize=14)
plt.grid(True)

plt.tight_layout()
plt.show()

# Prepare data for regression
X = df[['Construction_Products','Agricultural_Products']]
y = df['Industrial_Products']

# Linear Regression with scikit-learn
sklearn_model = LinearRegression()
sklearn_model.fit(X, y)

print('sklearn Model:")
print('Intercept: \n', sklearn_model.intercept_)
print('Coefficients: \n', sklearn_model.coef_)

# Linear Regression with statsmodels
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print("\nstatsmodels Model Summary:")
print(model.summary())
