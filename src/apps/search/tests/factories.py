# -*- coding: utf-8 -*-
"""
Este arquivo nao é de teste propriamente dito.
Ele é um helper para os meus testes.

Estou usando factory_boy para me ajudar a criar as dependecias para os tests.

As instancias criadas por factory_boy são persistidas
(a menos que voce impeça ele de fazer isso).

Como não estamos preocupados em mockar o DB (nao vale o esforço)
e o Django sobre um DB de testes na memoria RAM, isso normalmente está oK.

Confira mais sobre factory_boy em:
    http://readthedocs.org/docs/factoryboy/en/latest/
    http://readthedocs.org/docs/factoryboy/en/latest/subfactory.html

"""
import factory  # importa factory_boy para me ajudar
