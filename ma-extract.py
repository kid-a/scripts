#-------------------------------------------------------------------------------
#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name: ma-extract
# Purpose: extract email addresses from given text or file
#
# Author: Loris Fichera <loris.fichera@iit.it>
#
# Created: 2012-02-09
# Licence: WTFPL 2
#-------------------------------------------------------------------------------
"""A program to extract email addresses from text."""

import re
import sys

if __name__ == "__main__":
    if len (sys.argv) < 2:
        print "usage: ma-extract.py \"STRING\" [DEST]"
        print "   or: ma-extract.py -f FILENAME [DEST]"
        exit (0)

    source = ""
    target = None
    if sys.argv[1] == "-f":
        f = open (sys.argv[2], 'r')
        for line in f.readlines ():
            source = source + line

        f.close ()

        if len (sys.argv) == 4: 
            target = open (sys.argv[3], 'w')

    else:
        source = sys.argv[1]
        if len (sys.argv) == 3:
            target = open (sys.argv[2], 'w')
    
    ## find all the email addresses
    occurrences = re.findall (r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}',
                             source)
    
    print len (occurrences), " email addresses found."

    ## if a destination has been specified
    if target is not None: 
        print "Writing them on ", target.name
        for o in occurrences:
            target.write (o)
            target.write ('\n')
        target.close ()
        
    else: 
        for o in occurrences:
            print o
