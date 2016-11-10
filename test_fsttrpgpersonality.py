import os
import unittest

from fsttrpgpersonality.traitsmodels import Disorders, Quirks, Phobias, Clothes, Hair, Affections, Personality


class TestCheckListEditorClasses(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('fuziontables.db')
        except WindowsError as e:
            print('failed to delete: ' + str(e))

    def test_initialization(self):
        d = Disorders()
        p = Phobias()
        q = Quirks()
        c = Clothes()
        h = Hair()
        a = Affections()


class TestPersonalityTraitModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('fuziontables.db')
        except WindowsError as e:
            print('failed to delete: ' + str(e))

    def test_initialization(self):
        p = Personality()
