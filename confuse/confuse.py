import random, re
from alphabet import confusablesDict

NAMED_SUB_STR_REGEX = r'%(\S+)[sd]'
UNNAMED_SUB_STR_REGEX = r'%[sd]'
FORMATTER_REGEX = r'{\S}'
regexes = [NAMED_SUB_STR_REGEX,
           UNNAMED_SUB_STR_REGEX,
           FORMATTER_REGEX,
           ]
test_str = 'this is a test string with %(formatter)s'

def confuse(string):
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
                output.append(random.choice(confusablesDict[char]))
            else:
                if isinstance(char, str):
                    output.append(char.decode('utf-8'))
                else:
                    output.append(char)

            pos += 1
    return u''.join(output)
