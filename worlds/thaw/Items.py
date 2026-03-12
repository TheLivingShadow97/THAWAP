from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple, Optional, Dict, List

from BaseClasses import Item, ItemClassification
from .Options import EndGoal, THAWOptions

#if TYPE_CHECKING:
#    from .world import THAWWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.

class THAWItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification = ItemClassification.progression_deprioritized_skip_balancing
    count: Optional[int] = 1


stats_item_table: Dict[str, THAWItemData] = {
    "Progressive Air Stat": THAWItemData(10000001, ItemClassification.useful, 10),
    "Progressive Speed Stat": THAWItemData(10000002, ItemClassification.progression, 10),
    "Progressive Rail Stat": THAWItemData(10000003, ItemClassification.progression, 10),
    "Progressive Manual Stat": THAWItemData(10000004, ItemClassification.useful, 10),
    "Progressive Flip Stat": THAWItemData(10000005, ItemClassification.useful, 10),
    "Progressive Lip Stat": THAWItemData(10000006, ItemClassification.useful, 10),
    "Progressive Ollie Stat": THAWItemData(10000007, ItemClassification.progression, 10),
    "Progressive Run Stat": THAWItemData(10000008, ItemClassification.useful, 10),
    "Progressive Switch Stat": THAWItemData(10000009, ItemClassification.progression, 10),
    "Progressive Spin Stat": THAWItemData(10000010, ItemClassification.useful, 10)
}

skating_abilities_item_table: Dict[str, THAWItemData] = {
    "Skate Ability: Caveman": THAWItemData(11000001, ItemClassification.progression),
    "Skate Ability: Manual": THAWItemData(11000002, ItemClassification.progression),
    "Skate Ability: Revert": THAWItemData(11000003, ItemClassification.progression),
    "Skate Ability: Spine Transfer/Acid Drop/Bank Drop": THAWItemData(11000004, ItemClassification.progression),
    "Skate Ability: Wall Ride": THAWItemData(11000005, ItemClassification.progression),
    "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant": THAWItemData(11000006, ItemClassification.progression),
    "Skate Ability: Natas Spin": THAWItemData(11000007, ItemClassification.progression),
    "Skate Ability: Boneless": THAWItemData(11000008, ItemClassification.progression),
    "Skate Ability: Boned Ollie": THAWItemData(11000009, ItemClassification.progression),
    "Skate Ability: Flips/Rolls": THAWItemData(11000010, ItemClassification.progression),
    "Skate Ability: Wall Run": THAWItemData(11000011, ItemClassification.progression),
    "Skate Ability: Shimmy": THAWItemData(11000012, ItemClassification.progression),
    "Skate Ability: Wall Flip": THAWItemData(11000013, ItemClassification.progression),
    "Skate Ability: Back Tuck/Front Tuck": THAWItemData(11000014, ItemClassification.progression),
    "Skate Ability: Bert Slide": THAWItemData(11000015, ItemClassification.progression),
    "Skate Ability: Skitch": THAWItemData(11000016, ItemClassification.progression),
    "Skate Ability: Special": THAWItemData(11000017, ItemClassification.progression),
    "Skate Ability: Focus": THAWItemData(11000018, ItemClassification.progression),
    "Skate Ability: Stall": THAWItemData(11000019, ItemClassification.progression),
    "Skate Ability: Flatland": THAWItemData(11000020, ItemClassification.progression),
}

cash_item_table: Dict[str, THAWItemData] = {
    "5 Bucks": THAWItemData(90000001, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "10 Bucks": THAWItemData(90000002, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "40 Bucks": THAWItemData(90000003, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "100 Bucks": THAWItemData(90000004, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "200 Bucks": THAWItemData(90000005, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "500 Bucks": THAWItemData(90000006, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0)
}

goaling_item_table: Dict[str, THAWItemData] = {
    "Victory": THAWItemData(None, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
}

item_data_table = {
    **stats_item_table,
    **skating_abilities_item_table,
    **cash_item_table,
    **goaling_item_table
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.

# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class THAWItem(Item):
    game = "Tony Hawk's American Wasteland"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
#def get_random_filler_item_name(world: THAWWorld) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    #if world.random.randint(0, 99) < world.options.trap_chance:
    #    return "Math Trap"
#    return "Confetti Cannon"

junk_weights = {
    "5 Bucks": 30,
    "10 Bucks": 25,
    "40 Bucks": 10,
    "100 Bucks": 6,
    "200 Bucks": 5,
    "500 Bucks": 3
}

def setup_items(options: THAWOptions):
    temp_item_table = {}
    temp_item_table.update({**stats_item_table})
    temp_item_table.update({**skating_abilities_item_table})
    temp_item_table.update({**goaling_item_table})
    return temp_item_table