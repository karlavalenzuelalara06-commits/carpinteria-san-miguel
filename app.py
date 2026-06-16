from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Bienvenido a Carpintería San Miguel"

if _name_ == '_main_':
    app.run(debug=True)
