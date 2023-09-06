from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/press-view')
def press_view():
    return render_template('press.html')

@app.route('/image-evidence')
def image():
    return render_template('image.html')

@app.route('/process-photo')
def photo():
    return render_template('photo.html')

@app.route('/earrings')
def images():
    return render_template('earrings.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/tut-declaration')
def declaration():
    return render_template('declaration.html')
    

if __name__ == "__main__":
    app.run(debug=True)