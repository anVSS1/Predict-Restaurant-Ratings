from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = joblib.load('restaurant_rating_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    data = request.form.to_dict()
    df = pd.DataFrame([data])

    # Convert necessary columns to numeric (such as cost, votes, price range)
    df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'])
    df['Price range'] = pd.to_numeric(df['Price range'])
    df['Votes'] = pd.to_numeric(df['Votes'])

    # Make the prediction
    prediction = model.predict(df)

    # Render result template
    return render_template('result.html', predicted_rating=round(prediction[0], 2))

if __name__ == '__main__':
    app.run(debug=True)
