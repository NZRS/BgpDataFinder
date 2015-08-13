# BGP Data Finder

Author: Sebastian Castro <sebastian@nzrs.net.nz>

## Introduction

This package encapsulates the rules to identify and extract the URLs where 
BGP data from three BGP sources lives.

Currently can find data for

* RouteViews http://archive.routeviews.org  
* RIPE RIS https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris/ris-raw-data  
* PCH https://www.pch.net/resources/Routing_Data/  

BGP Routing data is useful for Internet analysis. NZRS uses it to develop 
visualization of the Internet in New Zealand.

## Instructions

Because all three packages share the same interface, the sequence to find the
 right URLs is
 
1. Create object
2. Find the potential sources of data (collectors)
3. Find the files provided by the collectors corresponding to a date (today 
by default)

With the list of URLs, you can use any program to download them

## Example

There is a complete example in the test-bgp-data-finder.py script
