#
# Developed by 10Pines SRL
# License: 
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. 
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ 
# or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, 
# California, 94041, USA.
#  

import unittest

from src.Entero import Entero
from src.Fraccion import Fraccion
from src.Numero import Numero


class NumeroTest(unittest.TestCase):

    def create_cero(self):
        return Entero(0)

    def create_uno(self):
        return Entero(1)

    def create_dos(self):
        return Entero(2)

    def create_tres(self):
        return Entero(3)

    def create_cuatro(self):
        return Entero(4)

    def create_cinco(self):
        return Entero(5)

    def create_un_quinto(self):
        return self.uno / self.cinco

    def create_dos_quintos(self):
        return self.dos / self.cinco

    def create_tres_quintos(self):
        return self.tres / self.cinco

    def create_dos_veinticincoavos(self):
        return self.dos / Entero(25)

    def create_un_medio(self):
        return self.uno / self.dos

    def create_cinco_medios(self):
        return self.cinco / self.dos

    def create_seis_quintos(self):
        return Entero(6) / self.cinco

    def create_cuatro_medios(self):
        return self.cuatro / self.dos

    def create_dos_cuartos(self):
        return self.dos / self.cuatro

    def setUp(self):
        self.cero = self.create_cero()
        self.uno = self.create_uno()
        self.dos = self.create_dos()
        self.tres = self.create_tres()
        self.cuatro = self.create_cuatro()
        self.cinco = self.create_cinco()
        self.un_quinto = self.create_un_quinto()
        self.dos_quintos = self.create_dos_quintos()
        self.tresQuintos = self.create_tres_quintos()
        self.dos_veinticincoavos = self.create_dos_veinticincoavos()
        self.un_medio = self.create_un_medio()
        self.cinco_medios = self.create_cinco_medios()
        self.seis_quintos = self.create_seis_quintos()
        self.cuatroMedios = self.create_cuatro_medios()
        self.dos_cuartos = self.create_dos_cuartos()

    def test01_es_cero_devuelve_true_solo_para_el_cero(self):
        self.assertTrue(self.cero.es_cero())
        self.assertFalse(self.uno.es_cero())

    def test02_es_uno_devuelve_true_solo_para_el_uno(self):
        self.assertTrue(self.uno.es_uno())
        self.assertFalse(self.cero.es_uno())

    def test03_suma_de_enteros(self):
        self.assertEqual(self.dos, self.uno + self.uno)

    def test04_multiplicacion_de_enteros(self):
        self.assertEqual(self.cuatro, self.dos * self.dos)

    def test05_division_de_enteros(self):
        self.assertEqual(self.uno, self.dos / self.dos)

    def test06_suma_de_fracciones(self):
        siete_decimos = Entero(7) / Entero(10)  # <- REEMPLAZAR POR LO QUE CORRESPONDA; Fraccion(7,10)
        self.assertEqual(siete_decimos, self.un_quinto + self.un_medio)
        # 
        # La suma de fracciones es:
        # 
        # a/b + c/d = (a.d + c.b) / (b.d)
        # 
        # SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
        # NO SE ESTA TESTEANDO ESE CASO
        #

    def test07_multiplicacion_de_fracciones(self):
        self.assertEqual(self.dos_veinticincoavos, self.un_quinto * self.dos_quintos)
        # 
        # La multiplicacion de fracciones es:
        # 
        # (a/b) * (c/d) = (a.c) / (b.d)
        # 
        # SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
        # TODAVIA NO SE ESTA TESTEANDO ESE CASO
        #

    def test08_division_de_fracciones(self):
        self.assertEqual(self.cinco_medios, self.un_medio / self.un_quinto)
        # 
        # La division de fracciones es:
        # 
        # (a/b) / (c/d) = (a.d) / (b.c)
        # 
        # SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
        # TODAVIA NO SE ESTA TESTEANDO ESE CASO
        #

    # 
    # Ahora empieza lo lindo! - Primero hacemos que se puedan sumar enteros con fracciones
    # y fracciones con enteros 
    #
    def test09_suma_de_entero_y_fraccion(self):
        self.assertEqual(self.seis_quintos, self.uno + self.un_quinto)

    def test10_suma_de_fraccion_y_entero(self):
        self.assertEqual(self.seis_quintos, self.un_quinto + self.uno)

    # 
    # Hacemos lo mismo para la multiplicacion
    #
    def test11_multiplicacion_de_entero_por_fraccion(self):
        self.assertEqual(self.dos_quintos, self.dos * self.un_quinto)

    def test12_multiplicacion_de_fraccion_por_entero(self):
        self.assertEqual(self.dos_quintos, self.un_quinto * self.dos)

    # 
    # Hacemos lo mismo para la division
    #
    def test13_division_de_entero_por_fraccion(self):
        self.assertEqual(self.cinco_medios, self.uno / self.dos_quintos)

    def test14_division_de_fraccion_por_entero(self):
        self.assertEqual(self.dos_veinticincoavos, self.dos_quintos / self.cinco)

    # 
    # Ahora si empezamos con problemas de reduccion de fracciones
    #
    def test15_una_fraccion_puede_ser_igual_a_un_entero(self):
        self.assertEquals(self.dos, self.cuatroMedios)

    def test16_las_fracciones_aparentes_son_iguales(self):
        self.assertEquals(self.un_medio, self.dos_cuartos)
        #
        # Las fracciones se reducen utilizando el maximo comun divisor (mcd)
        # Por lo tanto, para a/b, sea c = mcd (a,b) => a/b reducida es:
        # (a/c) / (b/c).
        # 
        # Por ejemplo: a/b = 2/4 entonces c = 2. Por lo tanto 2/4 reducida es:
        # (2/2) / (4/2) = 1/2
        # 
        # Para obtener el mcd pueden usar el algoritmo de Euclides que es:
        # 
        # mcd (a,b) = 
        #         si b = 0 --> a
        #         si b != 0 -->mcd(b, restoDeDividir(a,b))
        #     
        # Ejemplo:
        # mcd(2,4) ->
        # mcd(4,restoDeDividir(2,4)) ->
        # mcd(4,2) ->
        # mcd(2,restoDeDividir(4,2)) ->
        # mcd(2,0) ->
        # 2
        #

    def test17_la_suma_de_fracciones_puede_dar_entero(self):
        self.assertEquals(self.uno, self.un_medio + self.un_medio)

    def test18_la_multiplicacion_de_fracciones_puede_dar_entero(self):
        self.assertEquals(self.dos, self.cuatro * self.un_medio)

    def test19_la_division_de_enteros_puede_dar_fraccion(self):
        self.assertEquals(self.un_medio, self.dos / self.cuatro)

    def test20_la_division_de_fracciones_puede_dar_entero(self):
        self.assertEquals(self.uno, self.un_medio / self.un_medio)

    def test21_no_se_puede_dividir_entero_por_cero(self):
        self.assertRaisesWithDescription(lambda: self.uno / self.cero,
                                         Exception,
                                         Numero.ERROR_DE_DIVISION_POR_CERO)

    def test22_no_se_puede_dividir_fraccion_por_cero(self):
        self.assertRaisesWithDescription(lambda: self.un_quinto / self.cero,
                                         Exception,
                                         Numero.ERROR_DE_DIVISION_POR_CERO)

    def test23_no_se_puede_crear_fraccion_con_denominador_cero(self):
        self.assertRaisesWithDescription(lambda: Fraccion(self.uno, self.cero),
                                         Exception,
                                         Numero.ERROR_DE_DIVISION_POR_CERO)

    def assertRaisesWithDescription(self, a_block_to_try, exception_class, error_description):
        try:
            a_block_to_try()
            self.fail()
        except exception_class as error:
            self.assertEquals(error_description, error.args[0])


if __name__ == "__main__":
    unittest.main()
