import joblib
mind= joblib.load("SalaryPrediction.pkl")
exp=float(input("Enter years of experience:"))
result= mind.predict([[experience]])

print(result)
