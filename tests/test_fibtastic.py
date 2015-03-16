# -*- coding:utf-8 -*-

from tests import BaseTestCase as TestCase
from fibtastic.models import Fib
from database import db


class FibTestCase(TestCase):

    def test_create_fib(self):
        fib = Fib([0, 1, 1, 2, 3])
        db.session.add(fib)
        db.session.commit()
        self.assertListEqual(fib.sequence, [0, 1, 1, 2, 3])

    def test_delete_fib(self):
        fib = Fib([0, 1, 1, 2, 3])
        db.session.add(fib)
        db.session.commit()
        db.session.delete(fib)
        db.session.commit()
        self.assertIsNone(Fib.query.get(fib.id))
