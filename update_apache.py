#!/usr/bin/env python

import sys, os, re
import datetime
import time
import random

try:
    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write("[Error]: %s is not a file\n" % sys.argv[1])
        sys.exit(1)
except IndexError:
    sys.stderr.write("Usage: process_data.py file1 file2\n")
    sys.exit(1)



with open(sys.argv[1]) as file1, open(sys.argv[2],'a+') as file2:
    for line in file1:
        array1=line.strip().split('[')
        array2=array1[1].strip().split(']')
        datetime_object = datetime.datetime.now()
        
        timestamp=datetime_object.strftime("%d/%b/%Y:%H:%M:%S +0800")
        file2.write(array1[0]+'['+timestamp+']'+array2[1]+'\n')

        time.sleep(random.uniform(0.00314,0.00628))

