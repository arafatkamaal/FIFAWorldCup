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
import re

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

class ResultsAndGroupData:

    group_summary_urls = {}
    match_result_urls  = {}

    url_prefix_groups  = "http://thesoccerworldcups.com/world_cups/" 
    url_prefix_match   = "http://thesoccerworldcups.com/"

    def get_results( self ):

        section = sections['results']
   
        for year_wise_url in year_wise_urls.keys():
            url  = year_wise_urls[year_wise_url] + section
            page = get_page( url )

            self.brief_results( page )
            return

    def get_group_results( self ):

        for group_summary_url in self.group_summary_urls:
            url  = self.url_prefix_groups + group_summary_url
            #page = get_page( url )
            #self.group_results( page , url )
            #exit()

        for match_result_url in self.match_result_urls:
            url  = self.url_prefix_match + match_result_url.replace( '../' , '' )
            page = get_page( url )
            self.match_results( page , url )
            exit()

    def match_results( self , html_content , url ):

       page  = html.fromstring( html_content )
       table = page.xpath('//html//body//div//div[2]//article//div//table//tr')

       first_team  = ''
       second_team = ''
       first_team_score = ''
       second_team_score = ''
       first_team_goal_scorers = ''
       second_team_goal_scorers = ''

       for table_row in table:
           for table_data in table_row.findall( 'td' ):
               if 'width' in table_data.attrib:

                   if table_data.attrib['width'] == "35%":
                       if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "right" ):
                           first_team = table_data.text
                       else:
                           second_team = table_data.text

                   if table_data.attrib['width'] == "5%":
                       if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "right" ):
                           first_team_score  = table_data.text
                       else:
                           second_team_score = table_data.text

               if 'colspan' in table_data.attrib:           

                   if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "right" ):
                       first_team_goal_scorers = first_team_goal_scorers + "|" + table_data.text
                   if ( 'align' not in table_data.attrib ):
                       for img in table_data.findall( 'img' ):
                           second_team_goal_scorers = second_team_goal_scorers + "".join([x for x in table_data.itertext()]).strip()

       table = page.xpath('//html//body//div//div[2]//article//div//div[2]//table//tr')

       position = ''
       jersey   = ''
       player   = ''
       for table_row in table:
           for table_data in table_row.findall( 'td' ):

               if ( 'height' in table_data.attrib ) and ( table_data.attrib['height'] == "20" ):
                   if table_data.text is not None:
                       position = table_data.text.strip()

               if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "right" ):
                   for div in table_data.findall( 'div' ):
                       jersey   = div.text.strip()

               if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "left" ):
                   if table_data.text is not None:
                       player = table_data.text.strip()

       table = page.xpath('/html/body/div/div[2]/article/div/div[3]/table//tr')

       for table_row in table:
          for table_data in table_row.findall( 'td' ):

              if ( 'height' in table_data.attrib ) and ( table_data.attrib['height'] == "20" ):
                  if table_data.text is not None:
                      position = table_data.text.strip()

              if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "right" ):
                  for div in table_data.findall( 'div' ):
                      jersey   = div.text.strip()

              if ( 'align' in table_data.attrib ) and ( table_data.attrib['align'] == "left" ):
                  if table_data.text is not None:
                      player = table_data.text.strip()

          #print position + "," + jersey + "," + player

       table = page.xpath('//html//body//div//div[2]//article//div//table[2]//tr')

       team = ''
       player = ''
       card = ''
       for table_row in table:
           column = 0
           for table_data in table_row.findall( 'td' ):
               column = column + 1
               if ( 'height' in table_data.attrib ) and ( table_data.attrib['height'] == "20" ):
                   for img in table_data.findall( 'img' ):
                       team = "".join([x for x in table_data.itertext()]).strip()              

               if ( table_data.text is not None ) and ( column == 3 ):
                   player =  table_data.text.strip()

               if ( table_data.text is not None ) and ( column == 5 ):
                   card =  "".join([x for x in table_data.itertext()]).strip()


           print team + "," + player + "," + card 

    def group_results( self , html_content , url ):

        page  = html.fromstring( html_content )
        table = page.xpath('//html//body//div//div[2]//article//div//table[2]//tr[@align="right"]')

        serial_number = ''
        qualification = ''
        team          = ''
        pts           = '' 
        gp            = '' 
        w             = '' 
        d             = '' 
        l             = '' 
        gs            = ''
        ga            = ''
        gd            = ''

        groupresults_file = open( 'data/results.csv' , 'ab' )

        for table_row in table:
            row_number = 0
            for table_data in table_row.findall( 'td' ):

                row_number = row_number + 1

                if ( ( 'height' in table_data.attrib ) and ( 'class' in table_data.attrib ) and ( 'align' in table_data.attrib ) ):
                    serial_number = table_data.text.strip()

                if ( ( 'class' in table_data.attrib ) and ( 'align' in table_data.attrib ) and ( 'height' not in table_data.attrib ) ):
                    if table_data.attrib['align'] == 'center':
                        qualification = table_data.text 

                    if table_data.attrib['align'] == 'left':
                        for img in table_data.findall( 'img' ):
                            team = img.attrib['alt']

                if row_number == 3:
                    pts = table_data.text
                elif row_number == 4:
                    gp  = table_data.text
                elif row_number == 5:
                    w   = table_data.text
                elif row_number == 6:
                    d   = table_data.text
                elif row_number == 7:
                    l   = table_data.text
                elif row_number == 8:
                    gs  = table_data.text
                elif row_number == 9:
                    ga  = table_data.text
                elif row_number == 10:
                    gd  = table_data.text

            groupresults_file.write( serial_number + "|" + team + "|" + pts + "|" + gp + "|" + w + "|" + d + "|" + l + "|" + gs + "|" + ga + "|" + gd + "|" + qualification + "|" + url + "\n" )

        groupresults_file.close()

                 


    def brief_results( self , html_content ):

        serial_number = ''
        date          = ''
        first_team    = ''
        second_team   = ''
        result        = ''
        match_summary = ''
        group         = ''
        group_summary = ''

        overview_file = open( 'data/results.csv' , 'ab' )

        page  = html.fromstring( html_content )
        table = page.xpath('//html//body//div//div[2]//article//div//table//tr[@align="center"]')
        for table_row in table:
            for table_data in table_row.findall( 'td' ):

                #get the serial number
                if 'height' in table_data.attrib:
                    serial_number = table_data.text

                value = ''
                value = table_data.text
                if ( ( value != None ) and ( re.search( "[0-9]+$" , value ) ) ):
                    date = value          

                if ( ( 'class' in table_data.attrib ) and ( 'align' in table_data.attrib ) ):

                    if table_data.attrib['align'] == 'right':
                        first_team = table_data.text

                    if table_data.attrib['align'] == 'left':
                        second_team = table_data.text

                if 'class' in table_data.attrib:
                    score = table_data.findall( 'a' )
                    if table_data.attrib['class'] == 'scf12t':
                        for a in score:
                            result        = a.text
                            match_summary = a.attrib['href']
                            self.match_result_urls[match_summary] = 1
                else:
                    groups = table_data.findall( 'a' )
                    for a in groups:
                        if re.search ( 'Group' , a.text ):
                            group         = a.text.strip()
                        if re.search ( 'group' , a.attrib['href'] ):
                            group_summary = a.attrib['href'].strip()
                            self.group_summary_urls[group_summary] = 1
                            

            overview_file.write( serial_number + "|" + first_team + "|" + second_team + "|" + result + "|" + match_summary + "|" + group + "|" + group_summary + "\n" )

        overview_file.close()
                


class Overview:

    def get_results_overview( self , html_content ):

        try:

            page = html.fromstring( html_content )
            rows = page.xpath('//html/body//div//div[2]//article//div/table//tr//td[3]//p/text()')
            data = []
            for row in rows:
                data.append( row.replace( "-" , "" ).strip() )
 
            overview =  "|".join( data )
            return overview

        except IOError:
            print "Something went bonkers!!!"

    def get_champion( self , html_content ):

        try:

            page         = html.fromstring( html_content )
#            champion = page.xpath('//body//div[@class="todo"]//div[@class="contenido"]//article//div[@class="col_central"]//table[@cellspacing="0"]//tbody//tr[@align="center"]//td[@width="33%"]//table[@cellspacing="0"]//tbody//td[@align="center"]//h3')

            row          = page.xpath('//html//body//div//div[2]//article//div//table//tr//td[2]//table//tr//td[2]//h3')[0]
            raw_champion = row.text_content().split( )

            return raw_champion[1]
        except IOError:
            print "Something went bonkers!!!"

    def get_overall_winner_stats( self ):

        section = sections['overview']

        overview_file = open( 'data/overview.csv' , 'ab' )

        for year_wise_url in year_wise_urls.keys():
            url  = year_wise_urls[year_wise_url] + section
            page = get_page( url )

            if False == page:
                print 'Unable to process to overwall winner stats for url ' + url
                exit()

            champion = self.get_champion( page )
            overview = self.get_results_overview( page )

            overview_file.write( champion + "," + overview + "," + url + "\n" )

        overview_file.close()


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

#overall_stats = Overview();
#overall_stats.get_overall_winner_stats()

result_stats = ResultsAndGroupData()
result_stats.get_results()
result_stats.get_group_results()
