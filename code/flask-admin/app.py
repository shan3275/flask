#!/usr/bin/python
#-*- coding: UTF-8 -*-
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))

app.run()
