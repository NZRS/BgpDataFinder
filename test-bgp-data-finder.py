__author__ = 'secastro'

from RouteViewsBgpDataFinder import RouteViewsBgpDataFinder
from RipeRisBgpDataFinder import RipeRisBgpDataFinder
from PchBgpDataFinder import PchBgpDataFinder
import datetime

bgp_urls = []
# for provider in [RouteViewsBgpDataFinder(), RipeRisBgpDataFinder()]:
for provider in [PchBgpDataFinder()]:
    provider.show_debug = True
    # First step, find the sources
    provider.findsources()
    # Second step, fetch the URL with data
    provider.findlatest()
    bgp_urls = bgp_urls + provider.getlatest()

for url in bgp_urls:
    print url

