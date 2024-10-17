import pickle
from flask import Flask, render_template, request
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained machine learning model
with open('regr.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect form data from the dropdown inputs
        commodity = int(request.form['commodity'])
        state = int(request.form['state'])
        district = int(request.form['district'])
        market = int(request.form['market'])
        month_col = int(request.form['month'])
        season_names = int(request.form['season'])
        day = int(request.form['day'])

        # Prepare the input data for the model (reshape to 2D array)
        user_input = np.array([[commodity, state, district, market, month_col, season_names, day]])

        # Make the prediction using the model
        predicted_price = model.predict(user_input)

        # Display the result in result.html
        return render_template('result.html', prediction=predicted_price[0])

if __name__ == "__main__":
    app.run(debug=True)
