
def talent_tree(level,build):
        defense = [self.all_defense(0.5),self.all_attack(0.5),self.all_attack(0.5),self.all_attack(0.5),...
                   self.increase_counterattack(0.5),self.increase_counterattack(0.5),self.increase_counterattack(0.5),...
                   self.all_attack(0.5),self.reduce_skill_damage_taken(3),self.reduce_skill_damage_taken(3),self.reduce_skill_damage_taken(3),...
                   self.reduce_damage_taken(0.5),self.reduce_damage_taken(0.5),self.reduce_damage_taken(0.5),...
                   self.all_attack(0.5),self.all_attack(0.5),self.all_health(0.5),self.all_health(0.5),self.all_health(0.5),...
                   self.heal_slightly_wounded(100),self.heal_slightly_wounded(100),self.heal_slightly_wounded(100),..
                   self.all_defense(0.5),self.all_defense(0.5),self.all_defense(0.5),...
                   self.defense_star(0.5),self.defense_star(0.5),self.defense_star(0.5),self.all_health(0.5),...
                   self.reduce_damage_taken_and_dealt(1,0.5),self.reduce_damage_taken_and_dealt(1,0.5),self.reduce_damage_taken_and_dealt(1,0.5),...
                   self.add_rage(2),self.add_rage(2),self.add_rage(2),self.march_speed(3),self.march_speed(3),...
                   self.all_defense(0.5),self.all_defense(0.5),self.all_defense(0.5),...
                   self.chance_reduce_damage_taken(5),self.chance_reduce_damage_taken(5),self.chance_reduce_damage_taken(5),...
                   self.thirty_percent_rage_accum(30,25),self.thirty_percent_rage_accum(30,25),self.thirty_percent_rage_accum(30,25),...
                   self.percent_rage_accum(30,25),self.thirty_percent_rage_accum(30,25)]
        
        infantry = [self.inf_defense(1),self.inf_defense(1),self.inf_defense(1),...
                    self.percent_all_defense(50,2),self.percent_all_defense(50,2),self.percent_all_defense(50,2),...
                    self.inf_health(1),self.inf_health(1),self.inf_health(2),self.inf_health(2),self.inf_health(2),...
                    self.normal_attack_damage(0.5),self.normal_attack_damage(0.5),self.normal_attack_damage(0.5),...
                    self.inf_defense(1),self.inf_defense(1),self.inf_defense(1),self.inf_health(1),self.inf_health(1),...
                    self.chance_inf_reduce_damage_taken(10,5,2),self.chance_inf_reduce_damage_taken(10,5,2),...
                    self.chance_inf_reduce_damage_taken(10,5,2),self.chance_inf_reduce_damage_taken(10,5,2),...
                    self.rage_accum(3),self.rage_accum(3),self.rage_accum(3),...
                    self.inf_attack(1),self.inf_attack(1),self.inf_attack_cav(1),self.inf_attack_cav(1),self.inf_attack_cav(1),...
                    self.march_inf_speed(3),self.march_inf_speed(3),self.march_inf_speed(3),self.march_inf_speed(3),...
                    self.march_inf_speed(2),self.march_inf_speed(2),self.march_inf_speed(2),self.inf_health(1),...
                    self.inf_attack(1),self.inf_attack(1),self.chance_reduce_march_speed(10,5,2),self.chance_reduce_march_speed(10,5,2),...
                    self.chance_reduce_march_speed(10,5,2),self.chance_reduce_march_speed(10,5,2),self.inf_all_buffs(0.5),...
                    self.inf_all_buffs(0.5),self.inf_all_buffs(0.5),self.inf_all_buffs(0.5),self.inf_all_buffs(0.5)]
        
        archer  = [self.arc_attack(1),self.arc_attack(1),self.arc_attack(1),self.reduced_to_all_attack(50,3),...
                   self.reduced_to_all_attack(50,3),self.reduced_to_all_attack(50,3),self.arc_attack(1),...
                   self.arc_attack(1),self.arc_attack(1),self.arc_attack(1),self.all_attack(0.5),...
                   self.all_attack(0.5),self.all_attack(0.5),self.arc_attack(1),self.arc_attack(1),self.arc_attack(1),...
                   self.arc_health(1),self.arc_health(1),self.chance_arc_only(10,50),self.chance_arc_only(10,50),...
                   self.chance_arc_only(10,50),self.chance_arc_only(10,50),self.march_speed(3),self.march_speed(3),...
                   self.arc_health(1),self.arc_health(1),self.arc_health(1),self.arch_on_inf_damage(3),...
                   self.arch_on_inf_damage(3),self.arch_on_inf_damage(3),self.arc_defense(1),self.rage_accum(3),...
                   self.rage_accum(3),self.rage_accum(3),self.march_speed(3),self.march_speed(3),self.march_speed(3),...
                   self.march_speed(3),self.arc_defense(1),self.primary_secondary_skill_damage(2),...
                   self.primary_secondary_skill_damage(2),self.primary_secondary_skill_damage(2),self.primary_secondary_skill_damage(2),...
                   self.chance_arc_only_turns(10,5,2),self.chance_arc_only_turns(10,5,2),self.chance_arc_only_turns(10,5,2),...
                   self.chance_arc_only_turns(10,5,2),self.chance_arc_only_turns(10,5,2)]
        
                    
        garrison = [self.all_defense(0.5),self.all_attack(0.5),self.all_attack(0.5),self.garrison_damage_dealt(2),...
                    self.garrison_damage_dealt(2),self.garrison_damage_dealt(2),self.all_health(0.5),...
                    self.garrison_skill_damage_reduction(5),self.garrison_skill_damage_reduction(5),self.garrison_skill_damage_reduction(5),...
                    self.garrison_damage_taken_reduced(2),self.garrison_damage_taken_reduced(2),self.garrison_damage_taken_reduced(2),...
                    self.all_defense(0.5),self.garrison_rage_accum(2),self.garrison_rage_accum(2),self.garrison_rage_accum(2),...
                    self.all_attack(0.5),self.all_attack(0.5),self.all_health(0.5),self.all_health(0.5),...
                    self.all_defense(0.5),self.all_defense(0.5),self.all_health(0.5),self.all_health(0.5),...
                    self.watchtower_defense(5),self.watchtower_defense(5),self.watchtower_defense(5),...
                    self.watchtower_attack(5),self.watchtower_attack(5),self.watchtower_attack(5),...
                    self.all_attack(0.5),self.all_attack(0.5),self.all_defense(0.5),self.all_defense(0.5),...
                    self.garrison_surround_damage_reduction(3),self.garrison_surround_damage_reduction(3),self.garrison_surround_damage_reduction(3),...
                    self.garrison_all_stats(1),self.garrison_all_stats(1),self.garrison_all_stats(1),...
                    self.chance_shield(10,100),self.chance_shield(10,100),self.chance_shield(10,100),self.chance_shield(10,100),...
                    self.chance_shield(10,100),self.march_speed(3),self.march_speed(3),self.march_speed(3)]
        
        skill  =  [self.all_attack(0.5),self.all_defense(0.5),self.all_defense(0.5),self.all_defense(0.5),...
                   self.reduce_skill_damage_taken(2),self.reduce_skill_damage_taken(2),self.reduce_skill_damage_taken(2),...
                   self.increase_skill(1),self.increase_skill(1),self.increase_skill(1),self.all_attack(0.5),...
                   self.all_health(0.5),self.all_health(0.5),self.increase_skill_increase_skill_taken(2,2),...
                   self.increase_skill_increase_skill_taken(2,2),self.increase_skill_increase_skill_taken(2,2),...
                   self.march_speed(3),self.march_speed(3),self.skill_damage_time(2,6),self.skill_damage_time(2,6),...
                   self.skill_damage_time(2,6),self.add_rage(3),self.add_rage(3),self.add_rage(3),self.all_defense(0.5),...
                   self.enhance_skill_damage(2),self.enhance_skill_damage(2),self.enhance_skill_damage(2),...
                   self.secondary_skill_increase(2),self.secondary_skill_increase(2),self.secondary_skill_increase(2),...
                   self.all_health(0.5),self.all_health(0.5),self.all_health(0.5),self.all_health(0.5),self.skill_used_rage_accum(20),...
                   self.skill_used_rage_accum(20),self.skill_used_rage_accum(20),self.all_defense(0.5),self.all_defense(0.5),...
                   self.all_attack(0.5),self.all_attack(0.5),self.all_attack(0.5),self.change_add_rage(10,20),...
                   self.change_add_rage(10,20),self.change_add_rage(10,20),self.change_add_rage(10,20),self.change_add_rage(10,20)]
        
        
