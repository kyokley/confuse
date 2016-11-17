import re, polib
from alphabet import confusablesDict

NAMED_SUB_STR_REGEX = r'%(\S+)[sd]'
UNNAMED_SUB_STR_REGEX = r'%[sd]'
FORMATTER_REGEX = r'{\S?}'
HTML_TAG_REGEX = r'''</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>'''
regexes = [NAMED_SUB_STR_REGEX,
           UNNAMED_SUB_STR_REGEX,
           FORMATTER_REGEX,
           HTML_TAG_REGEX,
           ]

def confuse(string, encoding='utf-8'):
    output = []
    pos = 0
    while pos < len(string):
        for regex in regexes:
            pattern = re.compile(regex)
            match = pattern.match(string, pos)

            if match:
                pos = match.end(0)
                output.extend(match.group(0))
                break
        else:
            char = string[pos]
            if char in confusablesDict:
                output.append(confusablesDict[char][0])
            else:
                if isinstance(char, str):
                    output.append(char.decode(encoding))
                else:
                    output.append(char)

            pos += 1
    return u''.join(output)

def confusePO(filename):
    po = polib.pofile(filename)
    for entry in po:
        entry.msgstr = confuse(entry.msgid)
    po.save()
