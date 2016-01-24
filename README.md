# BGP Data Finder

Author: Sebastian Castro <sebastian@nzrs.net.nz>

## Introduction

This package encapsulates the rules to identify and extract the URLs where 
BGP data from three BGP sources lives.

Currently can find data for

* RouteViews http://archive.routeviews.org  
* RIPE RIS https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris/ris-raw-data  
* PCH https://www.pch.net/resources/Routing_Data/  

BGP Routing data is useful for Internet topology analysis. NZRS uses it
to develop visualization of the Internet in New Zealand.

## Instructions

Because all three packages share the same interface, the sequence to
find the right URLs is
 
1. Create object
2. Find the potential sources of data (collectors)
3. Find the files provided by the collectors corresponding to a date
   (today by default)

With the list of URLs, you can use any program to download them

## Example

There is a complete example in the test-bgp-data-finder.py script

Output will look like

```
http://archive.routeviews.org/route-views3/bgpdata/2015.08/RIBS/rib.20150812.2200.bz2
http://data.ris.ripe.net/rrc10//2015.08/bview.20150812.1600.gz
https://www.pch.net/resources/Routing_Data/2015/route-collector.lba.pch.net/route-collector.lba.pch.net.2015.08.12.gz
```

The `transform-to-curl.py` script takes the URLs and generates a
configuration file for CURL. To download using curl, you could

```
curl -K <(python test-bgp-data-finder.py | python transform-to-curl.py)
```
