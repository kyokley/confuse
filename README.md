# Confuse
Convert ascii strings to commonly confused unicode characters

## Purpose
Those familiar with xgettext know that in order to provide translations it is necessary to tag strings requiring translation with a function, normally gettext(...) or the commonly used alias _(...).
While attempting to confirm full i18n support for an application it became necessary to find all strings that were missing the proper translation functions. It was proposed that a dummy language be created that provides a translation for every entry in a PO file in such a way that the msgid and msgstr be mostly similar but still discernible.
The purpose of Confuse is to take a string with all ascii characters and return a lookalike string using unicode characters. The goal is for the string to remain readable but altered enough that it is clearly visible.
