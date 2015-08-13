__author__ = 'sebastian@nzrs.net.nz'

"""Implements the BgpDataFinder interface to get the URL with BGP MRT dumps
from RIPE RIS to the latest day, or an specific day"""

from BgpDataFinder import BgpDataFinder
from bs4 import BeautifulSoup
import urllib2
import re
import datetime
import urlparse


class RouteViewsBgpDataFinder(BgpDataFinder):
    sources = []
    latest = []
    bs4_parser = "html.parser"

    def __init__(self):
        self.base_url = "http://archive.routeviews.org"

    def findsources(self):
        response = urllib2.urlopen(self.base_url)
        html = BeautifulSoup(response.read(), self.bs4_parser)
        for link in html.findAll('a',
                                 text=re.compile('^\sMRT\s+format\s+RIBs')):
            self.sources.append(urlparse.urljoin(response.geturl(),
                                                 link['href']))

        return self.sources

    def findlatest(self, today=datetime.date.today()):
        self.today = today
        self.latest = []
        file_pat = "rib\.%s\.\d{4}\.bz2$" % self.today.strftime("%Y%m%d")
        self.debug("Using pattern %s" % file_pat)
        for source in self.sources:
            src_url = self._generate_url(source)
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

    def _generate_url(self, s):
        return "{}/{:04d}.{:02d}/RIBS/".format(s, self.today.year,
                                               self.today.month)
