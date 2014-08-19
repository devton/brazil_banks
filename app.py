import os
from bottle import run
from app.views import app


run(app, host="0.0.0.0", 
    port=os.environ.get('PORT', 5000), 
    debug=os.environ.get('DEBUG_MODE', False))
