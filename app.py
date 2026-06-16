from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Carpintería San Miguel"

if _name_ == '__main__':
    app.run(debug=True)
