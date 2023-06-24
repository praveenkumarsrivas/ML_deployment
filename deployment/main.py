from flask import Flask, render_template

# initialize an app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutus')
def aboutus():
    return render_template('about.html')


@app.route('/contact')
def contact():
   return render_template('contactus.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/images')
def images():
    return render_template('images.html')


# run
app.run()
