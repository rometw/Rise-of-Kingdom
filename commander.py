#!/usr/bin/env python
from character_profile import Character
from talent_tree_table import talent_trees
from equipment_table import equipment

#Buffs are sent in list in the following form:
#[ia,id,ih,ca,cd,ch,aa,ad,ah,sa,sd,sh,skill,rally,counter]
#Damage buffs are done in the following:,
#[all damage taken (enemy stats) buff/debuff, seconds, all damage given (own stats) buff/debuff, seconds]  If 0, its for all turns

class Richard:
    def __init__(self,skill):
        if skill:
            #Initiate Richard with input of skills
            self.skills = []#self.skill_build(skill)
            self.asl = skill[0]#level of active skill
            self.active_skills = []#actice skill build
            self.damage_skills = []
            self.heal_buffs = []
            self.skill_damage = [] #Not sure how this is being used, may be eliminated
            self.chance_skills = []
            self.talents = []
            self.passive_skill_build(skill)
            self.chance_skills_build(skill)
            self.active_skills_build(skill)
            self.name = 'Richard'
            self.equipment = equipment()
            
        
    def chance_skills_build(self,skill):
        return   #have no figured out how to do this
        #########################################################################
        #   Chance stats
        #########################################################################
        
    def chance_skills_use(self,skill):
         return  #have no figured out how to do this
         #########################################################################
         #   Chance stats
         #########################################################################
    
        
    def active_skills_use(self,slightly):
        
        heal = 0 #need to figure out how to calculate factor for healing
        if heal > slightly:
            heal = slightly
        return heal
        #Before we do this, we need to figure out how it will be passed
        #Need to access algorithm to determine how many of the slightly wounded will be healed
        #Need to somehow calculate how debuffs are utilized
        
        
    def active_skills_build(self,skill):
        #########################################################
        # Still need to figure out how to pass the active skill #
        #########################################################
        skill = [i-1 for i in skill] #done for indexing
        a_skill_buffs = [0,0,0]
        #Heal some of the slightly wounded troops (factor)
        skill1a = [600,800,1000,1200,1400]
        a_skill_buffs[0] = skill1a[skill[0]]
        #Adds a debuff to a maximum of 5 targets in a fan-shaped area (Damage Reduction %) for 2 seconds
        skill1b = [-10,-15,-20,-25,-30]
        a_skill_buffs[1] += skill1b[skill[0]]
        a_skill_buffs[2] = 2
        #Adds a debuff to a maximum of 5 targets in a fan-shaped area (March Sepeed Reduction %) for 2 seconds
        skill1c = [5,7,9,12,15] #not yet coded, seems irrelevant atm
        
        self.active_skills = a_skill_buffs
    
    def passive_skill_build(self,skill):
        buffs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        all_damage_buffs = [0,0,0,0]
        heal = [0]
        skill_dmg = [0]
        watch_buff = [0]
        skill_damage = [0] #not sure how this is getting used, may be eliminated
        
        skill = [i-1 for i in skill]
        #Increase troop damage reduction (damage taken reduction)
        skill2a = [5,7,9,12,15]
        all_damage_buffs[0] += skill2a[skill[1]]
        all_damage_buffs[1] = 0 #Not sure what I am doing here
        #Increase counterattack damage
        skill2b = [4,5,6,8,10]
        buffs[14] += skill2b[skill[1]]
        
        #Increases the attack of infantry
        skill3a = [5,7,9,12,15]
        buffs[0] += skill3a[skill[2]]
        #Increases the defense of infantry
        skill3b = [5,7,9,12,15]
        buffs[1] += skill3a[skill[2]]
        
        #Increases healing effects received by troops
        skill4a = [10,15,20,25,30]
        heal[0] += skill4a[skill[3]]
        
        #Reduces watchtower damage taken
        skill4b = [10,15,20,25,30]
        watch_buff[0] += skill4b[skill[3]]
        
        if [5,5,5,5] == skill:
            print('Richard is expertised')
            #Reduces all damage taken %
            #expertise_a = 5
            all_damage_buffs[0] += 5
            #Increase damage done to cav units %
            #####this seems like a difficult one to build, come back to it#####
            expertise_b = 2
            #Decreases target march every 10 seconds for 5 seconds
            expertise_c = 50
        
        self.skills = buffs
        self.damage_skills = all_damage_buffs
        self.heal_buffs = heal
        self.skill_damage = skill_damage

    def build_talent_tree(self,build,tree):
        talent_tree = talent_trees("Defense","Infantry","Garrison")
        self.talents = talent_tree.make_talent_tree(build,tree)
        print(self.talents,'this is the talent tree')
        
    def print_talent_tree(self):
        print(self.talents)
        
    def equip(self,type,name,expertise):
        self.equipment.set_equipment(type,name,expertise)
    
    def print_name(self):
        return 'Richard'
    
    
        

            
    
    


