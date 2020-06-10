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
            
    
    

primary = 'Richard'
secondary = 'Charles'
build_Richard = [1,0,0,0]
build_Charles = [1,0,0,0]
tech = [70,70,40,70,70,40,70,70,40]
alliance_tech = [15,15,0,15,15,0,15,15,0]
titles = [0,0,0,0,0,0,0,0,0]
holy_sites = [6,6,5,6,6,5,6,6,5]
building = [2,2,6,2,2,6,2,2,6]
vip = 15
troop_amount = 200000



kevin = Character('Ottoman')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
#kevin.civilization('Germany')
#print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.city_theme_buffs('No Place Like Home')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.technology_buffs(tech)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.alliance_buffs(alliance_tech)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.alliance_buffs(holy_sites)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.building_buffs(building)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.vip_buffs(vip)
print(kevin.aa,kevin.ad,kevin.ah,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
print(kevin.buffs_ia,kevin.buffs_id,kevin.buffs_ih,kevin.buffs_ca,kevin.buffs_cd,kevin.buffs_ch,kevin.buffs_aa,kevin.buffs_ad,kevin.buffs_ah,kevin.buffs_skill,kevin.buffs_rally,kevin.buffs_counter)
kevin.change_civ('Germany')
print(kevin.aa,kevin.ad,kevin.ah,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
print(kevin.buffs_ia,kevin.buffs_id,kevin.buffs_ih,kevin.buffs_ca,kevin.buffs_cd,kevin.buffs_ch,kevin.buffs_aa,kevin.buffs_ad,kevin.buffs_ah,kevin.buffs_skill,kevin.buffs_rally,kevin.buffs_counter)
