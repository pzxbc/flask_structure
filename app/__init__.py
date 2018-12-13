# -*- coding: utf-8 -*-

from flask import Flask

# Todo:
# 1. 添加自动注册blueprint函数
from app import helloworld


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册模块
    app.register_blueprint(helloworld.bp, url_prefix='/helloworld')

    return app
