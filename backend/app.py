from flask import Flask, render_template
import os

# Tell Flask where to find templates
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
