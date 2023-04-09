# Simple ML Webapp with Flask
introductory tutorial to build a flask web app that integrates a ML model

# Requirements
`pip install flask scikit-learn pandas`

# Steps
## Flask app
* Create a new file called app.py
* Import the Flask and pickle
* Create a new Flask application instance and store it in the app variable
* - The root route ('/') returns the page in which the user send its information about the mood.
* - The ('/predict') route is where we'll handle prediction requests. It expects a POST request with JSON data containing the mood of the user.
* When a request is made to the /predict route, the predict function is called. First, we load the machine learning model that we'll be using to make predictions. We then get the request data from the JSON payload, extract the user's mood, and use the model to make a prediction based on the user's mood. Finally, we return the prediction as a JSON object.
* In the if __name__ == '__main__' block, we start the Flask application in debug mode.
## ML model
* Create a new file called model_training.py
* This creates a simple linear regression model that predicts the number of hours you will work based on your mood. We train the model using a small dataset of ten examples, where the mood is the input and the number of hours worked is the output. We then save the trained model using pickle
* To train the model, simply run the model_training.py file: `python3 model_training.py`
* This will save the trained model to a file called regression.pkl.
## Run the application
Now, start the Flask application by running the app.py file: `python3 app.py`
