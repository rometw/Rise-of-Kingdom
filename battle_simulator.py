#!/usr/bin/env python
from character_profile import Character
import commander
import march_generator
import battle_calculator

#########################################################################
#########################################################################
#                   RISE OF KINGDOM BATTLE SIMULATOR                    #
#########################################################################
#   Created: May 28, 2020                                               #
#   Modified: June 10, 2020                                             #
#   Programming by:  Kevin Haghi (Die Zweihaender)                      #
#   Battle Kernel written by: Kevin Haghi and Kouen (Coconyan)          #
#                                                                       #
#                                                                       #
#   This is the main file for simualating battles that occur            #
#   in the game "Rise of Kingdom" by Lilith.  The code is               #
#   capable of setting base stats and buffs, building marches,          #
#   and simulating the battle between two marches.  This is             #
#   based on the website:                                               #
#   https://everythingrok.com/uncovering-the-combat-formula/#comments   #
#   and empirical evidence gathered in game.  This code is not intended #
#   for reproduction.                                                   #
#########################################################################

def main():
    primary = 'Richard'
    secondary = 'Charles'
    build_Richard = [5,5,5,5]
    build_Charles = [1,0,0,0]
    star = 1
    tech = [70,70,40,70,70,40,70,70,40]
    alliance_tech = [15,15,0,15,15,0,15,15,0]
    titles = [0,0,0,0,0,0,0,0,0]
    holy_sites = [6,6,5,6,6,5,6,6,5]
    building = [2,2,6,2,2,6,2,2,6]
    vip = 15
    troop_amount = 200000
    defense_build = [1]*50
    infantry_build = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    garrison_build = [0]
    talent_tree = [defense_build,infantry_build,garrison_build]



###Character Kevin
    kevin = Character('Germany')
    kevin.city_theme_buffs('No Place Like Home')
    kevinrich = commander.Richard(build_Richard)
    kevinrich.build_talent_tree(talent_tree,1)
    #rich.build_talent_tree(infantry_build,"Infantry")
    #march1 = march_generator.March(troop_amount,rich)
    kevin.launch_field_march(troop_amount,kevinrich)
    
    print(kevin.march1)
    #kevin.return_field_march(kevin.march1[1])

#### Character Coco
    coco = Character('Ottoman')
    coco.city_theme_buffs('No Place Like Home')
    cocorich = commander.Richard(build_Richard)
    cocorich.build_talent_tree(talent_tree,1)
    coco.launch_field_march(troop_amount,cocorich)
    
    
    rich_rich_battle = battle_calculator.Battle(kevin.march1[0],coco.march1[0])
    
    

    

   
    

if __name__ == "__main__":
    main()
