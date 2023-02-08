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
from src.Fraccion import Fraccion


class Entero(Numero):

    def __init__(self, numero):
        self._valor = numero

    def valor(self):
        return self._valor

    def es_cero(self):
        return self._valor == 0

    def es_uno(self):
        return self._valor == 1

    def __eq__(self, an_object):
        if not isinstance(an_object, self.__class__):
            return False
        return self._valor == an_object._valor

    def __add__(self, sumando):
        if isinstance(sumando, Fraccion):
            # return Fraccion(self._valor * sumando.denominador() + sumando.numerador(), sumando.denominador())  ESTO NO SIRVE ACÁ PORQUE LOS TESTS ESPERAN UN ENTERO
            return (self * sumando.denominador() + sumando.numerador()) / sumando.denominador()
        return Entero(self._valor + sumando.valor())

    def __mul__(self, factor):
        if not isinstance(factor, self.__class__):
            return self * factor.numerador() / factor.denominador()
        return Entero(self._valor * factor.valor())

    def __truediv__(self, divisor):
        if not isinstance(divisor, self.__class__):
            return Fraccion(self * divisor.denominador(), divisor.numerador())
        return Fraccion(self, divisor)

    def division_entera(self, divisor_entero):
        return Entero(self._valor / divisor_entero.valor())

    def maximo_comun_divisor_con(self, otro_entero):
        if otro_entero.es_cero():
            return self
        else:
            return otro_entero.maximo_comun_divisor_con(self.resto_con(otro_entero))

    def resto_con(self, divisor):
        return Entero(self._valor % divisor.valor())
