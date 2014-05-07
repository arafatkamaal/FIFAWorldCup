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

year_wise_urls = {
                     '1930' : 'http://thesoccerworldcups.com/world_cups/1930_',
                     '1934' : 'http://thesoccerworldcups.com/world_cups/1934_',
                     '1938' : 'http://thesoccerworldcups.com/world_cups/1938_',
                     '1950' : 'http://thesoccerworldcups.com/world_cups/1950_',
                     '1954' : 'http://thesoccerworldcups.com/world_cups/1954_',
                     '1958' : 'http://thesoccerworldcups.com/world_cups/1958_',
                     '1962' : 'http://thesoccerworldcups.com/world_cups/1962_',
                     '1966' : 'http://thesoccerworldcups.com/world_cups/1966_',
                     '1970' : 'http://thesoccerworldcups.com/world_cups/1970_',
                     '1974' : 'http://thesoccerworldcups.com/world_cups/1974_',
                     '1978' : 'http://thesoccerworldcups.com/world_cups/1978_',
                     '1982' : 'http://thesoccerworldcups.com/world_cups/1982_',
                     '1986' : 'http://thesoccerworldcups.com/world_cups/1986_',
                     '1990' : 'http://thesoccerworldcups.com/world_cups/1990_',
                     '1994' : 'http://thesoccerworldcups.com/world_cups/1994_',
                     '1998' : 'http://thesoccerworldcups.com/world_cups/1998_',
                     '2002' : 'http://thesoccerworldcups.com/world_cups/2002_',
                     '2006' : 'http://thesoccerworldcups.com/world_cups/2006_',
                     '2010' : 'http://thesoccerworldcups.com/world_cups/2010_',
                     '2014' : 'http://thesoccerworldcups.com/world_cups/2014_'

                 }

sections = {
               'overview'        : 'world_cup.php',
               'results'         : 'results.php',
               'playoffs'        : 'playoffs.php',
               'top_scorers'     : 'top_scorers.php',
               'final_standings' : 'final_standings.php'
           }

       

#####################################################################
# Implementation of classes starts here                             #
#####################################################################

class Overview:

    def get_overall_winner_stats( self ):

        section = sections['overview']
        for year_wise_url in year_wise_urls.keys():
            url  = year_wise_urls[year_wise_url] + section
            page = get_page( url )

            if False == page:
                print 'Unable to process to overwall winner stats for url ' + url
                exit()

            champion = self.get_champion( page )


    def get_champion( self , html_content ):

        try:

            page     = html.fromstring( html_content )
            champion = page.xpath('//body//div[@class="todo"]//div[@class="contenido"]//article//div[@class="col_central"]//table[@cellspacing="0"]//tbody//tr[@align="center"]//td[@width="33%"]//table[@cellspacing="0"]//tbody//td[@align="center"]//h3')

            print champion

        except:
            print "Something went bonkers!!!"

        




#####################################################################
# Implementation of functions starts here                           #
#####################################################################

def get_page( url ):

    if not url:
        return False

    try:

        print "Getting url " + url
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
        rows = page.xpath('//body//div[@class="todo"]//div[@class="contenido"]//article//div[@class="col_central"]//table[@class="c0s5"]')[0].findall( 'tr' )
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


#####################################################################
# Main function                                                     #
#####################################################################

#root_data = get_page( 'http://thesoccerworldcups.com/world_cups.php' )

create_directory( 'data' )
#get_wc_years_venues( root_data )

overall_stats = Overview();
overall_stats.get_overall_winner_stats()
