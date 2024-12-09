import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

print(x)

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1, 1)

print(x)

# Create the model
model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coeff = round(model.coef_[0], 2)
intercept = round(model.intercept_, 2)
rsquared = model.score(x, y)

# Print out the linear equation and r squared value
print(f"equation: y = {coeff}x + {intercept}")
print(f"r squared: {rsquared}")

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction
prediction = model.predict([[42]]) # we are predicted 43 year old with this 2d array that represents their age
print(prediction)

# Create the model in matplotlib and include the line of best fit
plt.figure(figsize=(6, 4))

plt.scatter(x, y)
plt.scatter([42], prediction, c="r") # here we add the point for the predicted blood pressure
plt.plot(x, coeff * x + intercept)

plt.xlabel("age")
plt.ylabel("blood pressure")
plt.title("age vs blood pressure")

plt.show()