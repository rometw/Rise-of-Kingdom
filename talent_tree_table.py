#!/usr/bin/env python

class talent_trees:
    def __init__(self):
        self.buffs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return
        
    def make_talent_tree(self,level,build):
        y = [0]*48
        for i in range(level):
            y[i] = 1
        
        defense = [self.all_defense(0.5,y[0]),self.all_attack(0.5,y[1]),self.all_attack(0.5,y[2]),self.all_attack(0.5,y[3]),\
            self.increase_counterattack(0.5,y[4]),self.increase_counterattack(0.5,y[5]),self.increase_counterattack(0.5,y[6]),\
            self.all_attack(0.5,y[7]),self.reduce_skill_damage_taken(3,y[8]),self.reduce_skill_damage_taken(3,y[9]),self.reduce_skill_damage_taken(3,y[10]),\
            self.reduce_damage_taken(0.5,y[11]),self.reduce_damage_taken(0.5,y[12]),self.reduce_damage_taken(0.5,y[13]),\
            self.all_attack(0.5,y[14]),self.all_attack(0.5,y[15]),self.all_health(0.5,y[16]),self.all_health(0.5,y[17]),self.all_health(0.5,y[18]),\
            self.heal_slightly_wounded(100,y[19]),self.heal_slightly_wounded(100,y[20]),self.heal_slightly_wounded(100,y[21]),\
            self.all_defense(0.5,y[22]),self.all_defense(0.5,y[23]),self.all_defense(0.5,y[24]),\
            self.defense_star(0.5,level,y[25]),self.defense_star(0.5,level,y[26]),self.defense_star(0.5,level,y[27]),self.all_health(0.5,y[28]),\
            self.reduce_damage_taken_and_dealt(1,0.5,y[29]),self.reduce_damage_taken_and_dealt(1,0.5,y[30]),self.reduce_damage_taken_and_dealt(1,0.5,y[31]),\
            self.add_rage(2,y[32]),self.add_rage(2,y[33]),self.add_rage(2,y[34]),self.march_speed(3,y[35]),self.march_speed(3,y[36]),\
            self.all_defense(0.5,y[37]),self.all_defense(0.5,y[38]),self.all_defense(0.5,y[39]),\
            self.chance_reduce_damage_taken(10,5,1,y[40]),self.chance_reduce_damage_taken(10,5,1,y[41]),self.chance_reduce_damage_taken(10,5,1,y[42]),\
            self.percent_rage_accum(30,25,20,y[43]),self.percent_rage_accum(30,25,20,y[44]),self.percent_rage_accum(30,25,20,y[45]),\
            self.percent_rage_accum(30,25,20,y[46]),self.percent_rage_accum(30,25,20,y[47])]
      
        '''
        infantry = [self.inf_defense(1),self.inf_defense(1),self.inf_defense(1),\
            self.percent_all_defense(50,2),self.percent_all_defense(50,2),self.percent_all_defense(50,2),\
            self.inf_health(1),self.inf_health(1),self.inf_health(2),self.inf_health(2),self.inf_health(2),\
            self.normal_attack_damage(0.5),self.normal_attack_damage(0.5),self.normal_attack_damage(0.5),\
            self.inf_defense(1),self.inf_defense(1),self.inf_defense(1),self.inf_health(1),self.inf_health(1),\
            self.chance_inf_reduce_damage_taken(10,5,2),self.chance_inf_reduce_damage_taken(10,5,2),\
            self.chance_inf_reduce_damage_taken(10,5,2),self.chance_inf_reduce_damage_taken(10,5,2),\
            self.rage_accum(3),self.rage_accum(3),self.rage_accum(3),\
            self.inf_attack(1),self.inf_attack(1),self.inf_attack_cav(1),self.inf_attack_cav(1),self.inf_attack_cav(1),\
            self.march_inf_speed(3),self.march_inf_speed(3),self.march_inf_speed(3),self.march_inf_speed(3),\
            self.march_inf_speed(2),self.march_inf_speed(2),self.march_inf_speed(2),self.inf_health(1),\
            self.inf_attack(1),self.inf_attack(1),self.chance_reduce_march_speed(10,5,2),self.chance_reduce_march_speed(10,5,2),\
            self.chance_reduce_march_speed(10,5,2),self.chance_reduce_march_speed(10,5,2),self.inf_all_buffs(0.5),\
            self.inf_all_buffs(0.5),self.inf_all_buffs(0.5),self.inf_all_buffs(0.5),self.inf_all_buffs(0.5)]

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
        if build == "Defensive Inf":
            return self.buffs
            
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
        
    def defense_star(self,percent=0,level=0,y=0):
        return
    
    def reduce_damage_taken(self,percent=0,y=0):
        return
    
    def reduce_damage_taken_and_dealt(self,percent_taken=0,percent_dealt=0,y=0):
        return
    
    def add_rage(self,amount=0,y=0):
        return
    
    def march_speed(self,percent=0,y=0):
        return
        
    def chance_reduce_damage_taken(self,chance=0,percent=0,turns=0,y=0):
        return
    
    def percent_rage_accum(self,percent=0,rage=0,turns=0,y=0):
        return
    

