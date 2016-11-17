import unittest
from confuse import confuse

class TestConfuse(unittest.TestCase):
    def test_simple_string(self):
        sample_str = 'simple string'
        expected = u'\u015f\xef\u1e41\u1d7d\u0142\xeb \u015f\u0167\u0155\xef\xf1\u011f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_digits(self):
        sample_str = '1234'
        expected = u'\u2460\u2461\u2462\u2463'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_string_substitution(self):
        sample_str = '%s and %s'
        expected = u'%s \xe3\xf1\u1d81 %s'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_numeric_substitution(self):
        sample_str = '%d apples and %d oranges'
        expected = u'%d \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %d \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_substitution(self):
        sample_str = '%(first)s, %(second)s, or %(third)s'
        expected = u'%(first)s\u275f %(second)s\u275f \xf0\u0155 %(third)s'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)
