#!/usr/bin/env python

class equipment:
    def __init__(self):
        self.helm = []
        self.weapon = []
        self.chest = []
        self.gloves = []
        self.legs = []
        self.boots = []
        self.accessory = []
        self.set = []
        self.buffs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def set_equipment(self,type,name,expertise):
        ##############################################################
        #                                                            #
        # function takes in type and name and assigns buff stats     #
        # Currently for version 10003414_113937:p1928004:17603256    #
        ##############################################################
        if type == 'Helm':
            if name == 'Iron Helm':
                self.buffs[0] += 3
                self.helm = name
            
            elif name == 'Mast of the Forest Guardian':
                self.buffs[0] += 4
                self.buffs[9] += 4
                self.helm = name
            
            elif name == 'Abyssal Visage':
                self.buffs[0] += 3
                self.buffs[3] += 4
                self.buffs[6] += 3
                self.helm = name
            
            elif name == 'Revival Helm':
                self.buffs[1] += 5
                self.buffs[7] += 5
                self.helm = name
            
            elif name == 'Harvesters Headscarf':
                self.buffs[9] += 3
                self.buffs[10] += 3
                self.helm = name
            
            elif name == 'Expedition War Helm':
                self.buffs[1] += 2
                self.buffs[4] += 4
                self.helm = name
            
            elif name == 'Helm of the Phoenix':
                self.buffs[2] += 2
                self.buffs[7] += 2
                self.helm = name
            
            elif name == 'Helm of Fear':
                self.buffs[3] += 2
                self.buffs[1] += 2
                self.helm = name
            
            else:
                print('You did not choose a correct Helm.  Try again.')
            
            
        elif type == 'Weapon':
            if name == 'Sharp Longsword':
                self.buffs[4] += 5
                self.weapon = name
            
            elif name == 'Trial of the Lost Kingdom':
                self.buffs[4] += 10
                self.buffs[2] += 5
                self.buffs[6] += 5
                self.weapon = name
            
            elif name == 'Golden Age':
                self.buffs[3] += 4
                self.buffs[1] += 6
                self.buffs[7] += 8
                self.weapon = name
            
            elif name == 'Scepter of the Forest Guardian':
                self.buffs[3] += 6
                self.buffs[10] += 6
                self.weapon = name
            
            elif name == 'Heart of the Saint':
                self.buffs[4] += 8
                self.buffs[2] += 4
                self.buffs[8] += 6
                self.weapon = name
            
            elif name == 'Staff of the Lost':
                self.buffs[4] += 3
                self.buffs[1] += 5
                self.buffs[7] += 5
                self.weapon = name
            
            elif name == 'Gatekeepers Shield':
                self.buffs[5] += 5
                self.buffs[2] += 5
                self.weapon = name
            
            elif name == 'Vanguard Halberd':
                self.buffs[4] += 5
                self.buffs[5] += 4
                self.weapon = name
            
            elif name == 'Blessed Blade':
                self.buffs[2] += 4
                self.buffs[6] += 4
                self.weapon = name
            
            else:
                print('You did not choose a correct Weapon.  Try again.')
        
        elif type == 'Chest':
            if name == 'Chain Mail':
                self.buffs[6] += 3
                self.chest = name
            
            elif name == 'Shadow Legions Retribution':
                self.buffs[3] += 5
                self.buffs[0] += 5
                self.buffs[6] += 5
                self.chest = name
            
            elif name == 'The Milky Way':
                self.buffs[5] += 6
                self.buffs[8] += 6
                self.chest = name
            
            elif name == 'Quinns Soul':
                self.buffs[0] += 4
                self.buffs[8] += 4
                self.chest = name
            
            elif name == 'Robe of the Forest Guardian':
                self.buffs[6] += 4
                self.buffs[9] += 4
                self.chest = name
            
            elif name == 'Revival Plate':
                self.buffs[4] += 5
                self.buffs[6] += 5
                self.chest = name
            
            elif name == 'Dark Lord Blessing':
                self.buffs[4] += 5
                self.buffs[6] += 5
                self.chest = name
            
            elif name == 'Harvester Robes':
                self.buffs[10] += 3
                self.buffs[11] += 3
                self.chest = name
            
            elif name == 'Commanders Heavy Armor':
                self.buffs[0] += 3
                self.buffs[8] += 3
                self.chest = name
            
            elif name == 'Infantry Breastplate':
                self.buffs[5] += 2
                self.buffs[1] += 2
                self.chest = name
            
            elif name == 'Milanese Plate':
                self.buffs[4] += 3
                self.buffs[6] += 2
                self.chest = name
            
            else:
                print('You did not choose a correct chest.  Try again.')
        
        elif type == 'Gloves':
            if name == 'Cloth Gloves':
                self.buffs[1] += 2
                self.gloves = name
            
            elif name == 'Ians Choice':
                self.buffs[6] += 8
                self.gloves = name
            
            elif name == 'Sacred Grips':
                self.buffs[1] += 5
                self.buffs[6] += 5
                self.gloves = name
            
            elif name == 'Seths Brutality':
                self.buffs[1] += 2
                self.buffs[7] += 2
                self.gloves = name
            
            elif name == 'Isets Sufferance':
                self.buffs[3] += 3
                self.buffs[5] += 3
                self.gloves = name
            
            elif name == 'Claws of the Forest Guardian':
                self.buffs[9] += 2
                self.buffs[10] += 2
                self.gloves = name
            
            elif name == 'Revival Guantlets':
                self.buffs[3] += 3
                self.buffs[0] += 3
                self.gloves = name
            
            elif name == 'Windswept Bracers':
                self.buffs[5] += 2
                self.buffs[2] += 1
                self.gloves = name
            
            elif name == 'Saints Song':
                self.buffs[3] += 2
                self.buffs[6] += 1
                self.gloves = name
            
            elif name == 'Leather Gloves':
                self.buffs[1] += 1
                self.buffs[8] += 2
                self.gloves = name
            
            else:
                print('You did not choose correct Gloves.  Try again.')
        
        elif type == 'Legs':
            if name == 'Coarse Breeches':
                self.buffs[3] += 3
                self.legs = name
            
            elif name == 'Eternal Night':
                self.buffs[4] += 5
                self.buffs[1] += 5
                self.buffs[7] += 5
                self.legs = name
            
            elif name == 'Ash of the Dawn':
                self.buffs[5] += 5
                self.buffs[2] += 5
                self.legs = name
            
            elif name == 'Gladiator':
                self.buffs[5] += 4
                self.buffs[7] += 4
                self.legs = name
            
            elif name == 'Karuaks Humility':
                self.buffs[3] += 5
                self.buffs[2] += 5
                self.legs = name
            
            elif name == 'Greaves of the Exile':
                self.buffs[1] += 3
                self.buffs[7] += 3
                self.legs = name
            
            elif name == 'Harvester Breeches':
                self.buffs[9] += 3
                self.buffs[10] += 3
                self.legs = name
            
            elif name == 'Ranger Trousers':
                self.buffs[0] += 2
                self.buffs[7] += 2
                self.legs = name
            
            elif name == 'Vanguard Greaves':
                self.buffs[3] += 4
                self.buffs[5] += 1
                self.legs = name
            
            else:
                print('You did not choose correct Legs.  Try again.')
        
        elif type == 'Boots':
            if name == 'Edged Boots':
                self.buffs[3] += 1
                self.buffs[6] += 1
                self.boots = name
            
            elif name == 'Boots of Reverence':
                self.buffs[0] += 2
                self.buffs[7] += 1
                self.boots = name
            
            elif name == 'Sturdy Boots':
                self.buffs[7] += 2
                self.boots = name
            
            elif name == 'Shios Return':
                self.buffs[8] += 5
                self.buffs[1] += 5
                self.boots = name
            
            elif name == 'Cloud Racers':
                self.buffs[3] += 2
                self.buffs[8] += 2
                self.boots = name
            
            elif name == 'Windswept Boots':
                self.buffs[5] += 2
                self.buffs[1] += 1
                self.boots = name
            
            elif name == 'Harvester Boots':
                self.buffs[10] += 2
                self.buffs[11] += 2
                self.boots = name
            
            else:
                print('You did not choose correct Boots.  Try again.')
            
        
        elif type == 'Accessory':
            if name == 'Scolas Lucky Coin':
                #need to program
                self.accessory = name
            
            elif name == 'Pendant of Eternal Night':
                self.buffs[12] += 5
            
            elif name == 'Delanes Amulet':
                #need to program
                self.accessory = name
            
            elif name == 'Silent Trial':
                #need to program
                self.accessory = name
            
            elif name == 'Savage Totem':
                self.accessory = name
            
            elif name == 'Lohars Bone Necklace':
                self.accessory = name
            
            else:
                print('You did not choose a correct Helm.  Try again.')
        
        else:
            print('You did not choose a correct type.  Try again.')
        
        self.is_set()
        
    def is_set(self):
        if (self.helm == 'Revival Helm') & (self.chest == 'Revival Plate') | (self.gloves == 'Revival Gauntlets'):
            self.buffs[0,3,6,9] += 2
            
        elif (self.helm == 'Revival Helm') | (self.chest == 'Revival Plate') & (self.gloves == 'Revival Gauntlets'):
            self.buffs[0,3,6,9] += 2
            
        elif (self.helm == 'Revival Helm') & (self.chest == 'Revival Gauntlets') | (self.gloves == 'Revival Plate'):
            self.buffs[0,3,6,9] += 2
        
        if (self.gloves == 'Windswept Bracers') & (self.boots == 'Windswept Boots'):
            self.buffs[0,3,6,9] += 2
        
        if (self.weapon == 'Vanguard Halberd') & (self.legs == 'Vanguard Greaves'):
            self.buffs[3] += 2
        
