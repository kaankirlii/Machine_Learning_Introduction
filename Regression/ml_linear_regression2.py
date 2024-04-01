# -*- coding: utf-8 -*-
"""ml_linear_regression2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RC_PMwHQViHm1cikZIn1D6i15ufxdxvG
"""

# Example: Price predictor, given Pizza Diameter.
# A Regression Algorithm predicts _continous values_ (like price)
#
#------------------------------------------------------------
# In "ML-regression1.py" you can see there's a correlation
# between X and Y.
#------------------------------------------------------------
#
# Steps:
# 1. Algorithm is trained on data.
# 2. Algorithm predicts price, given a new diameter

# Load LinearRegression algorithm
from sklearn.linear_model import LinearRegression

# Training Data: diameter
X = [[4], [8], [12], [16], [18]]
# Training Data: price
y = [[4], [8], [10], [12], [15]]

# 1. Algorithm is trained on data (X,y).
#y=aX+b
model = LinearRegression()
model.fit(X,y)

# 2. Algorithm predicts price, given a new diameter
diameter = 13
prediction = model.predict([[diameter]])
print('Price prediction: $%.2f' % prediction)

"""**Key facts**

*  Regression to predict continuous values, like price or temperature

*  Classification to predict discrete values, from a set of options like [0,1,2]

*  A regression algorithm uses the same steps as other supervised learning algorithms

1.   Collect training data
2.   Train algorithm
3.   Predict new value
"""