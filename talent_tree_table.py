#!/usr/bin/env python

class talent_trees:
    def __init__(self):
        return
        
    def make_talent_tree(self,level,build):
        defense = [self.all_defense(0.5),self.all_attack(0.5),self.all_attack(0.5),self.all_attack(0.5),\
            self.increase_counterattack(0.5),self.increase_counterattack(0.5),self.increase_counterattack(0.5),\
            self.all_attack(0.5),self.reduce_skill_damage_taken(3),self.reduce_skill_damage_taken(3),self.reduce_skill_damage_taken(3),\
            self.reduce_damage_taken(0.5),self.reduce_damage_taken(0.5),self.reduce_damage_taken(0.5),\
            self.all_attack(0.5),self.all_attack(0.5),self.all_health(0.5),self.all_health(0.5),self.all_health(0.5),\
            self.heal_slightly_wounded(100),self.heal_slightly_wounded(100),self.heal_slightly_wounded(100),\
            self.all_defense(0.5),self.all_defense(0.5),self.all_defense(0.5),\
            self.defense_star(0.5,level),self.defense_star(0.5,level),self.defense_star(0.5,level),self.all_health(0.5),\
            self.reduce_damage_taken_and_dealt(1,0.5),self.reduce_damage_taken_and_dealt(1,0.5),self.reduce_damage_taken_and_dealt(1,0.5),\
            self.add_rage(2),self.add_rage(2),self.add_rage(2),self.march_speed(3),self.march_speed(3),\
            self.all_defense(0.5),self.all_defense(0.5),self.all_defense(0.5),\
            self.chance_reduce_damage_taken(10,5,1),self.chance_reduce_damage_taken(10,5,1),self.chance_reduce_damage_taken(10,5,1),\
            self.percent_rage_accum(30,25,20),self.percent_rage_accum(30,25,20),self.percent_rage_accum(30,25,20),\
            self.percent_rage_accum(30,25,20),self.percent_rage_accum(30,25,20)]
        print(defense)
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
            print(defense[0:level-1])
            return defense[0:level-1]
            
    def all_defense(self,percent):
        return 
    
    def all_attack(self,percent):
        return
        
    def all_health(self,percent):
        return
    
    def increase_counterattack(self,percent):
        return
    
    def reduce_skill_damage_taken(self,percent):
        return
    
    def heal_slightly_wounded(self,factor):
        return
        
    def defense_star(self,percent,level):
        return
    
    def reduce_damage_taken(self,percent):
        return
    
    def reduce_damage_taken_and_dealt(self,percent_taken,percent_dealt):
        return
    
    def add_rage(self,amount):
        return
    
    def march_speed(self,percent):
        return
        
    def chance_reduce_damage_taken(self,chance,percent,turns):
        return
    
    def percent_rage_accum(self,percent,rage,turns):
        return
    

