#
#
# This python program generates insights for the data generated for FIFA world cup
#
#


import codecs
import os


def write_to_file( html_file , data ):

    html = codecs.open( html_file , 'ab' , encoding='utf8' )
    html.write( data )
    html.close()

def generate_html_header( html_file ):

    write_to_file( html_file , "<html>" )
    write_to_file( html_file , "<head>" )
    write_to_file( html_file , "<link href='http://fonts.googleapis.com/css?family=Nobile:400,400italic,700,700italic' rel='stylesheet' type='text/css'>" )
    write_to_file( html_file , "<title>FIFA world cup historic insights</title>" )
    write_to_file( html_file , "</head>" )
    write_to_file( html_file , '<body bgcolor="silver"'  )
  
def generate_html_footer( html_file ):

    write_to_file( html_file , "</body>" )
    write_to_file( html_file , "</html>" )


def generate_table_header( html_file , fields , close_header , title ):

   if True == close_header:
        write_to_file( html_file , '</table>' )
        return 

   #write_to_file( html_file , '<br><br><br>' )
   write_to_file( insights_file ,'<h2 style="font-family:Nobile; text-align:center">' + title + '<h1>' )
   write_to_file( html_file , '<table style="border:1px;width:300px;font-family:Nobile;font-size:12;text-align:center;margin: 0px auto">' )
   write_to_file( html_file , '<tr>'  )

   for field in fields:
       write_to_file( html_file , '<th>' + field + '</th>' )

   write_to_file( html_file , '</tr>' )

def generate_table_row( html_file , fields ):

    write_to_file( html_file , '<tr>'  )
    for field in fields:
        write_to_file( html_file , '<td>' + field + '</td>' )
    write_to_file( html_file , '</tr>' )

##########################
#Main program starts here#
##########################

insights_directory = 'insights'
insights_file      = insights_directory + "/insights.html"

if not os.path.exists( insights_directory ):
    os.makedirs( insights_directory  )


generate_html_header( insights_file )
write_to_file( insights_file ,'<br><br><h1 style="font-family:Nobile; text-align:center">FIFA World cup Insights<h1>' )


write_to_file( insights_file , '<br><br><br>' )

header = [ 'one' , 'two' , 'three' ]
row1   = [ '1' , '2' , '3' ]
row2   = [ '4' , '5' , '6' ]

generate_table_header( insights_file , header , False , "Test table" )
generate_table_row( insights_file , row1 )
generate_table_row( insights_file , row2 )
generate_table_header( insights_file , None , True , '' )

generate_table_header( insights_file , header , False , "Test table" )
generate_table_row( insights_file , row1 )
generate_table_row( insights_file , row2 )
generate_table_header( insights_file , None , True , '' )


generate_html_footer( insights_file )

