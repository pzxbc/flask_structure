# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('hellworld', __name__)

from app.helloworld import routes
