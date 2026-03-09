# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items they need to be bundled in a list
# A list in programming terms is anything in square brackets [] to put it simply

# When a list is described its described as a list of x where x is the type of variable within it
# IE: ["apple", "pear", "grape"] is a list of strings (anything inside "" OR '' are considered strings)

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name
# You can also do that ctrl + click for any functions to see what they do
from .Types import ItemData, VictoryConditionType, THAWItem, victory_condition_type_to_name
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

# This is just making sure nothing gets confused dw about what its doing exactly
if TYPE_CHECKING:
    from . import THAWWorld

# If you're curious about the -> List[Item] that is a syntax to make sure you return the correct variable type
# In this instance we're saying we only want to return a list of items
# You'll see a bunch of other examples of this in other functions
# It's main purpose is to protect yourself from yourself
def create_itempool(world: "THAWWorld") -> List[Item]:
    # This is the empty list of items. You'll add all the items in the game to this list
    itempool: List[Item] = []

    # In this function is where you would remove any starting items that you add in options such as starting chapter
    # This is also the place you would add dynamic amounts of items from options
    # I can point to Sly Cooper and the Thievious Raccoonus since I did that

    # This is a good place to grab anything you need from options
    victory_condition = victory_condition_type_to_name[VictoryConditionType(world.options.VictoryCondition)]
    
    # It's up to you and how you want things organized but I like to deal with victory here
    # This creates your win item and then places it at the "location" where you win
    if victory_condition == "Smash the T-Rex":
        victory = create_item(world, "Victory")
        world.multiworld.get_location("Smash the T-rex", world.player).place_locked_item(victory)

    #if victory_condition == "Get to the Skate Ranch":
    #    victory = create_item(world, "Victory")

    # Then junk items are made
    # Check out the create_junk_items function for more details
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)

    return itempool

# This is a generic function to create a singular item
def create_item(world: "THAWWorld", name: str) -> Item:
    data = item_table[name]
    return THAWItem(name, data.classification, data.ap_code, world.player)

# Another generic function. For creating a bunch of items at once!
def create_multiple_items(world: "THAWWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [THAWItem(name, item_type, data.ap_code, world.player)]

    return itemlist

# Finally, where junk items are created
def create_junk_items(world: "THAWWorld", count: int) -> List[Item]:
    #trap_chance = world.options.TrapChance.value
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    #trap_list: Dict[str, int] = {}

    # This grabs all the junk items and trap items
    for name in item_table.keys():
        # Here we are getting all the junk item names and weights
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

        # This is for traps if your randomization includes it
        # It also grabs the trap weights from the options page
        #elif trap_chance > 0 and ic == ItemClassification.trap:
            #if name == "Forcefem Trap":
                #trap_list[name] = world.options.ForcefemTrapWeight.value
            #elif name == "Speed Change Trap":
                #trap_list[name] = world.options.SpeedChangeTrapWeight.value

    # Where all the magic happens of adding the junk and traps randomly
    # AP does all the weight management so we just need to worry about how many are created
    for i in range(count):
        #if trap_chance > 0 and world.random.randint(1, 100) <= trap_chance:
            #junk_pool.append(world.create_item(
                #world.random.choices(list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]))
        #else:
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

# Time for the fun part of listing all of the items
# Watch out for overlap with your item codes
# These are just random numbers dont trust them PLEASE
# I've seen some games that dynamically add item codes such as DOOM as well
THAW_items = {
    # Player Stats
    "Progressive Air Stat": ItemData(10000001, ItemClassification.useful, 10),
    "Progressive Speed Stat": ItemData(10000002, ItemClassification.progression, 10),
    "Progressive Rail Stat": ItemData(10000003, ItemClassification.progression, 10),
    "Progressive Manual Stat": ItemData(10000004, ItemClassification.useful, 10),
    "Progressive Flip Stat": ItemData(10000005, ItemClassification.useful, 10),
    "Progressive Lip Stat": ItemData(10000006, ItemClassification.useful, 10),
    "Progressive Ollie Stat": ItemData(10000007, ItemClassification.progression, 10),
    "Progressive Run Stat": ItemData(10000008, ItemClassification.useful, 10),
    "Progressive Switch Stat": ItemData(10000009, ItemClassification.progression, 10),
    "Progressive Spin Stat": ItemData(10000010, ItemClassification.useful, 10),

    # Player Skating Abilities
    "Skate Ability: Caveman": ItemData(11000001, ItemClassification.progression),
    "Skate Ability: Manual": ItemData(11000002, ItemClassification.progression),
    "Skate Ability: Revert": ItemData(11000003, ItemClassification.progression),
    "Skate Ability: Spine Transfer/Acid Drop/Bank Drop": ItemData(11000004, ItemClassification.progression),
    "Skate Ability: Wall Ride": ItemData(11000005, ItemClassification.progression),
    "Skate Ability: Sticker Slap/Wall Plant/Vert Wall Plant": ItemData(11000006, ItemClassification.progression),
    "Skate Ability: Natas Spin": ItemData(11000007, ItemClassification.progression),
    "Skate Ability: Boneless": ItemData(11000008, ItemClassification.progression),
    "Skate Ability: Boned Ollie": ItemData(11000009, ItemClassification.progression),
    "Skate Ability: Flips/Rolls": ItemData(11000010, ItemClassification.progression),
    "Skate Ability: Wall Run": ItemData(11000011, ItemClassification.progression),
    "Skate Ability: Shimmy": ItemData(11000012, ItemClassification.progression),
    "Skate Ability: Wall Flip": ItemData(11000013, ItemClassification.progression),
    "Skate Ability: Back Tuck/Front Tuck": ItemData(11000014, ItemClassification.progression),
    "Skate Ability: Bert Slide": ItemData(11000015, ItemClassification.progression),
    "Skate Ability: Skitch": ItemData(11000016, ItemClassification.progression),
    "Skate Ability: Special": ItemData(11000017, ItemClassification.progression),
    "Skate Ability: Focus": ItemData(11000018, ItemClassification.progression),
    "Skate Ability: Stall": ItemData(11000019, ItemClassification.progression),
    "Skate Ability: Flatland": ItemData(11000020, ItemClassification.progression),

    # Unlocked Special Tricks

    # Victory is added here since in this organization it needs to be in the default item pool
    "Victory": ItemData(20050007, ItemClassification.progression)
}

# I like to split up the items so that its easier to look at and since sometimes you only need to look at one specific type of list
# An example of that is in create_itempool where I simulated having a starting chapter
# THAW_chapters = {
#     "Green Hill Zone": ItemData(20050008, ItemClassification.progression),
#    "Romania": ItemData(20050009, ItemClassification.progression),
#    "The Sewer": ItemData(20050010, ItemClassification.progression)
# }

# In the way that I made items, I added a way to specify how many of an item should exist
# That's why junk has a 0 since how many are created is in the create_junk_items
# There is a better way of doing this but this is my jank
junk_items = {
    # Junk and Cash
    "5 Bucks": ItemData(90000001, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "10 Bucks": ItemData(90000002, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "40 Bucks": ItemData(90000003, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "100 Bucks": ItemData(90000004, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "200 Bucks": ItemData(90000005, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),
    "500 Bucks": ItemData(90000006, ItemClassification.filler | ItemClassification.progression_skip_balancing, 0),

    # Traps
    #"Forcefem Trap": ItemData(20050013, ItemClassification.trap, 0),
    #"Speed Change Trap": ItemData(20050014, ItemClassification, 0)
}

# Junk weights is just how often an item will be chosen when junk is being made
# Bigger item = more likely to show up
junk_weights = {
    "5 Bucks": 30,
    "10 Bucks": 25,
    "40 Bucks": 10,
    "100 Bucks": 6,
    "200 Bucks": 5,
    "500 Bucks": 3
}

# This makes a really convenient list of all the other dictionaries
# (fun fact: {} is a dictionary)
item_table = {
    **THAW_items,
    **junk_items
}