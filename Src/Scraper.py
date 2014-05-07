#
#
#    This program scrapes the FIFA Data from the site:
#        http://thesoccerworldcups.com/index.php
#
#


import urllib2



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


#####################################################################
# Main function                                                     #
#####################################################################

get_page( 'http://www.google.com' )                              
