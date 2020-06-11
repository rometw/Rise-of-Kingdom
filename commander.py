#!/usr/bin/env python
from character_profile import Character
from talent_tree import talent_tree

class Richard:
    def __init__(self,skill,level,build):
        #Initiate Richard with input of skills
        self.skills = self.skill_build(skill)
        self.talents = talent_tree(level,build)
    
    def skill_build(skill):
        #Heal some of the slightly wounded troops (factor)
        skill1a = [600,800,1000,1200,1400]
        #Adds a debuff to a maximum of 5 targets in a fan-shaped area (Damage Reduction %) for 2 seconds
        skill1b = [10,15,20,25,30]
        #Adds a debuff to a maximum of 5 targets in a fan-shaped area (March Sepeed Reduction %) for 2 seconds
        skill1c = [5,7,9,12,15]
        
        #Increase trop damage reduction
        skill2a = [5,7,9,12,15]
        #Increase counterattack damage
        skill2b = [4,5,6,8,10]
        
        #Increases the attack of infantry
        skill3a = [5,7,9,12,15]
        #Increases the defense of infantry
        skill3b = [5,7,9,12,15]
        
        #Increases healing effects received by troops
        skill4a = [10,15,20,25,30]
        #Reduces watchtower damage taken
        skill4b = [10,15,20,25,30]
        
        if [5,5,5,5] = skill:
            #Reduces all damage taken %
            expertise_a = 5
            #Increase damage done to cav units %
            expertise_b = 2
            #Decreases target march every 10 seconds for 5 seconds
            expertise_c = 50
        
    
    
    def attack(self):
        self.skills()
        self.talents()
        return
        
class March:
    def __init__(self,primary,secondary,troop):
        self.primary = primary
        self.secondary = secondary
        self.troop = troop
            
    
    


