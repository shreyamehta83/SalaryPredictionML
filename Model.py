import pandas
db = pandas.read_csv("SalaryData.csv")

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X = db["YearsExperience"].values.reshape(30,1)
y= db["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state= 42)

mind = LinearRegression()
mind.fit(X_train, y_train)

import joblib
joblib.dump(mind, "SalaryPrediction.pkl")
