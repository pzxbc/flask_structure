# -*- coding: utf-8 -*-

from app.helloworld import bp


@bp.route('/', methods=['GET'])
def hello_world():
    return "Hello World"
