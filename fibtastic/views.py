# -*- coding:utf-8 -*-
"""
Author: Rick James
Date: 3-16-2015
Purpose: Rubicon ISE Interview

Todo:
    - Create uniform serializer methods
"""
from flask import Blueprint, current_app
from flask import  url_for, request, jsonify
from .helpers import gen_fib
from .exceptions import APIException

from database import db

from .models import Fib

app = Blueprint('blog', __name__, template_folder='templates')

@app.errorhandler(APIException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    current_app.elog(error.request.remote_addr,
        error.message, error.status_code)
    return response

@app.route("/fibtastic", methods=['GET'])
def get_fibs():
    """
    Returns all fibonacci sequences generated
    """
    fibs = Fib.query.all()
    response = []
    for fib in fibs:
        response.append({
            'id': fib.id,
            'sequence': fib.sequence,
            'url': url_for('.get_fib', fib_id=fib.id, _external=True)
            })
    return jsonify(fibs=response)

@app.route("/fibtastic/<int:fib_id>", methods=['GET'])
def get_fib(fib_id):
    """
    Returns a specific fibbonacci sequence
    """
    fib = Fib.query.get(fib_id)
    if not fib:
        raise APIException('Requested fib not found',
            request=request, status_code=404)
    return jsonify(id=fib.id, sequence=fib.sequence)

@app.route("/fibtastic", methods=['POST'])
def create_fib():
    """
    Creates a fibonacci sequence up to given parameter
    example json payload:
    {
        'n': 5
    }
    """
    if not request.json:
        raise APIException('Payload must be in JSON format',
            request=request, status_code=400)
    elif 'n' not in request.json:
        raise APIException('Parameter n must be passed',
        request=request, status_code=400)
    elif request.json['n'] < 0:
        raise APIException('parameter n must be a non-negative integer',
            request=request, status_code=400)

    obj = Fib(gen_fib(request.json['n']))
    db.session.add(obj)
    db.session.commit()
    current_app.ilog(request.remote_addr,
        'Created fib id:{}'.format(obj.id), 204)
    return jsonify({
        'id': obj.id,
        'sequence': obj.sequence,
        'url': url_for('.get_fib', fib_id=obj.id, _external=True)
        }), 201

@app.route("/fibtastic/<int:fib_id>", methods=['DELETE'])
def delete_fib(fib_id):
    fib = Fib.query.get(fib_id)
    if not fib:
        raise APIException('Requested fib not found',
            request=request, status_code=404)
    db.session.delete(fib)
    db.session.commit()
    current_app.ilog(request.remote_addr,
        'Deleted fib id:{}'.format(fib.id), 200)
    return jsonify(response="Fib {} successfully deleted.".format(fib.id))









