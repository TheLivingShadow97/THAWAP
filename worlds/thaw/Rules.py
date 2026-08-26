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

    def can_beverlyhills(state: CollectionState) -> bool:
        if options.include_skateboard_in_item_pool==False:
            return state.has("Bus Access: Beverly Hills", player) or state.has_all(("Skate Ability: Caveman", "Skate Ability: Manual", "Skate Ability: Revert"), player)
        if options.include_skateboard_in_item_pool==True:
                    return state.has("Bus Access: Beverly Hills", player) or state.has_all(("Skate Ability: Caveman", "Skate Ability: Manual", "Skate Ability: Revert", "Skateboard Unlock"), player)
    def can_skateranch(state: CollectionState) -> bool:
        return state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player)
    def can_downtown(state: CollectionState) -> bool:
        if options.progressive_wallet==False:
            return state.has("Bus Access: Downtown", player) or state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual", "Skate Ability: Skitch", "Skate Ability: Bert Slide",), player)
        if options.progressive_wallet==True:
            return state.has("Bus Access: Downtown", player) or (state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual", "Skate Ability: Skitch", "Skate Ability: Bert Slide",), player) and state.has("Progressive Wallet", player, 7))
    def can_skateranch_stage2(state: CollectionState) -> bool:
            if options.progressive_wallet==False:
                return state.has_all(("Skate Ability: Skitch", "Skate Ability: Bert Slide",), player)
            if options.progressive_wallet==True:
                return (state.has_all_counts({"Skate Ability: Skitch":1, "Skate Ability: Bert Slide":1, "Progressive Wallet":7}, player))
    def can_vanspark(state: CollectionState) -> bool:
        return state.has_all(("Skate Ability: Stall", "Skate Ability: Special", "Skate Ability: Focus"), player)
    def can_skateranch_piece_missions(state: CollectionState) -> bool:
        if options.progressive_wallet==False:
            return state.has_all(("Skate Ability: Skitch", "Skate Ability: Bert Slide",), player)
        if options.progressive_wallet==True:
            return (state.has_all_counts({"Progressive Speed Stat":3, "Skate Ability: Stall":1,"Progressive Wallet":7}, player))

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
    
    #Shops
    if options.progressive_wallet == True:
        #Hollywood
        add_rule(world.get_entrance("Hollywood Shops -> Hollywood Shops $10"),
                lambda state: state.has("Progressive Wallet", player, 1))
        add_rule(world.get_entrance("Hollywood Shops -> Hollywood Shops $20"),
                lambda state: state.has("Progressive Wallet", player, 2))
        add_rule(world.get_entrance("Hollywood Shops -> Hollywood Shops $30"),
                lambda state: state.has("Progressive Wallet", player, 3))
        add_rule(world.get_entrance("Hollywood Shops -> Hollywood Shops $50"),
                lambda state: state.has("Progressive Wallet", player, 4))
        add_rule(world.get_entrance("Hollywood Shops -> Hollywood Shops $100"),
                lambda state: state.has("Progressive Wallet", player, 5))
        #Beverly Hills
        add_rule(world.get_entrance("Beverly Hills Shops -> Beverly Hills Shops $10"),
                lambda state: state.has("Progressive Wallet", player, 1))
        add_rule(world.get_entrance("Beverly Hills Shops -> Beverly Hills Shops $20"),
                lambda state: state.has("Progressive Wallet", player, 2))
        add_rule(world.get_entrance("Beverly Hills Shops -> Beverly Hills Shops $30"),
                lambda state: state.has("Progressive Wallet", player, 3))
        add_rule(world.get_entrance("Beverly Hills Shops -> Beverly Hills Shops $50"),
                lambda state: state.has("Progressive Wallet", player, 4))
        add_rule(world.get_entrance("Beverly Hills Shops -> Beverly Hills Shops $100"),
                lambda state: state.has("Progressive Wallet", player, 5))
        add_rule(world.get_entrance("Beverly Hills Shops -> Beverly Hills Shops $1250"),
                lambda state: state.has("Progressive Wallet", player, 8))
        #Downtown
        add_rule(world.get_entrance("Downtown Shops -> Downtown Shops $10"),
                lambda state: state.has("Progressive Wallet", player, 1))
        add_rule(world.get_entrance("Downtown Shops -> Downtown Shops $20"),
                lambda state: state.has("Progressive Wallet", player, 2))
        add_rule(world.get_entrance("Downtown Shops -> Downtown Shops $30"),
                lambda state: state.has("Progressive Wallet", player, 3))
        add_rule(world.get_entrance("Downtown Shops -> Downtown Shops $50"),
                lambda state: state.has("Progressive Wallet", player, 4))
        add_rule(world.get_entrance("Downtown Shops -> Downtown Shops $100"),
                lambda state: state.has("Progressive Wallet", player, 5))

    #if options.shop_keys==True:
    #    add_rule(world.get_entrance("Beverly Hills -> Beverly Hills Shops"),
    #        lambda state: state.has("Beverly Hills Shops Key", player, 1))
    #    add_rule(world.get_entrance("Downtown -> Downtown Shops"),
    #        lambda state: state.has("Downtown Shops Key", player, 1))

    if options.include_skateboard_in_item_pool==True:
        add_rule(world.get_entrance("Hollywood No Skateboard Needed -> Hollywood"),
                         lambda state: state.has("Skateboard Unlock", player, 1))
        add_rule(world.get_entrance("Beverly Hills No Skateboard Needed -> Beverly Hills"),
                                 lambda state: state.has("Skateboard Unlock", player, 1))
        add_rule(world.get_entrance("Downtown No Skateboard Needed -> Downtown"),
                                 lambda state: state.has("Skateboard Unlock", player, 1))
        add_rule(world.get_entrance("Santa Monica No Skateboard Needed -> Santa Monica"),
                                         lambda state: state.has("Skateboard Unlock", player, 1))
        add_rule(world.get_entrance("East LA No Skateboard Needed -> East LA"),
                                         lambda state: state.has("Skateboard Unlock", player, 1))
    
    if options.end_goal >= EndGoal.option_get_to_the_skate_ranch:    
        set_rule(world.get_entrance("Hollywood No Skateboard Needed -> Beverly Hills No Skateboard Needed"), can_beverlyhills)
        set_rule(world.get_entrance("Beverly Hills -> Skate Ranch"), can_skateranch)
        #add_rule(world.get_entrance("Hollywood -> Beverly Hills"),
        #        lambda state: state.has("Bus Access: Beverly Hills", player) or state.has_all(("Skate Ability: Caveman", "Skate Ability: Manual", "Skate Ability: Revert"), player))
        #add_rule(world.get_entrance("Beverly Hills -> Skate Ranch"),
        #        lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player))
        
        # Beverly Hills Stage 1 Missions
        add_rule(world.multiworld.get_location("BH Mission: Learn the Natas Spin", player),
                lambda state: state.has("Skate Ability: Natas Spin", player))
        add_rule(world.multiworld.get_location("BH Mission: Learn Parkour tricks", player),
                lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck"), player))
        add_rule(world.multiworld.get_location("BH Mission: Learn Spines, Flips, Rolls, Acid Drops, Banks", player),
                lambda state: state.has_all(("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls"), player))
        add_rule(world.multiworld.get_location("BH Mission: Learn the Boneless and Boned Ollie", player),
                lambda state: state.has_all(("Skate Ability: Boneless", "Skate Ability: Boned Ollie"), player))
        add_rule(world.multiworld.get_location("BH Mission: Learn some wall tricks", player),
                lambda state: state.has_all(("Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride"), player))
        add_rule(world.multiworld.get_location("BH Mission: Impress Murphy", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride"), player))
        add_rule(world.multiworld.get_location("BH Mission: Impress Boone", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride"), player))
        add_rule(world.multiworld.get_location("BH Mission: Impress Dave", player),
                lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player))
        if options.include_skateboard_in_item_pool==True: 
            add_rule(world.multiworld.get_location("BH Mission: Second Tagging Mission", player),
                lambda state: (state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player)) or state.has("Skateboard Unlock", player))
            add_rule(world.multiworld.get_location("BH Mission: Third Tagging Mission", player),
                lambda state: (state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player)) or state.has("Skateboard Unlock", player))
            add_rule(world.multiworld.get_location("BH Mission: Fourth Tagging Mission", player),
                lambda state: (state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player)) or state.has("Skateboard Unlock", player))
            add_rule(world.multiworld.get_location("BH Mission: Fifth Tagging Mission", player),
                lambda state: (state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player)) or state.has("Skateboard Unlock", player))
        
        # Beverly Hills Stage 1 Gaps
        add_rule(world.multiworld.get_location("BH Gap: Rail 2 QP", player),
                lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
        add_rule(world.multiworld.get_location("BH Gap: Ramp 2 wire", player),
                lambda state: state.has("Progressive Speed Stat", player, 2))
        add_rule(world.multiworld.get_location("BH Gap: Across the street", player),
                lambda state: state.has_all_counts({"Progressive Speed Stat":7, "Progressive Ollie Stat":3}, player))
        add_rule(world.multiworld.get_location("BH Gap: Roof 2 roof", player),
                lambda state: state.has("Skate Ability: Spine Transfer/Acid Drop/Bank Drop", player))
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

    if options.end_goal >= EndGoal.option_win_the_skate_competition:
        set_rule(world.get_entrance("Hollywood No Skateboard Needed -> Downtown No Skateboard Needed"), can_downtown)
        set_rule(world.get_entrance("Skate Ranch -> Skate Ranch Stage 2"), can_skateranch_stage2)
        set_rule(world.get_entrance("Skate Ranch Stage 2 -> Skate Ranch Piece Missions"), can_skateranch_piece_missions)
        set_rule(world.get_entrance("Downtown Stage 2 -> Vans Park"), can_vanspark)
        #Skate Ranch Missions
        add_rule(world.multiworld.get_location("SR Mission: Skitch Sanchez", player),
            lambda state: state.has("Skate Ability: Skitch", player))
        add_rule(world.multiworld.get_location("SR Mission: Learn the Bert Slide from Iggy", player),
            lambda state: state.has_all(("Skate Ability: Skitch", "Skate Ability: Bert Slide"), player))
        #Skate Ranch S2 Gaps
        add_rule(world.multiworld.get_location("SR Gap: Ventura Fwy Drop", player),
            lambda state: state.has("Skate Ability: Stall", player))
        add_rule(world.multiworld.get_location("SR Gap: Bag Shop Arch Manual", player),
            lambda state: state.has("Progressive Speed Stat", player, 3))
        add_rule(world.multiworld.get_location("SR Gap: Green Dome Air", player),
            lambda state: state.has("Progressive Speed Stat", player, 10))
        add_rule(world.multiworld.get_location("SR Gap: El Teniente Grind", player),
            lambda state: state.has("Progressive Speed Stat", player, 3))
        add_rule(world.multiworld.get_location("SR Gap: Mexico Bell", player),
            lambda state: state.has("Progressive Speed Stat", player, 3))
        #BH S2 Gaps
        add_rule(world.multiworld.get_location("BH Gap: Upper ledge", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":3, "Progressive Ollie Stat":3}, player))
        add_rule(world.multiworld.get_location("BH Gap: Modern art?", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":5, "Progressive Ollie Stat":3, "Progressive Rail Stat":1}, player))
        add_rule(world.multiworld.get_location("BH Gap: No Tea baggin", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":5, "Progressive Ollie Stat":3, "Progressive Rail Stat":3}, player))
        add_rule(world.multiworld.get_location("BH Gap: Out by 7!!", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":5, "Progressive Ollie Stat":3, "Progressive Rail Stat":3}, player))
        #DT Stage 1 Missions
        add_rule(world.multiworld.get_location("DT Mission: First Tagging Mission", player),
            lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player))
        add_rule(world.multiworld.get_location("DT Mission: Second Tagging Mission", player),
            lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player))
        add_rule(world.multiworld.get_location("DT Mission: Third Tagging Mission", player),
            lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player))
        add_rule(world.multiworld.get_location("DT Mission: Fourth Tagging Mission", player),
            lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player))
        add_rule(world.multiworld.get_location("DT Mission: Fifth Tagging Mission", player),
            lambda state: state.has_all(("Skate Ability: Wall Run", "Skate Ability: Shimmy"), player))
        #DT Gaps
        add_rule(world.multiworld.get_location("DT Gap: Fence 2 Dumpster!", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":2, "Progressive Ollie Stat":3}, player))
        add_rule(world.multiworld.get_location("DT Gap: Over The Hut", player),
            lambda state: state.has("Progressive Speed Stat", player, 3))
        add_rule(world.multiworld.get_location("DT Gap: Chinese QP Transfer", player),
            lambda state: state.has("Progressive Speed Stat", player, 3))
        add_rule(world.multiworld.get_location("DT Gap: Fountain Manual", player),
            lambda state: state.has("Skate Ability: Manual", player))
        add_rule(world.multiworld.get_location("DT Gap: Freeway Flyer", player),
            lambda state: state.has("Progressive Speed Stat", player, 10))
        add_rule(world.multiworld.get_location("DT Gap: Chinese Air Transfer!", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":10, "Progressive Ollie Stat":10}, player))
        add_rule(world.multiworld.get_location("DT Gap: Manual The Dumpster!", player),
            lambda state: state.has("Progressive Manual Stat", player, 10))
        add_rule(world.multiworld.get_location("DT Gap: Freeway Bank!", player),
            lambda state: state.has_all_counts({"Skate Ability: Spine Transfer/Acid Drop/Bank Drop":1, "Progressive Speed Stat":3}, player))
        add_rule(world.multiworld.get_location("DT Gap: Underground Bank Transfer", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":10, "Progressive Ollie Stat":10, "Skate Ability: Spine Transfer/Acid Drop/Bank Drop":1}, player))
        add_rule(world.multiworld.get_location("DT Gap: Tunnel Transfer", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":10, "Progressive Ollie Stat":10}, player))
        add_rule(world.multiworld.get_location("DT Gap: Pyramid Drop!", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":2, "Skate Ability: Stall":1, "Skate Ability: Spine Transfer/Acid Drop/Bank Drop":1}, player))
        add_rule(world.multiworld.get_location("DT Gap: Big Lip!", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":2, "Skate Ability: Stall":1, "Skate Ability: Spine Transfer/Acid Drop/Bank Drop":1}, player))
        add_rule(world.multiworld.get_location("DT Gap: Overpass Air!", player),
            lambda state: state.has_all_counts({"Progressive Speed Stat":5, "Skate Ability: Stall":1, "Skate Ability: Spine Transfer/Acid Drop/Bank Drop":1}, player))
        #DT Stage 2 Missions
        add_rule(world.multiworld.get_location("DT Mission: Kick off the bell", player),
            lambda state: state.has("Progressive Speed Stat", player, 3))
        add_rule(world.multiworld.get_location("DT Mission: Learn the Board Stall", player),
            lambda state: state.has("Skate Ability: Stall", player))
        set_rule(world.get_location("DT Mission: Learn Special and Focus"), can_vanspark) 

    # Victory Goal Stuff
    if options.end_goal == EndGoal.option_smash_the_t_rex:
        add_rule(world.multiworld.get_location("Smash the T-Rex", player),
                lambda state: state.has("Skate Ability: Manual", player) and state.has("Skate Ability: Revert", player) and state.has("Skate Ability: Caveman", player))
    if options.end_goal == EndGoal.option_get_to_the_skate_ranch:
        set_rule(world.multiworld.get_location("Get to the Skate Ranch", player), can_skateranch)
        #add_rule(world.multiworld.get_location("Get to the Skate Ranch", player),
        #        lambda state: state.has_all(("Skate Ability: Natas Spin", "Skate Ability: Wall Run", "Skate Ability: Wall Flip", "Skate Ability: Shimmy", "Skate Ability: Back Tuck/Front Tuck", "Skate Ability: Spine Transfer/Acid Drop/Bank Drop", "Skate Ability: Flips/Rolls", "Skate Ability: Boneless", "Skate Ability: Boned Ollie", "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant", "Skate Ability: Wall Ride", "Skate Ability: Manual"), player))
    if options.end_goal == EndGoal.option_win_the_skate_competition:
            set_rule(world.multiworld.get_location("Win the Skate Competition", player), can_vanspark)    

def set_completion_condition(world: THAWWorld) -> None:
    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)