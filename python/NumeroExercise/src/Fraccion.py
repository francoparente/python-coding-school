#
# Developed by 10Pines SRL
# License:
# This work is licensed under the
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
# or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.
#

from src.Numero import Numero


class Fraccion(Numero):
    def __new__(cls, numerador, denominador):
        if denominador.es_cero():
            raise Exception(Numero.ERROR_DE_DIVISION_POR_CERO)
        if denominador.es_uno():
            return numerador

        maximoComunDivisor = denominador.maximo_comun_divisor_con(numerador)
        # No puedo usar / porque puedo caer en una recursion, por eso divido directamente
        # los valores porque se que son enteros
        numerador_reducido = numerador.division_entera(maximoComunDivisor)
        denominador_reducido = denominador.division_entera(maximoComunDivisor)

        if denominador_reducido.es_uno():
            return numerador_reducido

        return object.__new__(cls)

    def __init__(self, numerador, denominador):
        self._numerador = numerador
        self._denominador = denominador

    def numerador(self):
        return self._numerador

    def denominador(self):
        return self._denominador

    def es_cero(self):
        return False

    def es_uno(self):
        return False

    def __eq__(self, an_object):
        if isinstance(an_object, self.__class__):
            return self._numerador * an_object.denominador() == self._denominador * an_object.numerador()
        else:
            return False

    def __add__(self, sumando):
        if not isinstance(sumando, self.__class__):
            return sumando + self
        nuevo_denominador = self._denominador * sumando.denominador()
        primer_sumando = self._numerador * sumando.denominador()
        segundo_sumando = self._denominador * sumando.numerador()
        nuevo_numerador = primer_sumando + segundo_sumando
        return nuevo_numerador / nuevo_denominador

    def __mul__(self, factor):
        if not isinstance(factor, self.__class__):
            return factor * self._numerador / self._denominador
        return (self._numerador * factor.numerador()) / (self._denominador * factor.denominador())

    def __truediv__(self, divisor):
        if not isinstance(divisor, self.__class__):
            return Fraccion(self._numerador, self._denominador * divisor)
        return (divisor.denominador() * self._numerador) / (divisor.numerador() * self._denominador)
