from urlparse import urlparse
import sys

"""Transform an input file with URLs to a configuration file for CURL"""

print("create-dirs")
for line in sys.stdin:
    l = line.rstrip("\n")

    print("url = \"%s\"" % l)
    print("output = \"data/%s\"" % urlparse(line.rstrip("\n")).path[1:])
