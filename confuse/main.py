import re
import polib
import sys

from alphabet import confusablesDict

NAMED_SUB_STR_REGEX = r'%(\S+)[sdiouxXeEfFgGcr]'
UNNAMED_SUB_STR_REGEX = r'%[sdiouxXeEfFgGcr]'
FORMATTER_REGEX = r'{\S?}'
HTML_TAG_REGEX = r'''</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>'''
regexes = [NAMED_SUB_STR_REGEX,
           UNNAMED_SUB_STR_REGEX,
           FORMATTER_REGEX,
           HTML_TAG_REGEX,
           ]

def get_stdin():
    return sys.stdin.readlines()

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

def main():
    if len(sys.argv) > 1:
        print(' '.join([confuse(x) for x in sys.argv[1:]]))
    else:
        for line in get_stdin():
            print(confuse(line))

if __name__ == '__main__':
    main()
