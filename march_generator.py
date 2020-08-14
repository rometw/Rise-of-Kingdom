


class March:
    def __init__(self,troop,primary,secondary=None):
        self.primary = primary
        self.set_active_skill_primary = primary.active_skills_use
        self.set_chance_skill_primary = primary.chance_skills_use
        if secondary == None:
            self.secondary = secondary
            self.set_active_skill_secondary = secondary.active_skills_use
            self.set_chance_skill_secondary = secondary.chance_skills_use
        else:
            print('Primary only')
            self.secondary = None
        self.initialize_buffs()
        self.troop = troop
        
        
        
        
    '''
    def pass_static_skills(self):
        skill += self.primary.skills
        boosted_skills += self.primary.boosted_skills
        if self.seconaary == None:
            skill += self.secondary.pass_static_skills
            boosted_skills += self.secondary.boosted_skills
        return skill,boosted_skills
    '''
       
    def pass_character_stats(self,stats):
        return
        
    
    def active_skills(self):
        return
       
    def march_stats(self,sklls,talents,character):
        return
    
    def name_of_comm(self):
        if self.secondary == None:
            return self.primary,self.secondary
        else:
            
            return self.primary

    def __delete__(self,march):
        del march
        
    def initialize_buffs(self):
        self.ia = 0
        self.id = 0
        self.ih = 0
        self.ca = 0
        self.cd = 0
        self.ch = 0
        self.aa = 0
        self.ad = 0
        self.ah = 0
        self.sa = 0
        self.sd = 0
        self.sh = 0
        self.buffs_ia = 0
        self.buffs_id = 0
        self.buffs_ih = 0
        self.buffs_ca = 0
        self.buffs_cd = 0
        self.buffs_ch = 0
        self.buffs_aa = 0
        self.buffs_ad = 0
        self.buffs_ah = 0
        self.buffs_sa = 0
        self.buffs_sd = 0
        self.buffs_sh = 0
        self.buffs_rally = 0
        self.buffs_skill = 0
        self.buffs_counter = 0
    
    def set_base_stats(self,character):
        self.ia = getattr(character,"ia")
        self.id = getattr(character,"id")
        self.ih = getattr(character,"ih")
        self.ca = getattr(character,"ca")
        self.cd = getattr(character,"cd")
        self.ch = getattr(character,"ch")
        self.aa = getattr(character,"aa")
        self.ad = getattr(character,"ad")
        self.ah = getattr(character,"ah")
        self.sa = getattr(character,"sa")
        self.sd = getattr(character,"sd")
        self.sh = getattr(character,"sh")

 

    def set_character_buffs(self,character):
    
        self.buffs_ia = getattr(character,"buffs_ia")
        self.buffs_id = getattr(character,"buffs_id")
        self.buffs_ih = getattr(character,"buffs_ih")
        self.buffs_ca = getattr(character,"buffs_ca")
        self.buffs_cd = getattr(character,"buffs_cd")
        self.buffs_ch = getattr(character,"buffs_ch")
        self.buffs_aa = getattr(character,"buffs_aa")
        self.buffs_ad = getattr(character,"buffs_ad")
        self.buffs_ah = getattr(character,"buffs_ah")
        self.buffs_sa = []
        self.buffs_sd = []
        self.buffs_sh = []
        self.buffs_rally = getattr(character,"buffs_rally")
        self.buffs_skill = getattr(character,"buffs_skill")
        self.buffs_counter = getattr(character,"buffs_counter")
    
    def add_comm_buffs(self,commander):
        buffs = getattr(commander,"skills")
        self.buffs_ia += buffs[0]
        self.buffs_id += buffs[1]
        self.buffs_ih += buffs[2]
        self.buffs_ca += buffs[3]
        self.buffs_cd += buffs[4]
        self.buffs_ch += buffs[5]
        self.buffs_aa += buffs[6]
        self.buffs_ad += buffs[7]
        self.buffs_ah += buffs[8]
        self.buffs_sa = buffs[9]
        self.buffs_sd = buffs[10]
        self.buffs_sh = buffs[11]
        self.buffs_rally += buffs[12]
        self.buffs_skill += buffs[13]
        self.buffs_counter += buffs[14]

    def add_comm_talents(self,commander):
        talents = getattr(commander,"talents")
        self.buffs_ia += talents[0]
        self.buffs_id += talents[1]
        self.buffs_ih += talents[2]
        self.buffs_ca += talents[3]
        self.buffs_cd += talents[4]
        self.buffs_ch += talents[5]
        self.buffs_aa += talents[6]
        self.buffs_ad += talents[7]
        self.buffs_ah += talents[8]
        self.buffs_sa = talents[9]
        self.buffs_sd = talents[10]
        self.buffs_sh = talents[11]
        self.buffs_rally += talents[12]
        self.buffs_skill += talents[13]
        self.buffs_counter += talents[14]

    def add_armor_buffs(self,commander):
        buffs = getattr(commander.equipment,"skills")
        self.buffs_ia += buffs[0]
        self.buffs_id += buffs[1]
        self.buffs_ih += buffs[2]
        self.buffs_ca += buffs[3]
        self.buffs_cd += buffs[4]
        self.buffs_ch += buffs[5]
        self.buffs_aa += buffs[6]
        self.buffs_ad += buffs[7]
        self.buffs_ah += buffs[8]
        self.buffs_sa = buffs[9]
        self.buffs_sd = buffs[10]
        self.buffs_sh = buffs[11]
        self.buffs_rally += buffs[12]
        self.buffs_skill += buffs[13]
        self.buffs_counter += buffs[14]

  
