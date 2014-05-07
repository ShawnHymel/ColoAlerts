#-------------------------------------------------------------------------------
# ColoAlerts
#
# Refreshes ColoProperty.com search criteria on a regular basis. Any new
# listings found are emailed to the provided email account.
#
# Author: Shawn Hymel
# Date: May 7, 2014
# License: 
#  Copyright (C) <year> <copyright holders>
#  Permission is hereby granted, free of charge, to any person obtaining a copy 
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights 
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
#  copies of the Software, and to permit persons to whom the Software is 
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in 
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#-------------------------------------------------------------------------------

import urllib2
import os.path

#-------------------------------------------------------------------------------
# User parameters
#-------------------------------------------------------------------------------

# Fill this with the site you wish to set alerts on
SEARCH_SITE = "http://www.coloproperty.com/listing/list?rawLoc=&typeId=2&cityId=9&mlsNumber=&zip=&stNumber=&stName=&prMin=%24170%2C000&prMax=%24250%2C000&bed=2&bath=&sqFtMin=&sqFtMax=&yrBuiltMin=&yrBuiltMax=&lsMin=&lsMax=&garSpace=1&garType=&style=&hoaMax=&subdiv=&elemSch=&midSch=&highSch=&walkMin=&orderBy=mlsDsc&perPage=50&searchFor=listing&page=1&reportFormat=quick"

# Substring on which to search (how we find listings)
LISTING_STRING = 'onclick="window.viewDetails('

# Number of digits in listing number
NUM_LISTING_DIGITS = 7

# File that stores the last listings seen
LAST_LISTINGS_FILE = 'last_listings.txt'

#-------------------------------------------------------------------------------
# Import custom modules
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

# Array of listings seen on last refresh
last_listings = []

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

# Read in last listing numbers from text file (if file exists)
def read_last_listings():

    # If file exists, open and read contents
    if os.path.isfile(LAST_LISTINGS_FILE):
        with open(LAST_LISTINGS_FILE, 'r') as f:
            content = f.read()
        print content

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

# Runs the main ColoAlerts loop. Checks site regularly and sends email alerts.
def run_main():
    
    # Refresh site
    site_html = urllib2.urlopen(SEARCH_SITE).read()
    
    # Find listings
    listings = []
    index = 0
    while index < len(site_html):
        index = site_html.find(LISTING_STRING, index)
        if index == -1:
            break
        listings.append(site_html[(index + len(LISTING_STRING) + 1): \
                        (index + len(LISTING_STRING) + NUM_LISTING_DIGITS + 1)])
        index += len(LISTING_STRING)
    
    print listings
    
    read_last_listings()

# Run main
if __name__ == "__main__":
    run_main()