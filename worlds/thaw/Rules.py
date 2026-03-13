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


#def set_all_entrance_rules(world: THAWWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    #overworld_to_bottom_right_room = world.get_entrance("Overworld to Bottom Right Room")
    #overworld_to_top_left_room = world.get_entrance("Overworld to Top Left Room")
    #right_room_to_final_boss_room = world.get_entrance("Right Room to Final Boss Room")

    # An access rule is a function. We can define this function like any other function.
    # This function must accept exactly one parameter: A "CollectionState".
    # A CollectionState describes the current progress of the players in the multiworld, i.e. what items they have,
    # which regions they've reached, etc.
    # In an access rule, we can ask whether the player has a collected a certain item.
    # We can do this via the state.has(...) function.
    # This function takes an item name, a player number, and an optional count parameter (more on that below)
    # Since a rule only takes a CollectionState parameter, but we also need the player number in the state.has call,
    # our function needs to be locally defined so that it has access to the player number from the outer scope.
    # In our case, we are inside a function that has access to the "world" parameter, so we can use world.player.
    #def can_destroy_bush(state: CollectionState) -> bool:
    #    return state.has("Sword", world.player)

    # Now we can set our "can_destroy_bush" rule to our entrance which requires slashing a bush to clear the path.
    # One way to set rules is via the set_rule() function, which works on both Entrances and Locations.
    #set_rule(overworld_to_bottom_right_room, can_destroy_bush)

    # Because the function has to be defined locally, most worlds prefer the lambda syntax.
    #set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))

    # Conditions can depend on event items.
    #set_rule(right_room_to_final_boss_room, lambda state: state.has("Top Left Room Button Pressed", world.player))

    # Some entrance rules may only apply if the player enabled certain options.
    # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    # Overworld to the Top Middle Room.
    #if world.options.hammer:
    #    overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
    #    set_rule(overworld_to_top_middle_room, lambda state: state.has("Hammer", world.player))


def set_all_location_rules(world: "THAWWorld"):
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
    if options.end_goal == EndGoal.option_smash_the_t_rex:
        add_rule(world.multiworld.get_location("Smash the T-Rex", player),
                 lambda state: state.has("Skate Ability: Manual") and state.has("Skate Ability: Revert") and state.has("Skate Ability: Caveman"))

def set_completion_condition(world: THAWWorld) -> None:
    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)