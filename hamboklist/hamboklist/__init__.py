# -*- coding: utf-8 -*-

from app import app
from database import db
from views.api import api

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://smarteen:mmentoring@localhost/hamboklist_xoul'
app.secret_key = 'This is fucking secret.'
app.debug = True

app.register_blueprint(api, url_prefix='/api')

db.init_app(app)
db.create_all(app=app)