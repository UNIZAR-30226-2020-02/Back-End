from django.test import TestCase
from rest_framework.test import APIRequestFactory
import os
import sys
from playstackDjango import *
from django.test import RequestFactory, TestCase

class MyTests(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

    def test1(self):
        print('ejecuto')
        request = self.factory.post('/user/login/', {'NombreUsuario': 'Amador', 'Contrasenya':  'Password'})

    def test2(self):
        print('ejecuto')
        request = self.factory.post('/user/login/', {'NombreUsuario': 'Amador', 'Contrasenya':  'Password'})