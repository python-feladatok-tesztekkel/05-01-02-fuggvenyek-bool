from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestPozitivE(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.pozitiv_e(5)
        elvart = True
        self.assertEqual(elvart, aktualis, "Nullánál nagyobb számok esetén a pozitiv-e függvény nem megfelelően működik")
    def test_feladat02(self):
        aktualis = feladatok.pozitiv_e(0)
        elvart = False
        self.assertEqual(elvart, aktualis, "Nem pozitív szám esetén a pozitiv-e függvény nem megfelelően működik")
    def test_feladat03(self):
        aktualis = feladatok.pozitiv_e(-5)
        elvart = False
        self.assertEqual(elvart, aktualis, "Nem pozitív szám esetén a pozitiv-e függvény nem megfelelően működik")

