from collections.abc import Mapping
from typing import Any, Dict

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World
from BaseClasses import Item

# Imports of your world's files must be relative.
from . import Rules, web_world
from . import Options as thaw_options  # rename due to a name conflict with World.options
from .Locations import setup_locations, all_location_table
from .Items import THAWItemData, item_data_table, setup_items, THAWItem 
from .Regions import create_regions
from .Options import EndGoal

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
    seed_item_table: Dict[str, THAWItemData]

    location_name_groups = {
        "Hollywood": {name for name, data in all_location_table.items()
                                   if data.region == "Hollywood"},
        "Beverly Hills": {name for name, data in all_location_table.items() if data.region == "Beverly Hills"},
        "Downtown": {name for name, data in all_location_table.items() if data.region == "Downtown"},
        "Santa Monica": {name for name, data in all_location_table.items()
                                      if data.region == "Santa Monica"},
        "East LA": {name for name, data in all_location_table.items()
                                    if data.region == "East LA"},
        "Skate Ranch": {name for name, data in all_location_table.items() if data.region == "Skate Ranch"},
        "Beverly Hills Stage 2": {name for name, data in all_location_table.items()
                                 if data.region == "Beverly Hills Stage 2"},
        "Hollywood Stage 2": {name for name, data in all_location_table.items() if data.region == "Hollywood Stage 2"},
        "Downtown Stage 2": {name for name, data in all_location_table.items() if data.region == "Downtown Stage 2"},
        "Vans Park": {name for name, data in all_location_table.items() if data.region == "Vans Park"},
        "Santa Monica Stage 2": {name for name, data in all_location_table.items() if data.region == "Santa Monica Stage 2"},
        "Oil Rig": {name for name, data in all_location_table.items() if data.region == "Oil Rig"},
        "Downtown Stage 3": {name for name, data in all_location_table.items()
                                      if data.region == "Downtown Stage 3"},
        "East LA Stage 2": {name for name, data in all_location_table.items() if data.region == "East LA Stage 2"},
        "Skate Ranch Stage 2": {name for name, data in all_location_table.items() if data.region == "Skate Ranch Stage 2"},
        "Beverly Hills Stage 3": {name for name, data in all_location_table.items()
                                    if data.region == "Beverly Hills Stage 3"},
        "Hollywood Stage 3": {name for name, data in all_location_table.items()
                                           if data.region == "Hollywood Stage 3"},
        "Downtown Stage 4": {name for name, data in all_location_table.items() if data.region == "Downtown Stage 4"},
        "East LA Stage 3": {name for name, data in all_location_table.items() if data.region == "East LA Stage 3"},
        "Casino": {name for name, data in all_location_table.items()
                                  if data.region == "Casino"},
    }

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = {name: data.ap_code for name, data in all_location_table.items()}
    item_name_to_id = item_name_to_id = {name: data.ap_code for name, data in item_data_table.items() if data.ap_code is not None}

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Hollywood"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self):
        self.seed_location_table = setup_locations(self.options)
        create_regions(self.multiworld, self.player, self.seed_location_table)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = THAWItem(name, data.classification, data.ap_code, self.player)
        return item
    
    def set_rules(self) -> None:
        Rules.set_all_rules(self)
        Rules.set_completion_condition(self)
        #need to define an entrance rule function in future

    def create_items(self) -> None:
        self.seed_item_table = setup_items(self.options)

        for item_name, data in self.seed_item_table.items():
            count = data.count

            for _ in range(count):
                temp_item = self.create_item(item_name)
                self.multiworld.itempool.append(temp_item)

        #it works!
        if self.options.end_goal == EndGoal.option_smash_the_t_rex:
            smashtrex = self.multiworld.get_location("Smash the T-Rex", self.player)
            victory = self.create_item("Victory")
            smashtrex.place_locked_item(victory)


        total_locations = len(self.multiworld.get_locations())
        remaining_items = total_locations - len(self.multiworld.itempool)

        if remaining_items > 0:
            self.create_filler_items(remaining_items)

    #maybe add traps later? may also need balancing
    def create_filler_items(self, remaining_items: int):
        filler_items = {
            "5 Bucks": 30,
            "10 Bucks": 25,
            "40 Bucks": 10,
            "100 Bucks": 6,
            "200 Bucks": 5,
            "500 Bucks": 3
        }

        names, weights = zip(*filler_items.items())

        for _ in range(remaining_items):
            item_name = self.random.choices(names, weights=weights, k=1)[0]
            self.multiworld.itempool.append(self.create_item(item_name))

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "end_goal"
        )
