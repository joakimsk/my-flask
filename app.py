#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# my-flask
# description : test of flask
# created by : Joakim Skjefstad
# =============================================================================

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')