# -*- coding: utf-8 -*-
from django import forms
from haystack.forms import SearchForm as HaystackSearchForm


class SearchForm(HaystackSearchForm):
    """
    Nosso form de busca.

    No futuro ele será customizado.
    """
    pass
