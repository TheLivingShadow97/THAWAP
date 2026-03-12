from collections.abc import Mapping
from itertools import count
from typing import Any, Dict, List

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification

# Imports of your world's files must be relative.
from . import regions, rules, web_world
from . import options as thaw_options  # rename due to a name conflict with World.options
from .Locations import setup_locations, all_location_table
from .Items import item_data_table, setup_items, THAWItem, junk_weights

seed_location_table: Dict[str, int]
seed_item_table: Dict[str, int]

# APQuest will go through all the parts of the world api one step at a time,
# with many examples and comments across multiple files.
# If you'd rather read one continuous document, or just like reading multiple sources,
# we also have this document specifying the entire world api:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md


# The world class is the heart and soul of an apworld implementation.
# It holds all the data and functions required to build the world and submit it to the multiworld generator.
# You could have all your world code in just this one class, but for readability and better structure,
# it is common to split up world functionality into multiple files.
# This implementation in particular has the following additional files, each covering one topic:
# regions.py, locations.py, rules.py, items.py, options.py and web_world.py.
# It is recommended that you read these in that specific order, then come back to the world class.
class THAWWorld(World):
    """
    Tony Hawk's American Wasteland is an open world skateboarding game developed by Neversoft. It's pretty rad.
    """

    # The docstring should contain a description of the game, to be displayed on the WebHost.

    # You must override the "game" field to say the name of the game.
    game = "Tony Hawk's American Wasteland"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.THAWWebWorld()

    # This is how we associate the options defined in our options.py with our world.
    # (Note: options.py has been imported as "thaw_options" at the top of this file to avoid a name conflict)
    options_dataclass = thaw_options.THAWOptions
    options: thaw_options.THAWOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    seed_location_table: Dict[str, int]
    seed_item_table: Dict[str, int]

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = {name: data.id for name, data in all_location_table.items()}
    item_name_to_id = item_name_to_id = {name: data.code for name, data in item_data_table.items() if data.code is not None}

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Hollywood"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self):
        self.seed_location_table = setup_locations(self.options)
        regions.create_and_connect_regions(self.multiworld, self.player, self.seed_location_table)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = THAWItem(name, data.classification, data.code, self.player)
        return item
    
    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self):
        self.seed_item_table = setup_items(self.options)
        self.multiworld.itempool += [self.create_item(item_name) for item_name in self.seed_item_table]

    def create_events(self):
        regions.create_events(self.multiworld, self.player)

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    
    def create_junk_items(world: "THAWWorld", count: int) -> List[Item]:
        #trap_chance = world.options.TrapChance.value
        junk_pool: List[Item] = []
        junk_list: Dict[str, int] = {}
        #trap_list: Dict[str, int] = {}

        # This grabs all the junk items and trap items
        for name in item_data_table.keys():
        # Here we are getting all the junk item names and weights
            ic = item_data_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

    # Where all the magic happens of adding the junk and traps randomly
    # AP does all the weight management so we just need to worry about how many are created
        for i in range(count):
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

            return junk_pool


    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "end_goal"
        )