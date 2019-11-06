#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from . import views

accounts = Blueprint("accounts", __name__)

accounts.add_url_rule("/login", "login", views.login, methods=["POST", "GET"])
accounts.add_url_rule("/logout", "logout", views.logout)
accounts.add_url_rule("/register", "register", views.register)


