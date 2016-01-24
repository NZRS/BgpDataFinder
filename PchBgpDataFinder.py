__author__ = 'secastro'

__author__ = 'secastro'

from BgpDataFinder import BgpDataFinder
from bs4 import BeautifulSoup
import urllib2
import re
import datetime
import urlparse
from collections import defaultdict


class PchBgpDataFinder(BgpDataFinder):
    base_url = None
    sources = []
    latest = []
    bs4_parser = "html.parser"
    url_stash = defaultdict(list)

    def __init__(self):
        self.base_url = "https://www.pch.net/resources/Routing_Data" \
                        "/IPv4_daily_snapshots/"

    def findsources(self):
        response = urllib2.urlopen(self.base_url)
        html = BeautifulSoup(response.read(), self.bs4_parser)
        self.debug("1: %s" % response.geturl())
        # Find all the links corresponding to the year
        for link in html.findAll('a', href=re.compile('^201[6-9]/$')):
            # PCH has a three level structure, let's dig a little bit
            l2_link = urlparse.urljoin(self.base_url, link['href'])
            response2 = urllib2.urlopen(l2_link)
            self.debug("2: %s" % response2.geturl())
            month = BeautifulSoup(response2.read(), self.bs4_parser)
            for link2 in month.findAll('a', href=re.compile('^\d{2}/$')):
                l3_link = urlparse.urljoin(l2_link, link2['href'])
                response3 = urllib2.urlopen(l3_link)
                self.debug("3: %s" % response3.geturl())
                collector = BeautifulSoup(response3.read(), self.bs4_parser)
                for link3 in collector.findAll('a',
                                               href=re.compile('route\-collector\.\w{3}\.pch\.net/$')):
                        source_url = urlparse.urljoin(response3.geturl(),
                                                      link3['href'])
                        self.sources.append(source_url)
                        self.debug("*: %s" % source_url)
                        self.url_stash[link['href'][0:4]].append(source_url)

        return self.sources

    def findlatest(self, today=datetime.date.today()):
        self.today = today
        self.latest = []
        # Because sources for PCH include the year in the URL, we need to
        # filter those that are relevant to the date provided
        # If the year requested is not available, return an empty list
        source_sublist = self.url_stash.get(self.today.strftime("%Y"), [])

        file_pat = "ipv4_bgp_routes\.%s\.gz$" % self.today.strftime("%Y.%m.%d")
        self.debug("Using pattern %s" % file_pat)
        for source in source_sublist:
            src_url = source
            response = urllib2.urlopen(src_url)
            html = BeautifulSoup(response.read(), self.bs4_parser)
            link_list = []
            for link in html.findAll('a', href=re.compile(file_pat)):
                link_list.append(link['href'])

            """Return the largest value found, representing the latest month
            available"""
            if len(link_list) > 0:
                self.latest.append(src_url + sorted(link_list, reverse=True)[0])
            else:
                self.warning("%s didnt produce any link" % source)

    def getlatest(self):
        return self.latest

