from flask import Flask, render_template, request
import joblib

# initialize an app
app = Flask(__name__)
model = joblib.load("joblib_model.pkl")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    columns = [float(x) for x in [preg, plas, pres, skin, test, mass, pedi, age]]
    result = model.predict([columns])
    if result[0] ==0:
        return "You are safe!!"
    return "OOps!! you are Diabetic!"

# run
app.run(port=9090, host='0.0.0.0')
