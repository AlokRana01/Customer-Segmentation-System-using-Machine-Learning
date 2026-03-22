from flask import Flask, render_template, request
import pickle
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # User enters ₹ → convert to k$
    income_rupees = float(request.form['income'])
    income = income_rupees / 83000

    score = float(request.form['score'])

    cluster = model.predict([[income, score]])[0]

    # Smart labels
    if cluster == 0:
        result = "💸 Low Income - Low Spending (Budget Customer)"
    elif cluster == 1:
        result = "💎 High Income - High Spending (Premium Customer)"
    elif cluster == 2:
        result = "🛍 High Spending - Low Income"
    elif cluster == 3:
        result = "🧠 Careful Customer"
    else:
        result = "📊 Average Customer"

    # -------------------------------
    # UPDATED GRAPH (IMPORTANT FIX)
    # -------------------------------
    data = pd.read_csv('Mall_Customers.csv')
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

    # Predict clusters for dataset
    labels = model.predict(X)

    plt.figure()

    # Plot all customers (clusters)
    plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=labels)

    # Highlight user input
    plt.scatter(income, score, color='red', s=120)

    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score')
    plt.title('Customer Segmentation')

    # Save graph
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    plt.close()  # Prevent memory issues

    return render_template('index.html',
                           prediction_text=result,
                           plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)