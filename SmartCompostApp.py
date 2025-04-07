from flask import Flask, request, render_template
import pickle

# Load the trained pipeline model (includes TfidfVectorizer + classifier)
model = pickle.load(open("smartcompostmodel.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    description = request.form['description']
    prediction = model.predict([description])[0]
    return render_template('index.html', prediction=f"<strong>{prediction}</strong><br><br>{description}", request=request)

if __name__ == "__main__":
    app.run(debug=True)
