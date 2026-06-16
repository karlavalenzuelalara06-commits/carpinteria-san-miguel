from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Carpintería San Miguel"

if __name__ == '__main__':
    app.run(debug=True)
