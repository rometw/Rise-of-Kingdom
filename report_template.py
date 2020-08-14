#!/usr/bin/env python
import datetime

class Report:
    def __init__(self,battle):
        self.file = open('/Users/kevin/Desktop/Rise-of-Kingdom/battle_reports/Battle Report: {date:%d-%m-%Y_%H:%M:%S}.csv'.format( date=datetime.datetime.now()),'w')
        
    def write_lines(self,data):
        for listitem in data:
            if listitem == data[-1]:
                self.file.write('%s\n, ' %listitem)
            else:
                self.file.write('%s, ' %listitem)
    
    def close_file(self):
        self.file.close()

