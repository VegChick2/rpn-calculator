import unittest

import rpn

class TestBasics(unittest.TestCase):
      def test_add(self):
         result = rpn.calculate('1 1 5 + -')
         self.assertEqual( -5  , result )
