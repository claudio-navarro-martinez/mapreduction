#!/usr/bin/python
import time
import sys

ip_pre = 'x'
day_pre = '00'
primera_linea = True
numclicks = 0
for lineas in sys.stdin:
        (ip, day, somethingelse) = lineas.split()
        if ip != ip_pre:
            if not primera_linea:
                print "{0}\t{1}\t{2}".format(ip_pre, day_pre, numclicks)
            else:
                primera_linea = False
            numclicks = 1
            ip_pre = ip
            day_pre = day
        else:
            if day != day_pre:
                print "{0}\t{1}\t{2}".format(ip_pre, day_pre, numclicks)
                numclicks = 1
                day_pre = day
            else:
                numclicks += 1
