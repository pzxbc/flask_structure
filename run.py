#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)
