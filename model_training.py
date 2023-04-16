import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from pymongo import MongoClient

# Initialize MongoDB
client = MongoClient('mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority')
db = client['data']
collection = db['test.users']


data = collection.find({})
# Insert data
# data = {'mood': [0,1,2,3,4,5,0,1,2,3,4,5], 'sleep': [7,9,10,6,10,8,7,9,10,6,5,8], 'work_hours': [3,4,10,6,7,8,3,4,5,8,10,8]}
# db.users.insert_one(data)



# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Split the data into input (X) and output (y) variables
X = data[['mood', 'sleep']]
y = data['work_hours']

# Train a linear regression model on the data
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
print(y_pred)
# Save the trained model to a file using pickle
with open('multi_regression.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as multi_regression.pkl")
