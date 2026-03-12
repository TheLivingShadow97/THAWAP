# The first thing you should make for your world is an archipelago.json manifest file.
# You can reference APQuest's, but you should change the "game" field (obviously),
# and you should also change the "minimum_ap_version" - probably to the current value of Utils.__version__.

# Apart from the regular apworld code that allows generating multiworld seeds with your game,
# your apworld might have other "components" that should be launchable from the Archipelago Launcher.
# You can ignore this for now. If you are specifically interested in components, you can read components.py.

# The main thing we do in our __init__.py is importing our world class from our world.py to initialize it.
# Obviously, this world class needs to exist first. For this, read world.py.
from .world import THAWWorld as THAWWorld
from .Locations import all_location_table, THAWLocData

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