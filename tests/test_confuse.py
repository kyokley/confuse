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

    def test_integer_substitution(self):
        sample_str = '%i apples and %i oranges'
        expected = u'%i \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %i \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_octal_substitution(self):
        sample_str = '%o apples and %o oranges'
        expected = u'%o \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %o \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_lowercase_hex_substitution(self):
        sample_str = '%x apples and %x oranges'
        expected = u'%x \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %x \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_uppercase_hex_substitution(self):
        sample_str = '%X apples and %X oranges'
        expected = u'%X \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %X \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_number_substitution(self):
        sample_str = '%n apples and %n oranges'
        expected = u'%n \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %n \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_binary_substitution(self):
        sample_str = '%b apples and %b oranges'
        expected = u'%b \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %b \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_substitution(self):
        sample_str = '%(first)s, %(second)s, or %(third)s'
        expected = u'%(first)s\u275f %(second)s\u275f \xf0\u0155 %(third)s'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)
