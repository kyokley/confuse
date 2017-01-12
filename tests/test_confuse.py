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

    def test_lowercase_exp_substitution(self):
        sample_str = '%e apples and %e oranges'
        expected = u'%e \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %e \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_uppercase_exp_substitution(self):
        sample_str = '%E apples and %E oranges'
        expected = u'%E \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %E \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_floating_point_substitution(self):
        sample_str = '%f apples and %f oranges'
        expected = u'%f \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %f \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_floating_point_substitution2(self):
        sample_str = '%F apples and %F oranges'
        expected = u'%F \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %F \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_g_substitution(self):
        sample_str = '%g apples and %g oranges'
        expected = u'%g \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %g \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_G_substitution(self):
        sample_str = '%G apples and %G oranges'
        expected = u'%G \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %G \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_char_substitution(self):
        sample_str = '%c apples and %c oranges'
        expected = u'%c \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %c \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_repr_substitution(self):
        sample_str = '%r apples and %r oranges'
        expected = u'%r \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %r \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_substitution(self):
        sample_str = '%(first)s, %(second)s, or %(third)s'
        expected = u'%(first)s\u275f %(second)s\u275f \xf0\u0155 %(third)s'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_numeric_substitution(self):
        sample_str = '%(first)d apples and %(second)d oranges'
        expected = u'%(first)d \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)d \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_integer_substitution(self):
        sample_str = '%(first)i apples and %(second)i oranges'
        expected = u'%(first)i \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)i \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_octal_substitution(self):
        sample_str = '%(first)o apples and %(second)o oranges'
        expected = u'%(first)o \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)o \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_lowercase_hex_substitution(self):
        sample_str = '%(first)x apples and %(second)x oranges'
        expected = u'%(first)x \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)x \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_uppercase_hex_substitution(self):
        sample_str = '%(first)X apples and %(second)X oranges'
        expected = u'%(first)X \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)X \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_lowercase_exp_substitution(self):
        sample_str = '%(first)e apples and %(second)e oranges'
        expected = u'%(first)e \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)e \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_uppercase_exp_substitution(self):
        sample_str = '%(first)E apples and %(second)E oranges'
        expected = u'%(first)E \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)E \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_floating_point_substitution(self):
        sample_str = '%(first)f apples and %(second)f oranges'
        expected = u'%(first)f \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)f \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_floating_point_substitution2(self):
        sample_str = '%(first)F apples and %(second)F oranges'
        expected = u'%(first)F \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)F \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_g_substitution(self):
        sample_str = '%(first)g apples and %(second)g oranges'
        expected = u'%(first)g \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)g \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_G_substitution(self):
        sample_str = '%(first)G apples and %(second)G oranges'
        expected = u'%(first)G \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)G \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_char_substitution(self):
        sample_str = '%(first)c apples and %(second)c oranges'
        expected = u'%(first)c \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)c \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)

    def test_keyword_repr_substitution(self):
        sample_str = '%(first)r apples and %(second)r oranges'
        expected = u'%(first)r \xe3\u1d7d\u1d7d\u0142\xeb\u015f \xe3\xf1\u1d81 %(second)r \xf0\u0155\xe3\xf1\u011f\xeb\u015f'
        actual = confuse(sample_str)
        self.assertEqual(expected, actual)
