# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import RequestFactory
from contrib.tests import assert_post, assert_get, assert_equals


class SearchSpec(TestCase):
    """
    Search specification

    """
    def deve_saber_apresentar_a_pagina_principal(self):
        url = '/search/'
        response = self.client.get(url)
        assert_get(response, 'search/search.html')
