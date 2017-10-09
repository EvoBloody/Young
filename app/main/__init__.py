#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by evo on 10/9/17
from flask import Blueprint

main = Blueprint(__name__)

from . import views, errors
