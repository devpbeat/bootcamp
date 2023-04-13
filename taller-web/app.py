from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/enviar_datos")
def test():
    name = "Nahuel"
    age = 22
    return render_template('datos.html', name=name, age=age)

@app.route("/nice_weather")
def nice_weather():
    return "<p>nice weather bro</p>"


if __name__ == "__main__":
    app.run(debug=True)

