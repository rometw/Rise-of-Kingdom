#!/usr/bin/env python
import random as rn

class talent_trees:
    def __init__(self,branch1,branch2,branch3):
        self.buffs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.damage_buffs = [0,0,0,0]
        self.normal_buffs = [0,0]
        self.skill_buffs = [0,0]
        self.tree1 = []
        self.tree2 = []
        self.tree3 = []
        self.branches = [branch1,branch2,branch3]
        return
        
    def make_talent_tree(self,build,tree):
        star = 6
        if "Defense" in self.branches:
            index = self.branches.index("Defense")
            def_build = build[index]
            
            #########################################
            #   Defense Tree Explanations           #
            #########################################
            #    1: Defense (All Troops) > Increases the defense of all units led by this commander by 0.5%
            #  2-4: Attack (All Troops) > Increases the attack of al units led by this commander by 0.5$%
            #  5-7: Spiked Armor > Increases counterattack damage dealt by 1.5%
            #    8: Attack (All Troops) > Increases the attack of al units led by this commander by 0.5$%
            # 9-11: Loose Formation > Reduces skill damage taken by 3%
            #12-14: No Weaknesses > Reduce damage taken by 0.5%
            #15-16: Attack (All Troops) > Increases the attack of al units led by this commander by 0.5$%
            #17-19: Health (All Troops) > Increases the health of al units led by this commander by 0.5$%
            #20-22: Medicinal Suppluies > After using a skill, heals a portion of slightly wounded units (Healing Factor 300)
            #23-25: Defense (All Troops) > Increases the defense of all units led by this commander by 0.5%
            #26-28: Master Armorer > When troops led by this commander enter battle, increases defense by (1.5 x Commander Star Level)%
            #   29: Health (All Troops) > Increases the health of al units led by this commander by 0.5$%
            #30-32: Balance > Reduces damage taken by 1% by also reduced damage dealth by 0.5%
            #33-35: Burning Blood > Grants an additional 6 rage every time this commander's troops are attacked
            #36-37: Increases the march speed of all units led by this commander by 3%
            #38-40: Defense (All Troops) > Increases the defense of all units led by this commander by 0.5%
            #41-43: Testudo Formation > Normal troop attacks have a 10% chance to reduce all damage taken by 15% during the next second
            #44-48: Desparate Elegy > When the army led by this commander has been reduced to 30% strength, greatly increases rage accumulation rate for the next 20 seconds. An additional 25 rage will be recovered from each attack
            
            defense = [self.all_defense(0.5,def_build[0]),self.all_attack(0.5,def_build[1]),self.all_attack(0.5,def_build[2]),self.all_attack(0.5,def_build[3]),\
                self.increase_counterattack(0.5,def_build[4]),self.increase_counterattack(0.5,def_build[5]),self.increase_counterattack(0.5,def_build[6]),\
                self.all_attack(0.5,def_build[7]),self.reduce_skill_damage_taken(3,def_build[8]),self.reduce_skill_damage_taken(3,def_build[9]),self.reduce_skill_damage_taken(3,def_build[10]),\
                self.reduce_damage_taken(0.5,def_build[11]),self.reduce_damage_taken(0.5,def_build[12]),self.reduce_damage_taken(0.5,def_build[13]),\
                self.all_attack(0.5,def_build[14]),self.all_attack(0.5,def_build[15]),self.all_health(0.5,def_build[16]),self.all_health(0.5,def_build[17]),self.all_health(0.5,def_build[18]),\
                self.heal_slightly_wounded(100,def_build[19]),self.heal_slightly_wounded(100,def_build[20]),self.heal_slightly_wounded(100,def_build[21]),\
                self.all_defense(0.5,def_build[22]),self.all_defense(0.5,def_build[23]),self.all_defense(0.5,def_build[24]),\
                self.defense_star(0.5,star,def_build[25]),self.defense_star(0.5,star,def_build[26]),self.defense_star(0.5,star,def_build[27]),self.all_health(0.5,def_build[28]),\
                self.reduce_damage_taken_and_dealt(1,0.5,def_build[29]),self.reduce_damage_taken_and_dealt(1,0.5,def_build[30]),self.reduce_damage_taken_and_dealt(1,0.5,def_build[31]),\
                self.add_rage(2,def_build[32]),self.add_rage(2,def_build[33]),self.add_rage(2,def_build[34]),self.march_speed(3,def_build[35]),self.march_speed(3,def_build[36]),\
                self.all_defense(0.5,def_build[37]),self.all_defense(0.5,def_build[38]),self.all_defense(0.5,def_build[39]),\
                self.chance_reduce_damage_taken(10,5,1,def_build[40]),self.chance_reduce_damage_taken(10,5,1,def_build[41]),self.chance_reduce_damage_taken(10,5,1,def_build[42]),\
                self.percent_rage_accum(30,25,20,def_build[43]),self.percent_rage_accum(30,25,20,def_build[44]),self.percent_rage_accum(30,25,20,def_build[45]),\
                self.percent_rage_accum(30,25,20,def_build[46]),self.percent_rage_accum(30,25,20,def_build[47])]
      
        if "Infantry" in self.branches:
            index = self.branches.index("Infantry")
            inf_build = build[index]
            #########################################
            #   Infantry Tree Explanations          #
            #########################################
            #    1: Defense (Infantry) > Increases defense of infantry units by 1%
            #  2-3: Defense (Infantry) > Increases defense of infantry units by 1%
            #  4-6: Call of the Pack > When the army led by this commander has been reduced to 50% strength, increases defense of all troops by 2%
            #  7-8: Health (Infantry) > Increases health of infantry units by 1%
            # 9-11: Strong of Body > Increases health of infantry units by 2%
            #12-14: Double-Headed Axe > Increases normal attack damage by 0.5%
            #15-16: Defense (Infantry) > Increases defense of infantry by 1%
            #   17: Defense (Infantry) > Increases defense of infantry by 1%
            #18-19: Health (Infantry) > Increases health of infantry units by 1%
            #20-23: Hold the Line > When army led by this commander contains only infantry units, gives troops a 10% chance to reduce damage taken by 5% for the next 2 seconds after being attacked
            #24-25: Attack (Infantry) > Increases attack of infantry units by 1%
            #26-28: Iron Spear > Infantry units led by this commander deal an additional 3% damage to cavalry units
            #29-31: Undying Fury > Normal attack grant an additional 3 rage
            #32-33: March Speed (Infantry) > Increases march speed of infantry units by 3%
            #34-35: March Speed (Infantry) > Increases march speed of infantry units by 3%
            #36-38: March Speed (Infantry) > Increases march speed of infantry units by 2%
            #   39: Health (Infantry) > Increases health of infantry units by 1%
            #40-41: Attack (Infantry) > Increases attack of infantry units by 1%
            #42-45: Snare of Thorns > Gives normal attacks a 10% chance to reduce target march speed by 5% for the next 2 seconds.
            #46-50: Elite Soldiers > When the army led by this commander contains only infantry units, attack, defense, and health are increased by 0.5%
            
            
            infantry = [self.inf_defense(1,inf_build[0]),self.inf_defense(1,inf_build[1]),self.inf_defense(1,inf_build[2]),\
                self.percent_all_defense(50,2,inf_build[3]),self.percent_all_defense(50,2,inf_build[4]),self.percent_all_defense(50,2,inf_build[5]),\
                self.inf_health(1,inf_build[6]),self.inf_health(1,inf_build[7]),self.inf_health(2,inf_build[8]),self.inf_health(2,inf_build[9]),self.inf_health(2,inf_build[10]),\
                self.normal_attack_damage(0.5,inf_build[11]),self.normal_attack_damage(0.5,inf_build[12]),self.normal_attack_damage(0.5,inf_build[13]),\
                self.inf_defense(1,inf_build[14]),self.inf_defense(1,inf_build[15]),self.inf_defense(1,inf_build[16]),self.inf_health(1,inf_build[17]),self.inf_health(1,inf_build[18]),\
                self.chance_inf_reduce_damage_taken(10,5,2,inf_build[19]),self.chance_inf_reduce_damage_taken(10,5,2,inf_build[20]),\
                self.chance_inf_reduce_damage_taken(10,5,2,inf_build[21]),self.chance_inf_reduce_damage_taken(10,5,2,inf_build[22]),\
                self.inf_attack(1,inf_build[23]),self.inf_attack(1,inf_build[24]),\
                self.add_rage(3,inf_build[25]),self.add_rage(3,inf_build[26]),self.add_rage(3,inf_build[27]),\
                self.inf_attack_cav(1,inf_build[28]),self.inf_attack_cav(1,inf_build[29]),self.inf_attack_cav(1,inf_build[30]),\
                self.march_inf_speed(3,inf_build[31]),self.march_inf_speed(3,inf_build[32]),self.march_inf_speed(3,inf_build[33]),self.march_inf_speed(3,inf_build[34]),\
                self.march_inf_speed(2,inf_build[35]),self.march_inf_speed(2,inf_build[36]),self.march_inf_speed(2,inf_build[37]),self.inf_health(1,inf_build[38]),\
                self.inf_attack(1,inf_build[39]),self.inf_attack(1,inf_build[40]),self.chance_reduce_march_speed(10,5,2,inf_build[41]),self.chance_reduce_march_speed(10,5,2,inf_build[42]),\
                self.chance_reduce_march_speed(10,5,2,inf_build[43]),self.chance_reduce_march_speed(10,5,2,inf_build[44]),self.inf_all_buffs(0.5,inf_build[45]),\
                self.inf_all_buffs(0.5,inf_build[46]),self.inf_all_buffs(0.5,inf_build[47]),self.inf_all_buffs(0.5,inf_build[48]),self.inf_all_buffs(0.5,inf_build[49])]
        
        else:
            return print('Found no tree by that name.  Please try: Infantry, Archer, Cavalry, Defense, Attack, Skill, Support, Leadership, Garrison, Conquering, Peacekeeping, Gathering')
        
        '''
        archer  = [self.arc_attack(1),self.arc_attack(1),self.arc_attack(1),self.reduced_to_all_attack(50,3),\
            self.reduced_to_all_attack(50,3),self.reduced_to_all_attack(50,3),self.arc_attack(1),\
            self.arc_attack(1),self.arc_attack(1),self.arc_attack(1),self.all_attack(0.5),\
            self.all_attack(0.5),self.all_attack(0.5),self.arc_attack(1),self.arc_attack(1),self.arc_attack(1),\
            self.arc_health(1),self.arc_health(1),self.chance_arc_only(10,50),self.chance_arc_only(10,50),\
            self.chance_arc_only(10,50),self.chance_arc_only(10,50),self.march_speed(3),self.march_speed(3),\
            self.arc_health(1),self.arc_health(1),self.arc_health(1),self.arch_on_inf_damage(3),\
            self.arch_on_inf_damage(3),self.arch_on_inf_damage(3),self.arc_defense(1),self.rage_accum(3),\
            self.rage_accum(3),self.rage_accum(3),self.march_speed(3),self.march_speed(3),self.march_speed(3),\
            self.march_speed(3),self.arc_defense(1),self.primary_secondary_skill_damage(2),\
            self.primary_secondary_skill_damage(2),self.primary_secondary_skill_damage(2),self.primary_secondary_skill_damage(2),\
            self.chance_arc_only_turns(10,5,2),self.chance_arc_only_turns(10,5,2),self.chance_arc_only_turns(10,5,2),\
            self.chance_arc_only_turns(10,5,2),self.chance_arc_only_turns(10,5,2)]


        garrison = [self.all_defense(0.5),self.all_attack(0.5),self.all_attack(0.5),self.garrison_damage_dealt(2),\
            self.garrison_damage_dealt(2),self.garrison_damage_dealt(2),self.all_health(0.5),\
            self.garrison_skill_damage_reduction(5),self.garrison_skill_damage_reduction(5),self.garrison_skill_damage_reduction(5),\
            self.garrison_damage_taken_reduced(2),self.garrison_damage_taken_reduced(2),self.garrison_damage_taken_reduced(2),\
            self.all_defense(0.5),self.garrison_rage_accum(2),self.garrison_rage_accum(2),self.garrison_rage_accum(2),\
            self.all_attack(0.5),self.all_attack(0.5),self.all_health(0.5),self.all_health(0.5),\
            self.all_defense(0.5),self.all_defense(0.5),self.all_health(0.5),self.all_health(0.5),\
            self.watchtower_defense(5),self.watchtower_defense(5),self.watchtower_defense(5),\
            self.watchtower_attack(5),self.watchtower_attack(5),self.watchtower_attack(5),\
            self.all_attack(0.5),self.all_attack(0.5),self.all_defense(0.5),self.all_defense(0.5),\
            self.garrison_surround_damage_reduction(3),self.garrison_surround_damage_reduction(3),self.garrison_surround_damage_reduction(3),\
            self.garrison_all_stats(1),self.garrison_all_stats(1),self.garrison_all_stats(1),\
            self.chance_shield(10,100),self.chance_shield(10,100),self.chance_shield(10,100),self.chance_shield(10,100),\
            self.chance_shield(10,100),self.march_speed(3),self.march_speed(3),self.march_speed(3)]

        skill  =  [self.all_attack(0.5),self.all_defense(0.5),self.all_defense(0.5),self.all_defense(0.5),\
            self.reduce_skill_damage_taken(2),self.reduce_skill_damage_taken(2),self.reduce_skill_damage_taken(2),\
            self.increase_skill(1),self.increase_skill(1),self.increase_skill(1),self.all_attack(0.5),\
            self.all_health(0.5),self.all_health(0.5),self.increase_skill_increase_skill_taken(2,2),\
            self.increase_skill_increase_skill_taken(2,2),self.increase_skill_increase_skill_taken(2,2),\
            self.march_speed(3),self.march_speed(3),self.skill_damage_time(2,6),self.skill_damage_time(2,6),\
            self.skill_damage_time(2,6),self.add_rage(3),self.add_rage(3),self.add_rage(3),self.all_defense(0.5),\
            self.enhance_skill_damage(2),self.enhance_skill_damage(2),self.enhance_skill_damage(2),\
            self.secondary_skill_increase(2),self.secondary_skill_increase(2),self.secondary_skill_increase(2),\
            self.all_health(0.5),self.all_health(0.5),self.all_health(0.5),self.all_health(0.5),self.skill_used_rage_accum(20),\
            self.skill_used_rage_accum(20),self.skill_used_rage_accum(20),self.all_defense(0.5),self.all_defense(0.5),\
            self.all_attack(0.5),self.all_attack(0.5),self.all_attack(0.5),self.change_add_rage(10,20),\
            self.change_add_rage(10,20),self.change_add_rage(10,20),self.change_add_rage(10,20),self.change_add_rage(10,20)]
        '''
            
       
        return self.buffs
        
    
    
 

    
    #Threshold talents
    def chance_inf_reduce_damage_taken(self,chance,percent,rounds,y=0, battle=0):
        num = int(100/chance)
        chance_var = rn.randrange(num)
        if (y == 1) & (battle == 1) & (chance_var == rn.randrange(num)):
            return #Still need to code how the chance stats occur
    
    def chance_reduce_march_speed(self,chance,percent,rounds,y=0,battle=0):
        num = int(100/chance)
        chance_var = rn.randrange(num)
        if (y == 1) & (battle == 1) & (chance_var == rn.randrange(num)):
            return #Still need to code how the chance stats occur
            
    def inf_all_buffs(self,percent,y=0):
        return #another difficult one, figure out
    
    def percent_all_defense(self,percent_lost,percent,y=0):
        return
        
    def inf_attack_cav(self,percent,y=0):
        if y == 1:
            return #need to figure out how to work this in
    
    
    #Pasive talents
    def normal_attack_damage(self,percent,y=0):
        if y == 1:
            self.normal_buffs[1] += percent
    
    def inf_attack(self,percent,y=0):
        if y == 1:
            self.buffs[0] += percent
    
    def inf_defense(self,percent,y=0):
        if y == 1:
            self.buffs[1] += percent
            
    def inf_health(self,percent,y=0):
        if y == 1:
            self.buffs[2] += percent

    def all_defense(self,percent = 0,y=0):
        if y == 1:
            self.buffs[1] += percent
            self.buffs[4] += percent
            self.buffs[7] += percent
            self.buffs[10] += percent
        
    
    def all_attack(self,percent=0,y=0):
        if y == 1:
            self.buffs[0] += percent
            self.buffs[3] += percent
            self.buffs[6] += percent
            self.buffs[9] += percent
        
    def all_health(self,percent=0,y=0):
        if y == 1:
            self.buffs[2] += percent
            self.buffs[5] += percent
            self.buffs[8] += percent
            self.buffs[11] += percent
    
    def increase_counterattack(self,percent=0,y=0):
        if y == 1:
            self.buffs[12] = percent
        
    
    def reduce_skill_damage_taken(self,percent=0,y=0):
        return
    
    def heal_slightly_wounded(self,factor=0,y=0):
        return
        
    def defense_star(self,star,percent=0,y=0):
        return
    
    def reduce_damage_taken(self,percent=0,y=0):
        return
    
    def reduce_damage_taken_and_dealt(self,percent_taken=0,percent_dealt=0,y=0):
        return
    
    def add_rage(self,amount=0,y=0):
        return
    
    def march_speed(self,percent=0,y=0):
        return
        
    def march_inf_speed(self,percent,y=0):
        return
        
    def chance_reduce_damage_taken(self,chance=0,percent=0,turns=0,y=0):
        return
    
    def percent_rage_accum(self,percent=0,rage=0,turns=0,y=0):
        return
    

