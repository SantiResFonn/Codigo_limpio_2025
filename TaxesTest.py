import unittest
import BuyLogic

class ImpuestosComprasTest(unittest.TestCase):


    def testImpuesto1(self):
        valor_compra=65000
        valor_iva=19
        valor_ic=0
        impuesto_licor=0
        impuesto_bolsa="si"

        experado = 77420

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto2(self):
        valor_compra=150000
        valor_iva=5
        valor_ic=0
        impuesto_licor=5
        impuesto_bolsa="si"

        experado = 165070

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto3(self):
        valor_compra=230000
        valor_iva=19
        valor_ic=8
        impuesto_licor=5
        impuesto_bolsa="no"

        experado = 303600

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto4(self):
        valor_compra=315000
        valor_iva=19
        valor_ic=0
        impuesto_licor=0
        impuesto_bolsa="si"

        experado = 374920

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto5(self):
        valor_compra=410000
        valor_iva=19
        valor_ic=16
        impuesto_licor=0
        impuesto_bolsa="si"

        experado = 553570

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto6(self):
        valor_compra=52500
        valor_iva=5
        valor_ic=4
        impuesto_licor=5
        impuesto_bolsa="no"

        experado = 59850

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto7(self):
        valor_compra=600000
        valor_iva=19
        valor_ic=4
        impuesto_licor=0
        impuesto_bolsa="si"

        experado = 738070

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto8(self):
        valor_compra=7200
        valor_iva=5
        valor_ic=0
        impuesto_licor=0
        impuesto_bolsa="no"

        experado = 7560

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto9(self):
        valor_compra=850000
        valor_iva=19
        valor_ic=16
        impuesto_licor=0
        impuesto_bolsa="si"

        experado = 1147570

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def testImpuesto10(self):
        valor_compra=93000
        valor_iva=19
        valor_ic=8
        impuesto_licor=5
        impuesto_bolsa="no"

        experado = 122760

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)

    def test_cero_iva(self):
        valor_compra=35000
        valor_iva=0
        valor_ic=0
        impuesto_licor=0
        impuesto_bolsa="no"

        experado = 35000

        resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        self.assertEqual(experado,resultado,2)
    
    def test_valor_compra_cero(self):
        valor_compra=0
        valor_iva=19
        valor_ic=0
        impuesto_licor=0
        impuesto_bolsa="no"

        with self.assertRaises(BuyLogic.ErrorValorCompra):
            resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

    def test_valor_negativo_IVA(self):
        valor_compra=78000
        valor_iva=-12
        valor_ic=0
        impuesto_licor=0
        impuesto_bolsa="si"

        with self.assertRaises(BuyLogic.ErrorValorIVA):
            resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

    def test_valor_negativo_IC(self):
        valor_compra=65000
        valor_iva=19
        valor_ic=-5
        impuesto_licor=0
        impuesto_bolsa="no"

        with self.assertRaises(BuyLogic.ErrorValorIC):
            resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

    def test_valor_negativo_licor(self):
        valor_compra=130000
        valor_iva=19
        valor_ic=0
        impuesto_licor=-6
        impuesto_bolsa="si"

        with self.assertRaises(BuyLogic.ErrorImpuestoLicor):
            resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

    def test_valor_parametro_bolsa(self):
        valor_compra=23380
        valor_iva=5
        valor_ic=5
        impuesto_licor=0
        impuesto_bolsa="None"

        with self.assertRaises(BuyLogic.ErrorParametroBolsa):
            resultado = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)



if __name__ == "__main__":
    unittest.main()