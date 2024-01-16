import unittest

import flexmock

from flexmock_unittest_repro.flexmock_repro_code import add_constant

class TestYesFlexmock(unittest.TestCase):
    def test_yes_flexmock_add_constant_success(self):
        n = 4
        self.assertEqual(add_constant(n), 7)

    def test_yes_flexmock_add_constant_fail(self):
        n = 4
        self.assertEqual(add_constant(n), 8)
