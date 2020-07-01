#!/usr/bin/env python
from character_profile import Character
from talent_tree_table import talent_trees

#Buffs are sent in list in the following form:
#[ia,id,ih,ca,cd,ch,aa,ad,ah,sa,sd,sh,skill,rally,counter]
#Boosted buffs are done in the following:,
#[all damage taken (enemy stats) buff/debuff, seconds, all damage given (own stats) buff/debuff, seconds]  If 0, its for all turns

class Richard:
    def __init__(self):
        #Initiate Richard with input of skills
        self.skills = []#self.skill_build(skill)
        self.a_skill_buffs = []
        self.boosted_skills = []
        self.heal = []
        self.skill_damage = []
    
    def skill_build(self,skill):
        buffs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        a_skill_buffs = [0,0,0]
        boosted_buffs = [0,0,0,0]
        heal = [0]
        skill_dmg = [0]
        watch_buff = [0]
        skill_damage = [0]
        
        #########################################################
        # Still need to figure out how to pass the active skill #
        #########################################################
        #Heal some of the slightly wounded troops (factor)
        skill1a = [600,800,1000,1200,1400]
        a_skill_buffs[0] = skill1a[skill[0]]
        #Adds a debuff to a maximum of 5 targets in a fan-shaped area (Damage Reduction %) for 2 seconds
        skill1b = [-10,-15,-20,-25,-30]
        a_skill_buffs[1] += skill1b[skill[0]]
        a_skill_buffs[2] = 2
        #Adds a debuff to a maximum of 5 targets in a fan-shaped area (March Sepeed Reduction %) for 2 seconds
        skill1c = [5,7,9,12,15] #not yet coded, seems irrelevant atm
        
        
        
        #Increase troop damage reduction (damage taken reduction)
        skill2a = [5,7,9,12,15]
        boosted_buffs[0] += skill2a[skill[1]]
        boosted_buffs[1] = 0
        #Increase counterattack damage
        skill2b = [4,5,6,8,10]
        buffs[14] = skill2b[skill[1]]
        
        #Increases the attack of infantry
        skill3a = [5,7,9,12,15]
        buffs[0] = skill3a[skill[2]]
        #Increases the defense of infantry
        skill3b = [5,7,9,12,15]
        buffs[1] = skill3a[skill[2]]
        
        #Increases healing effects received by troops
        skill4a = [10,15,20,25,30]
        heal[0] = skill4a[skill[3]]
        
        #Reduces watchtower damage taken
        skill4b = [10,15,20,25,30]
        watch_buff[0] = skill4b[skill[3]]
        
        if [5,5,5,5] == skill:
            #Reduces all damage taken %
            #expertise_a = 5
            boosted_buffs[0] += 5
            #Increase damage done to cav units %
            #####this seems like a difficult one to build, come back to it#####
            expertise_b = 2
            #Decreases target march every 10 seconds for 5 seconds
            expertise_c = 50
        
        self.skills = buffs
        self.boosted_skills = boosted_buffs
        self.active_skills = a_skill_buffs
        self.heal = heal
        self.skill_damage = skill_damage

    def build_talent_tree(self,level,build):
        talent_tree = talent_trees()
        self.talents = talent_tree.make_talent_tree(level,build)
        print(self.talents,'this is the talent tree')
        
    def print_talent_tree(self):
        print(self.talents)
    
    def attack(self):
        self.skills()
        self.talents()
        return
        

            
    
    


