import requests
from bottle import Bottle, response
from app.scrapper import Scrapper


app = Bottle()


@app.route('/')
def home():
    response.content_type = 'application/json'

    url = 'http://www.buscabanco.org.br/AgenciasBancos.asp'
    request = requests.post(url, {'Buscar': 'S'})
    scrap = Scrapper(request.text)

    return scrap.as_json()
