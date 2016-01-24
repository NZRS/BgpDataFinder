from __future__ import print_function
__author__ = 'sebastian@nzrs.net.nz'

"""Generic abstract class to describe access to a BGP data provider"""

import sys

class BgpDataFinder(object):
    show_debug = False
    base_url = None
    today = None

    def __init__(self):
        # Create a fetcher object to crawl and discover
        self.base_url = None

    def error(self, *objs):
        print("ERROR: ", *objs, file=sys.stderr)

    def warning(self, *objs):
        print("WARNING: ", *objs, file=sys.stderr)

    def debug(self, *objs):
        if self.show_debug:
            print("DEBUG: ", *objs, file=sys.stderr)

    def findsources(self):
        # Use the base URL, crawl and extract potential sources
        raise NotImplementedError("This method requires implementation")

    def findlatest(self):
        # Go over the list of detected sources and find the latest file
        # available
        raise NotImplementedError("This method requires implementation")

    def getlatest(self):
        raise NotImplementedError("This method requires implementation")

