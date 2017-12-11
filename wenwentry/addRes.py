#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,url_for,render_template,jsonify
from flask import make_response,abort,request
import addToDB

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/canting/add', methods=['POST'])
def create_restaurant():
    if not request.json:
        abort(400)
    addToDB.Add_restaurant().add_restaurant(request.json)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

