from flask import Flask, render_template, request
import pickle


app = Flask(__name__, template_folder='templates')


# Load the trained machine learning model
with open('multi_regression.pkl', 'rb') as file:
    multi_regression = pickle.load(file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')
# Define a route for the home page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
	# Get input data from request
    prediction = 0
    if request.method == 'POST':
        # Get the user's mood from the form
        input_data = request.form.get("input_data")
        mood = request.form['mood']
        sleep = request.form['sleep']
        try:
            # Convert the input to a numeric format
            mood = float(mood)
            sleep = float(sleep)
            # Use the machine learning model to make a prediction
            prediction = multi_regression.predict([[mood, sleep]])

            #prediction = multi_regression.predict(input_data)
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