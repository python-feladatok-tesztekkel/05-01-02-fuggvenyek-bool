from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestJegyE(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.erdemjegy_e(5)
        elvart = True
        self.assertEqual(elvart, aktualis, "Az erdemjegy-e függvény nem megfelelően működik")

    def test_feladat02(self):
        aktualis = feladatok.erdemjegy_e(1)
        elvart = True
        self.assertEqual(elvart, aktualis, "Az erdemjegy-e függvény nem megfelelően működik")

    def test_feladat03(self):
        aktualis = feladatok.erdemjegy_e(6)
        elvart = False
        self.assertEqual(elvart, aktualis, "Az erdemjegy-e függvény nem megfelelően működik")

    def test_feladat04(self):
        aktualis = feladatok.erdemjegy_e(0)
        elvart = False
        self.assertEqual(elvart, aktualis, "Az erdemjegy-e függvény nem megfelelően működik")

    def test_feladat05(self):
        aktualis = feladatok.erdemjegy_e(-10)
        elvart = False
        self.assertEqual(elvart, aktualis, "Az erdemjegy-e függvény nem megfelelően működik")

