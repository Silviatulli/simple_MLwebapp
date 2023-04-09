import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Split the data into input (X) and output (y) variables
X = data[['mood']]
y = data['work_hours']

# Train a linear regression model on the data
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
print(y_pred)
# Save the trained model to a file using pickle
with open('regression.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as regression.pkl")