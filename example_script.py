from count import *

for (c, n) in count('example_script.py').stats.iteritems():
    print '%4d %1c : %d' % (ord(c), ' ' if c in ('\n', '\r', '\b') else c, n)