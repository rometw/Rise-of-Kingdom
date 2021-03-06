#!/usr/bin/env python
from base_stats_table import set_base_stats
from city_themes import set_city_buffs
from vip_table import set_vip_buffs
from civilization_table import set_civ_buffs
from march_generator import March

#Buffs are sent in list in the following form:
#[ia,id,ih,ca,cd,ch,aa,ad,ah,sa,sd,sh,skill,rally,counter]

class Character:
    def __init__(self,civ):
        #Initiate a character and their base stats
        self.attack_buffs([])
        self.defense_buffs([])
        self.health_buffs([])
        self.rally_buffs([])
        self.skill_buffs([])
        self.counter_buffs([])
        self.civilization(civ)
        self.skin = ''
        self.title = ''
        self.march_count = 0

        
    def launch_field_march(self,troop_count,primary,*secondary):
        #self.march_count+=1
        march = March(troop_count,primary,secondary)
        march.set_base_stats(self)
        march.set_character_buffs(self)
        march.add_comm_buffs(primary)
        march.add_comm_talents(primary)
        if secondary:
            march.add_buffs(secondary)
        
        if not hasattr(self,'march1'):
            self.march1 = [march,1]
            print('March launched as March 1.  reference self.march1[0] for object')
        elif not hasattr(self,'march2'):
            self.march2 = [march,2]
            print('March launched as March 2.  reference self.march2[0] for object')
        elif not hasattr(self,'march3'):
            self.march3 = [march,3]
            print('March launched as March 3.  reference self.march3[0] for object')
        elif not hasattr(self,'march4'):
            self.march4 = [march,4]
            print('March launched as March 4.  reference self.march4[0] for object')
        elif not hasattr(self,'march5'):
            self.march5 = [march,5]
            print('March launched as March 5.  reference self.march5[0] for object')
        else:
            print('Only allowed 5 marches in the field, return a march[0] for object')
            return []
        
    
    def return_field_march(self,march_num):
        if march_num == 1:
            print('Commander(s) ',self.march1[0].name_of_comm(), 'with ', self.march1[0].troop,' troops has returned.')
            delattr(self,'march1')
        elif march_num == 2:
            print('Commander(s) ',self.march2[0].primary, 'with ', self.march1[0].troop,' troops has returned.')
            delattr(self,'march2')
        elif march_num == 3:
            print('Commander(s) ',self.march3[0].primary, 'with ', self.march1[0].troop,' troops has returned.')
            delattr(self,'march3')
        elif march_num == 4:
            print('Commander(s) ',self.march4[0].primary, 'with ', self.march1[0].troop,' troops has returned.')
            delattr(self,'march4')
        elif march_num == 5:
            print('Commander(s) ',self.march5[0].primary, 'with ', self.march1[0].troop,' troops has returned.')
            delattr(self,'march5')
        else:
            print('This march does not belong to this character')
        return
        
    
        
    def city_theme_buffs(self,skin):
        self.skin = skin
        buffs = set_city_buffs(skin)
        self.defense_buffs([buffs[1],buffs[4],buffs[7]])
        self.attack_buffs([buffs[0],buffs[3],buffs[6]])
        self.health_buffs([buffs[2],buffs[5],buffs[8]])
        self.rally_buffs(buffs[13])
        self.skill_buffs(buffs[12])
        
    def technology_buffs(self,tech):
        self.defense_buffs([tech[1],tech[4],tech[7]])
        self.attack_buffs([tech[0],tech[3],tech[6]])
        self.health_buffs([tech[2],tech[5],tech[8]])

    def alliance_buffs(self,tech):
        self.defense_buffs([tech[1],tech[4],tech[7]])
        self.attack_buffs([tech[0],tech[3],tech[6]])
        self.health_buffs([tech[2],tech[5],tech[8]])
        
    def holy_sites_buffs(self,holy):
        self.defense_buffs([holy[1],holy[4],holy[7]])
        self.attack_buffs([holy[0],holy[3],holy[6]])
        self.health_buffs([holy[2],holy[5],holy[8]])

    def titles(self,title):
        self.title = title
        self.defense_buffs([title[1],title[4],title[7]])
        self.attack_buffs([title[0],title[3],title[6]])
        self.health_buffs([title[2],title[5],title[8]])

    def building_buffs(self,build):
        self.defense_buffs([build[1],build[4],build[7]])
        self.attack_buffs([build[0],build[3],build[6]])
        self.health_buffs([build[2],build[5],build[8]])
        
    def vip_buffs(self,vip):
        buffs = set_vip_buffs(vip)
        self.defense_buffs([buffs[1],buffs[4],buffs[7]])
        self.attack_buffs([buffs[0],buffs[3],buffs[6]])
        self.health_buffs([buffs[2],buffs[5],buffs[8]])
        self.rally_buffs(buffs[13])
        self.skill_buffs(buffs[12])
        self.counter_buffs(buffs[14])
        
    def change_civ(self,civ):
        buffs = set_civ_buffs(self.civ)
        remove_buffs = [i * -1 for i in buffs]
        self.defense_buffs([remove_buffs[1],remove_buffs[4],remove_buffs[7]])
        self.attack_buffs([remove_buffs[0],remove_buffs[3],remove_buffs[6]])
        self.health_buffs([remove_buffs[2],remove_buffs[5],remove_buffs[8]])
        self.rally_buffs(remove_buffs[13])
        self.skill_buffs(remove_buffs[12])
        self.civilization(civ)
        
    def civilization(self,civ):
        buffs = set_civ_buffs(civ)
        base = set_base_stats(civ)
        self.base_stats(base)
        self.civ = civ
        self.defense_buffs([buffs[1],buffs[4],buffs[7]])
        self.attack_buffs([buffs[0],buffs[3],buffs[6]])
        self.health_buffs([buffs[2],buffs[5],buffs[8]])
        self.rally_buffs(buffs[13])
        self.skill_buffs(buffs[12])
        
        
    def base_stats(self,stats):
        #Base stats for character
        self.ia = stats[0]
        self.id = stats[1]
        self.ih = stats[2]
        self.ca = stats[3]
        self.cd = stats[4]
        self.ch = stats[5]
        self.aa = stats[6]
        self.ad = stats[7]
        self.ah = stats[8]
        self.sa = stats[9]
        self.sd = stats[10]
        self.sh = stats[11]
        
    def attack_buffs(self,buffs):
        if buffs == []:
            self.buffs_ia = 0
            self.buffs_ca = 0
            self.buffs_aa = 0
        else:
            self.buffs_ia += buffs[0]
            self.buffs_ca += buffs[1]
            self.buffs_aa += buffs[2]

    def defense_buffs(self,buffs):
        if buffs == []:
            self.buffs_id = 0
            self.buffs_cd = 0
            self.buffs_ad = 0
        else:
            self.buffs_id += buffs[0]
            self.buffs_cd += buffs[1]
            self.buffs_ad += buffs[2]

    def health_buffs(self,buffs):
        if buffs == []:
            self.buffs_ih = 0
            self.buffs_ch = 0
            self.buffs_ah = 0
        else:
            self.buffs_ih += buffs[0]
            self.buffs_ch += buffs[1]
            self.buffs_ah += buffs[2]

    def rally_buffs(self,buffs):
        if buffs == []:
            self.buffs_rally = 0
        else:
            self.buffs_rally += buffs
            
    def skill_buffs(self,buffs):
        if buffs == []:
            self.buffs_skill = 0
        else:
            self.buffs_skill += buffs

    def counter_buffs(self,buffs):
        if buffs == []:
            self.buffs_counter = 0
        else:
            self.buffs_counter += buffs
    

