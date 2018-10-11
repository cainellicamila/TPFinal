import unittest

from app import ReusableForm

import urllib

from flask import Flask, render_template, flash, request

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import requests


class TestsApp(unittest.TestCase):


    def setUp(self):
        super(TestsApp, self).setUp()
        self.app = ReusableForm(request.form)

    def test_coordenadas (self):

        query = 'Zeballos 1301' + ', Rosario, Santa Fe, Argentina'
        query = query.encode('utf-8')
        a=self.app.get_coordinates(query)
        self.assertIsNotNone(a)

