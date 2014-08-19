import os
import requests
import bottle.ext.memcache
from bottle import Bottle, response
from app.scrapper import Scrapper


app = Bottle()
plugin = bottle.ext.memcache.MemcachePlugin(
    servers=[os.environ.get('MEMCACHEDCLOUD_SERVERS', 'localhost:11211')])
app.install(plugin)


@app.route('/')
def home(mc):
    response.content_type = 'application/json'
    response.charset = 'UTF-8'

    banks_cache = mc.get('banks_cache')

    if banks_cache is not None:
        print('cached')
        return banks_cache
    else:
        print('not cached')
        url = 'http://www.buscabanco.org.br/AgenciasBancos.asp'
        request = requests.post(url, {'Buscar': 'S'})
        scrap = Scrapper(request.text)

        json = scrap.as_json()
        mc.set('banks_cache', json)

        return json
