from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/enviar_datos")
def test():
    name = "Nahuel"
    age = 22
    return render_template('datos.html', name=name, age=age)

@app.route("/character/<id>")
def character(id:str):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(url).json()
    nombre = response["name"]
    estado = response["status"]
    especie = response["species"]
    url_imagen = response["image"]
    next_id = int(id) + 1
    prev_id = int(id) - 1 if int(id) != 1 else None
    return render_template('characters.html', nombre=nombre, estado=estado, url_imagen=url_imagen, especie=especie, next_id=next_id, prev_id=prev_id)

@app.route("/characters/<page>")
def characters(page:str):
    url = f"https://rickandmortyapi.com/api/character/?page={page}"
    response = requests.get(url).json()
    characters = response["results"]
    # clear characters deleating the key "episodes"
    clean_characters = [{key: value for key, value in character.items() if key != "episode"} for character in characters]
    next_page = response["info"]["next"].split("=")[1]
    prev_page = response["info"]["prev"].split("=")[1] if response["info"]["prev"] else None
    # return {"characters": clean_characters, "next_page": next_page, "prev_page": prev_page}
    return render_template('list_of_characters.html', characters=clean_characters, next_page=next_page, prev_page=prev_page)


if __name__ == "__main__":
    app.run(debug=True)