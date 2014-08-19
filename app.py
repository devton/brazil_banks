from bottle import run
from app.views import app

run(app, host="0.0.0.0", port=8080, debug=True)
