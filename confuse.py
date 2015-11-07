import random
from alphabet import confusablesDict

def confuse(string):
    output = []
    for char in string:
        if char in confusablesDict:
            output.append(random.choice(confusablesDict[char]))
        else:
            output.append(char)
    return ''.join(output)