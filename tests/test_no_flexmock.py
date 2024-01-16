import unittest
from flexmock_unittest_repro.flexmock_repro_code import add_constant

class TestNoFlexmock(unittest.TestCase):
    def test_no_flexmock_add_constant_success(self):
        n = 4
        self.assertEqual(add_constant(n), 7)

    def test_no_flexmock_add_constant_fail(self):
        n = 4
        self.assertEqual(add_constant(n), 8)
