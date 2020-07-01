#!/usr/bin/env python
from character_profile import Character
import commander
import march_generator

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
    build_Richard = [1,0,0,0]
    build_Charles = [1,0,0,0]
    star = 1
    tech = [70,70,40,70,70,40,70,70,40]
    alliance_tech = [15,15,0,15,15,0,15,15,0]
    titles = [0,0,0,0,0,0,0,0,0]
    holy_sites = [6,6,5,6,6,5,6,6,5]
    building = [2,2,6,2,2,6,2,2,6]
    vip = 15
    troop_amount = 200000
    level = 10



    kevin = Character('Ottoman')
    kevin.city_theme_buffs('No Place Like Home')
    kevin.change_civ('Germany')
    rich = commander.Richard()
    rich.skill_build(build_Richard)
    rich.build_talent_tree(level,"Defensive Inf")
    #march1 = march_generator.March(troop_amount,rich)
    kevin.launch_field_march(troop_amount,rich)
    #print(march1.primary,march1.primary.print_talent_tree())
    
    
    
    

    

   
    

if __name__ == "__main__":
    main()
