#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into CSV fields
    line = line.strip()
    words = line.split(",")
    
    if len(words) == 4:
        try:
            cite = long(words[1])
            print('%s\t%s,%s' % (words[1], words[2], words[3]))
        except Exception as e:
            # improperly formed citation number
            # print("Exception ", e)
            pass
    else:
        #
        # It's patent info 
        #
        try:
            cite = long(words[0])
            print('%s\t%s' % (words[0], ','.join(words[1:])))
        except Exception as e:
            # improperly formed citation number
            # print("Exception ", e)
            pass
