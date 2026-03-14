from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from .Options import EndGoal
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import THAWWorld


def set_all_rules(world: THAWWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    #set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: "THAWWorld"):
    player = world.player
    options = world.options

    # Hollywood Missions
    add_rule(world.multiworld.get_location("HW Mission: Learn to Caveman", player),
             lambda state: state.has("Skate Ability: Caveman", player))
    add_rule(world.multiworld.get_location("HW Mission: Do a Sponsor Challenge", player),
             lambda state: state.has("Skate Ability: Caveman", player))
    add_rule(world.multiworld.get_location("HW Mission: Kickflip Whofleck", player),
             lambda state: state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Caveman", player))
    add_rule(world.multiworld.get_location("HW Mission: Learn to Revert", player),
             lambda state: state.has("Skate Ability: Revert", player) and state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Caveman", player))
    add_rule(world.multiworld.get_location("HW Mission: Get Your Stuff Back", player),
             lambda state: state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Revert", player) and state.has("Skate Ability: Caveman", player))
    add_rule(world.multiworld.get_location("HW Mission: Get Into Beverly Hills", player),
             lambda state: state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Revert", player) and state.has("Skate Ability: Caveman", player))

    # Hollywood Gaps
    add_rule(world.multiworld.get_location("HW Gap: El Teniente Spine", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
    add_rule(world.multiworld.get_location("HW Gap: Pin Plant", player),
             lambda state: state.has("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", player))
    add_rule(world.multiworld.get_location("HW Gap: Planter Pop", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
    add_rule(world.multiworld.get_location("HW Gap: Romperwood Spine", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))            
    add_rule(world.multiworld.get_location("HW Gap: Tony to Tony", player),
             lambda state: state.has("Skate Ability: Manual", player))
    add_rule(world.multiworld.get_location("HW Gap: Voodoo Spine", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
    add_rule(world.multiworld.get_location("HW Gap: Spinner", player),
             lambda state: state.has("Skate Ability: Wall Run", player))
    add_rule(world.multiworld.get_location("HW Gap: El Teniente Drop", player),
             lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
    add_rule(world.multiworld.get_location("HW Gap: Romper Rail", player),
             lambda state: state.has("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", player))
    add_rule(world.multiworld.get_location("HW Gap: FireEscape Level4", player),
             lambda state: state.has_all(("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Caveman", "Skate Ability: Wall Run"), player))
    add_rule(world.multiworld.get_location("HW Gap: Goat Whackin'", player),
             lambda state: state.has("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", player))
    add_rule(world.multiworld.get_location("HW Gap: FireEscape Level5", player),
             lambda state: state.has_all(("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Caveman", "Skate Ability: Wall Run"), player) and state.has("Progressive Speed Stat", world.player, 3))
    add_rule(world.multiworld.get_location("HW Gap: Hollywood High Line", player),
             lambda state: state.has_all(("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Manual"), player) and state.has("Progressive Speed Stat", world.player, 1) and state.has("Progressive Ollie Stat", world.player, 4))

    # Victory Goal Stuff
    if options.end_goal == EndGoal.option_smash_the_t_rex:
        add_rule(world.multiworld.get_location("Smash the T-Rex", player),
                 lambda state: state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Revert", player) and state.has("Skate Ability: Caveman", player))

def set_completion_condition(world: THAWWorld) -> None:
    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)