#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models import base_model
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8

class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
class TestBaseModelDoc(unittest.TestCase):
    """Contains tests for documentation in base_model"""

    def test_module_doc(self):
        """Checks for documentation in base_model module"""
        self.assertGreaterEqual(len(base_model.__doc__), 1)

    def test_class_doc(self):
        """Checks for documentation in BaseClass"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    def test_init_doc(self):
        """Checks for documentation of __init__ method"""
        self.assertGreaterEqual(len(BaseModel.__init__.__doc__), 1)

    def test_str_doc(self):
        """Checks for documentation of __str__ method"""
        self.assertGreaterEqual(len(BaseModel.__str__.__doc__), 1)

    def test_save_doc(self):
        """Checks for documentation of save() method"""
        self.assertGreaterEqual(len(BaseModel.save.__doc__), 1)

    def test_to_dict_doc(self):
        """Checks for documentation of to_dict() method"""
        self.assertGreaterEqual(len(BaseModel.to_dict.__doc__), 1)

class TestBaseModelPep8(unittest.TestCase):
    """Tests BaseModel Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base-model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/base_model.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([("tests/test_models"
                                       "/test_base_model.py")])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")