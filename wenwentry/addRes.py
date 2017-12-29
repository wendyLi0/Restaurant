#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from flask import Flask, url_for, render_template, jsonify
from flask import make_response, abort, request
import DB_Operation
from Log import SimpleLog

app = Flask(__name__)
log = SimpleLog()


@app.route('/hello')
def hello():
    return 'hello world'


@app.route('/index')
def index():
    return render_template('lunch.html')


@app.route('/canting/add', methods=['POST'])
def create_restaurant():
    if not request.form:
        log.info('添加餐厅请求参数为空')
        abort(400)
    if (request.form['cantingName'] != "" and request.form['cantingAddress'] != ""):
        DB_Operation.add_restaurant(request.form)
        return jsonify(request.form), 200
    else:
        return jsonify(request.form), 200


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/canting/getlist', )
def get_restaurant():
    data_json = DB_Operation.get_restaurant("true")
    restaurants = jsonify({'restaurant': data_json})
    return restaurants


@app.route('/canting/ramdon')
def get_ramdon_restaurant():
    data_json = DB_Operation.get_restaurant('false')
    return jsonify({'restaurant': data_json})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
