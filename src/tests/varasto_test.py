import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktorille_negatiivinen_tilavuus(self):
        self.neg_varasto = Varasto(-10)
        self.assertAlmostEqual(self.neg_varasto.tilavuus, 0)

    def test_kostruktorille_neg_alkusaldo(self):
        self.neg_saldo_varasto = Varasto(10, -10)
        self.assertAlmostEqual(self.neg_saldo_varasto.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-10)

        # vapaata tilaa ennen lisäystä 10, ei pitäisi muuttua
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaa_enemman_kuin_varastossa_tilaa(self):
        self.varasto.lisaa_varastoon(11)

        # yritetään lisätä 11, vaikka mahtuu vain 10.
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-2)

        # lisätään 5, otetaan -2. Saldon ei pitäisi muuttua.
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_otetaan_enemmän_kuin_saldo(self):
        self.varasto.lisaa_varastoon(5)
        otto = self.varasto.ota_varastosta(6)

        #otetaan 6, varaston saldo 5, saadaan 5
        self.assertAlmostEqual(otto, 5)

    def test_varaston_saldo_ei_neg_kun_otetaan_yli_saldon(self):

        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(6)

        #otetaan 6, varaston saldo 5 -> varaston saldo 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tulostus(self):
        self.assertEqual(int(self.varasto), "saldo = 0, vielä tilaa 10")
        

