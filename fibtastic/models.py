"""
Author: Rick James
Date: 3-16-2015
Purpose: Rubicon ISE Interview
"""

from database import db
from datetime import datetime
from flask import url_for

class Fib(db.Model):
    """
    DB Model class with 3 fields:
        id: primary key, sequential
        invoke_date: The date the request was made
        sequence: The fibonacci sequence generated
    """
    id = db.Column(db.Integer, primary_key=True)
    invoke_date = db.Column(db.DateTime)
    sequence = db.Column(db.PickleType)

    def __init__(self, sequence, invoke_date=None):
        self.sequence = sequence
        self.invoke_date = ( invoke_date or datetime.utcnow() )

