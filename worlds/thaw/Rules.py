from worlds.generic.Rules import add_rule
from typing import TYPE_CHECKING
from .Items import victory_condition

if TYPE_CHECKING:
    from . import THAWWorld

# This is the last big thing to do (at least for me)
# This is where you add item
# These are omega simplified rules
# There are a ton of different ways you can add rules from amount of items you need to optional items
# Theres also difficulty options and a bunch others
# Id suggest going through a bunch of different ap worlds and seeing how they do the rules
# Even better if its a game you know a lot about and can tell what you need to get to certain locations
def set_rules(world: "THAWWorld"):
    player = world.player
    options = world.options

    # Hollywood Missions
    add_rule(world.multiworld.get_location("HW Mission: Learn to Caveman", player),
             lambda state: state.has("Skate Ability: Caveman"))
    add_rule(world.multiworld.get_location("HW Mission: Do a Sponsor Challenge", player),
             lambda state: state.has("Skate Ability: Caveman"))
    add_rule(world.multiworld.get_location("HW Mission: Kickflip Whofleck", player),
             lambda state: state.has("Skate Ability: Manual") and state.has("Skate Ability: Caveman"))
    add_rule(world.multiworld.get_location("HW Mission: Learn to Revert", player),
             lambda state: state.has("Skate Ability: Revert") and state.has("Skate Ability: Manual") and state.has("Skate Ability: Caveman"))
    add_rule(world.multiworld.get_location("HW Mission: Get Your Stuff Back", player),
             lambda state: state.has("Skate Ability: Manual") and state.has("Skate Ability: Revert") and state.has("Skate Ability: Caveman"))
    add_rule(world.multiworld.get_location("HW Mission: Get Into Beverly Hills", player),
             lambda state: state.has("Skate Ability: Manual") and state.has("Skate Ability: Revert") and state.has("Skate Ability: Caveman")) 

    # Hollywood Gaps
    add_rule(world.multiworld.get_location("", player),
             lambda state: state.has(""))  
    add_rule(world.multiworld.get_location("HW Gap: El Teniente Spine", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop"))
    add_rule(world.multiworld.get_location("HW Gap: Pin Plant", player),
             lambda state: state.has("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant"))
    add_rule(world.multiworld.get_location("HW Gap: Planter Pop", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop"))
    add_rule(world.multiworld.get_location("HW Gap: Romperwood Spine", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop"))            
    add_rule(world.multiworld.get_location("HW Gap: Tony to Tony", player),
             lambda state: state.has("Skate Ability: Manual"))
    add_rule(world.multiworld.get_location("HW Gap: Voodoo Spine", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop"))
    add_rule(world.multiworld.get_location("HW Gap: Spinner", player),
             lambda state: state.has("Skate Ability: Wall Run"))
    add_rule(world.multiworld.get_location("HW Gap: El Teniente Drop", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop"))
    add_rule(world.multiworld.get_location("HW Gap: Romper Rail", player),
             lambda state: state.has("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant"))
    add_rule(world.multiworld.get_location("HW Gap: FireEscape Level4", player),
             lambda state: state.has_all("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Caveman", "Skate Ability: Wall Run"))
    add_rule(world.multiworld.get_location("HW Gap: Goat Whackin'", player),
             lambda state: state.has_all("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant"))
    add_rule(world.multiworld.get_location("HW Gap: FireEscape Level5", player),
             lambda state: state.has_all("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Caveman", "Skate Ability: Wall Run") and state.has("Progressive Speed Stat", world.player, 3))
    add_rule(world.multiworld.get_location("HW Gap: Hollywood High Line", player),
             lambda state: state.has_all("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Manual") and state.has("Progressive Speed Stat", world.player, 1) and state.has("Progressive Ollie Stat", world.player, 4)) 

    # Victory Goal Stuff
    if victory_condition == "Smash the T-rex":
        add_rule(world.multiworld.get_location("Smash the T-Rex", player),
                 lambda state: state.has("Skate Ability: Manual") and state.has("Skate Ability: Revert") and state.has("Skate Ability: Caveman"))
    
    # Victory condition rule!
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)