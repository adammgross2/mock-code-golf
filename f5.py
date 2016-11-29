import random
import sys

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


num = None
try:
    num = int(sys.argv[sys.argv.index(__file__) + 1])
    if num < 1 or num > 100:
