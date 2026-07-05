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

    add_rule(world.get_entrance("Hollywood -> Hollywood Shops"),
                lambda state: state.has(("40 Bucks"), player))
    # Hollywood Stage 1 Missions
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
    add_rule(world.multiworld.get_location("HW Gap: Manual the Stars", player),
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
    
    if options.end_goal == EndGoal.option_get_to_the_skate_ranch:    
        add_rule(world.get_entrance("Hollywood -> Beverly Hills"),
                lambda state: state.has("Bus Access: Beverly Hills", player) or state.has_all(("Skate Ability: Caveman", "Skate Ability: Manual", "Skate Ability: Revert"), player))
        add_rule(world.get_entrance("Beverly Hills -> Skate Ranch"),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player))
        # Beverly Hills Stage 1 Missions
        add_rule(world.multiworld.get_location("BH Mission: Learn the Natas Spin", player),
                lambda state: state.has("Skate Ability: Natas Spin", player))
        add_rule(world.multiworld.get_location("BH Mission: Learn Parkour tricks", player),
                lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck"), player))
        add_rule(world.multiworld.get_location("BH Mission: Learn Spines, Flips, Rolls, Acid Drops, Banks", player),
                lambda state: state.has_all(("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls"), player))
        add_rule(world.multiworld.get_location("BH Mission: Learn the Boneless and Boned Ollie", player),
                lambda state: state.has(("Skate Ability: Boneless", "Skate Ability: Boned Ollie"), player))
        add_rule(world.multiworld.get_location("BH Mission: Learn some wall tricks", player),
                lambda state: state.has(("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride"), player))
        add_rule(world.multiworld.get_location("BH Mission: Impress Murphy", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride"), player))
        add_rule(world.multiworld.get_location("BH Mission: Impress Boone", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride"), player))
        add_rule(world.multiworld.get_location("BH Mission: Impress Dave", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player))
        add_rule(world.multiworld.get_location("BH Mission: Second Tagging Mission", player),
                lambda state: state.has_all(("Skate Ability: Wall Ride", "Skate Ability: Caveman"), player))
        add_rule(world.multiworld.get_location("BH Mission: Third Tagging Mission", player),
                lambda state: state.has_all(("Skate Ability: Wall Ride", "Skate Ability: Caveman"), player))
        add_rule(world.multiworld.get_location("BH Mission: Fourth Tagging Mission", player),
                lambda state: state.has_all(("Skate Ability: Wall Ride", "Skate Ability: Caveman"), player))
        add_rule(world.multiworld.get_location("BH Mission: Fifth Tagging Mission", player),
                lambda state: state.has_all(("Skate Ability: Wall Ride", "Skate Ability: Caveman"), player))
        
        # Beverly Hills Stage 1 Gaps
        add_rule(world.multiworld.get_location("BH Gap: Rail 2 QP", player),
                lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
        add_rule(world.multiworld.get_location("BH Gap: Ramp 2 wire", player),
                lambda state: state.has("Progressive Speed Stat", player, 2))
        add_rule(world.multiworld.get_location("BH Gap: Across the street", player),
                lambda state: state.has_all_counts({"Progressive Speed Stat":7, "Progressive Ollie Stat":3}, player))
        add_rule(world.multiworld.get_location("BH Gap: Roof 2 roof", player),
                lambda state: state.has_all("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
        add_rule(world.multiworld.get_location("BH Gap: Qp 2 wire hop", player),
                lambda state: state.has_all_counts({"Progressive Speed Stat":5, "Progressive Ollie Stat":3}, player))
        add_rule(world.multiworld.get_location("BH Gap: Got wings?", player),
                lambda state: state.has_all_counts({"Progressive Speed Stat":5, "Progressive Ollie Stat":5}, player))
        add_rule(world.multiworld.get_location("BH Gap: Nice manual", player),
                lambda state: state.has("Skate Ability: Manual", player))
        add_rule(world.multiworld.get_location("BH Gap: Sweet stairset", player),
                lambda state: state.has_all_counts({"Progressive Speed Stat":6, "Progressive Ollie Stat":3}, player) and state.has("Skate Ability: Boneless", player))
        add_rule(world.multiworld.get_location("BH Gap: Wall 2 wire", player),
                lambda state: state.has("Skate Ability: Wall Ride", player))

    # Victory Goal Stuff
    if options.end_goal == EndGoal.option_smash_the_t_rex:
        add_rule(world.multiworld.get_location("Smash the T-Rex", player),
                lambda state: state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Revert", player) and state.has("Skate Ability: Caveman", player))
    if options.end_goal == EndGoal.option_get_to_the_skate_ranch:
        add_rule(world.multiworld.get_location("Get to the Skate Ranch", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player))

def set_completion_condition(world: THAWWorld) -> None:
    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)