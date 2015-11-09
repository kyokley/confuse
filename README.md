# Confuse
Convert ascii strings to commonly confused unicode characters

## Purpose
Those familiar with xgettext know that in order to provide translations it is necessary to tag strings requiring translation with a function, normally gettext(...) or the commonly used alias _(...).

While attempting to confirm full i18n support for an application it became necessary to find all strings that were missing the proper translation functions. It was proposed that a dummy language be created that provides a translation for every entry in a PO file in such a way that the msgid and msgstr be mostly similar but still discernible.

The purpose of Confuse is to take a string with all ascii characters and return a lookalike string using unicode characters. The goal is for the string to remain readable but altered enough that it is clearly visible. For example:

```
this is a test -> ŧħïş ïş ã ŧëşŧ
```

## Usage
```
>>> from confuse import confuse
>>> confuse('this is a string')
u'\u0167\u0127\xef\u015f \xef\u015f \xe3 \u015f\u0167\u0155\xef\xf1\u011f'
>>> confuse('this is a string').encode('utf-8')
'\xc5\xa7\xc4\xa7\xc3\xaf\xc5\x9f \xc3\xaf\xc5\x9f \xc3\xa3 \xc5\x9f\xc5\xa7\xc5\x95\xc3\xaf\xc3\xb1\xc4\x9f'
>>> print confuse('this is a string').encode('utf-8')
ŧħïş ïş ã şŧŕïñğ
```

Confuse tries to be smart about skipping things that should not be altered. Therefore, it tries to recognize various python string formatters as well as anything contained in an HTML tag.
```
>>> foo = 'Hi, my name is %(name)s'
>>> print confuse(foo)
Ĥï❟ ṁý ñãṁë ïş %(name)s
>>> bar = 'I like {} and {}'
>>> print confuse(bar)
Į ļïķë {} ãñᶁ {}
>>> baz = '<a href="index.html">This is a link to %s</a>'
>>> print confuse(baz)
<a href="index.html">Ŧħïş ïş ã ļïñķ ŧð %s</a>
```

## Why Confuse?
The Unicode Consortium has a utility to generate a set of confusable characters (a.k.a. confusables) for a given input. The purpose of this program is to generate something similar.
