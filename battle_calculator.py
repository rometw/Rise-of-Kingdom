#!/usr/bin/env python
import random as rn
import numpy as np
from report_template import Report

class Battle:
    def __init__(self, march1,march2):
        self.march1 = march1
        self.march2 = march2
        self.report = Report(self)
        #Place a method here for placing all of the buffs
        self.begin()
        self.report.close_file()
  
        #Need something about chance stats
    
    
    def begin(self):

        while (self.march1.troop > 0) & (self.march2.troop > 0):
            check = self.turn()
            if check == 0:
                print('March 1 is dead.  Go home!')
                self.report.close_file()
            if check == 1:
                print('March 2 is dead.  Go home!')
                self.report.close_file()
            if check == 2:
                print('March 1 and 2 are dead.  Go home!')
                self.report.close_file()
            if check == 3:
                pass
                #print(self.march1.troop,self.march2.troop)
            
    
    def turn(self):
        loss1 = rn.randint(800,1000) #This is where the algorithm will go
        loss2 = rn.randint(800,1000) #This is where the algorithm will go
        
        if (self.march1.troop - loss1 < 0) & (self.march2.troop - loss2 < 0):
            self.march1.troop = 0
            self.march2.troop = 0
            self.report.write_lines([self.march1.troop,self.march2.troop])
            return 2
        elif (self.march1.troop - loss1 < 0):
            self.march1.troop = 0
            self.report.write_lines([self.march1.troop,self.march2.troop])
            return 0
        elif (self.march2.troop - loss2 < 0):
            self.march2.troop = 0
            self.report.write_lines([self.march1.troop,self.march2.troop])
            return 1
        else:
            self.march1.troop -= loss1
            self.march2.troop -= loss2
            self.report.write_lines([self.march1.troop,self.march2.troop])
            return 3
