from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs
        input_data = {
            'CRIM': float(request.form['CRIM']),
            'ZN': float(request.form['ZN']),
            'INDUS': float(request.form['INDUS']),
            'CHAS': float(request.form['CHAS']),
            'NOX': float(request.form['NOX']),
            'RM': float(request.form['RM']),
            'AGE': float(request.form['AGE']),
            'DIS': float(request.form['DIS']),
            'RAD': float(request.form['RAD']),
            'TAX': float(request.form['TAX']),
            'PTRATIO': float(request.form['PTRATIO']),
            'B': float(request.form['B']),
            'LSTAT': float(request.form['LSTAT']),
        }

        df = pd.DataFrame([input_data])
        prediction = model.predict(df)[0]
        return render_template("result.html", price=round(prediction, 2))

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
