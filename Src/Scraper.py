#
#
#    This program scrapes the FIFA Data from the site:
#        http://thesoccerworldcups.com/index.php
#
#

from lxml import html
from io import BytesIO
import urllib2
import os

#####################################################################
# Global variables and constants                                    #
#####################################################################

year_wise_urls = (
                     'http://thesoccerworldcups.com/world_cups/1930_',
                     'http://thesoccerworldcups.com/world_cups/1934_',
                     'http://thesoccerworldcups.com/world_cups/1938_',
                     'http://thesoccerworldcups.com/world_cups/1950_',
                     'http://thesoccerworldcups.com/world_cups/1954_',
                     'http://thesoccerworldcups.com/world_cups/1958_',
                     'http://thesoccerworldcups.com/world_cups/1962_',
                     'http://thesoccerworldcups.com/world_cups/1966_',
                     'http://thesoccerworldcups.com/world_cups/1970_',
                     'http://thesoccerworldcups.com/world_cups/1974_'
                     'http://thesoccerworldcups.com/world_cups/1978_',
                     'http://thesoccerworldcups.com/world_cups/1982_',
                     'http://thesoccerworldcups.com/world_cups/1986_',
                     'http://thesoccerworldcups.com/world_cups/1990_',
                     'http://thesoccerworldcups.com/world_cups/1994_',
                     'http://thesoccerworldcups.com/world_cups/1998_',
                     'http://thesoccerworldcups.com/world_cups/2002_',
                     'http://thesoccerworldcups.com/world_cups/2006_',
                     'http://thesoccerworldcups.com/world_cups/2010_',
                     'http://thesoccerworldcups.com/world_cups/2014_'

                 );

#####################################################################
# Implementation of classes starts here                             #
#####################################################################

#####################################################################
# Implementation of functions starts here                           #
#####################################################################

def get_page( url ):

    if not url:
        return False

    try:

        request  = urllib2.Request( url     )
        response = urllib2.urlopen( request )
        data     = response.read()
        return data

    except urllib2.HTTPError as e: 

        print "The url" + url + "returned with error code " + e.code + " and " + e.read()
        return False


def create_directory( directory ):

    if not os.path.exists( directory ):
        os.makedirs( directory )


def get_wc_years_venues( html_content ):

    if not html_content:
        return False

    main_file = open( 'data/mainfile.csv' , 'wb' )

    try:

        page = html.fromstring( html_content )
        rows = page.xpath('//body//div[@class="todo"]//div[@class="contenido"]//article//div[@class="col_central"]//table[@class="c0s5"]')[0].findall( 'tr' );
        for row in rows:
            for child in row.getchildren():
                for rowchild in child.getchildren():
                    if ( rowchild.get( 'href' ) ):
                        main_file.write( rowchild.text.strip() + ',' + rowchild.get( 'href' ) + ',' )
            main_file.write( "\n" )

    except:
        main_file.close()
        print "Something went bonkers!!!"

    main_file.close()

def get_overall_winner_stats():




#####################################################################
# Main function                                                     #
#####################################################################

root_data = get_page( 'http://thesoccerworldcups.com/world_cups.php' )

create_directory( 'data' )
get_wc_years_venues( root_data )
