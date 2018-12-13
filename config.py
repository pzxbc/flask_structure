# -*- coding: utf-8 -*-


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""


class DevelopmentConfig(Config):
    DEBUG = True
