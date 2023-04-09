from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='templates')

# Load the trained machine learning model
with open('regression.pkl', 'rb') as file:
    regression = pickle.load(file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')
# Define a route for the home page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = 0
    if request.method == 'POST':
        # Get the user's mood from the form
        mood = request.form['mood']
        try:
            # Convert the input to a numeric format
            mood = float(mood)
            # Use the machine learning model to make a prediction
            prediction = regression.predict([[mood]])
            # Display the prediction on the page
            return render_template('result.html', prediction=prediction)
        except ValueError:
            # Handle invalid input
            return "Invalid input: please enter a number."
    else:
        # Handle GET request by displaying the home page
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)