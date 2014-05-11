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


##########################
#Main program starts here#
##########################

insights_directory = 'insights'
insights_file      = insights_directory + "/insights.html"

if not os.path.exists( insights_directory ):
    os.makedirs( insights_directory  )


generate_html_header( insights_file )
write_to_file( insights_file ,'<br><br><h1 style="font-family:Nobile; text-align:center">FIFA World cup Insights<h1>' )
generate_html_footer( insights_file ) 
