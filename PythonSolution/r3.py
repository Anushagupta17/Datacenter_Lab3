#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
current_patent = None
current_patent_info = None
current_patent_citations_count = 0


def outputPatentInfo():
    global current_patent
    global current_patent_info
    global current_patent_citations_count

    if current_patent != None and current_patent_info != None:
        try:
            #print("%s" % (current_patent_citations_count))
            print("%s,%s,%s" % (current_patent, current_patent_info, current_patent_citations_count))
        except ValueError:
            #
            # Something wrong in number format
            #
            pass
        except Exception as e:
            # print("Something died", e)
            pass

    current_patent = None
    current_patent_info = None
    current_patent_citations_count = 0

def main():
    global current_patent
    global current_patent_info
    global current_patent_citations_count

    current_patent = None
    debug = False
    
    # input comes from STDIN
    for line in sys.stdin:
        # parse the input we got from mapper.py
        line = line.strip()
        key, value = line.split('\t', 1)
        # convert count (currently a string) to int
        try:
            patent = long(key)
        except ValueError:
            # key was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer

        if current_patent != patent:
            outputPatentInfo()

        current_patent = patent
        fields = value.split(',')
        
        if len(fields) > 2:
            current_patent_info = value
        else:
            if fields[0] != '""' and fields[1] != '""' and fields[0] == fields[1]:
                current_patent_citations_count = current_patent_citations_count + 1;
        
    # do not forget to output the last word if needed!
    outputPatentInfo()


main()
