from BaseClasses import Region
from .Types import THAWLocation
from .Locations import location_table, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import THAWWorld

# This is where you will create your imaginary game world
# IE: connect rooms and areas together
# This is NOT where you'll add requirements for how to get to certain locations thats in Rules.py
# This is also long and tediouos
def create_regions(world: "THAWWorld"):
    # The functions that are being used here will be located at the bottom to view
    # The important part is that if its not a dead end and connects to another place then name it
    # Otherwise you can just create the connection. Not that naming it is bad

    # You can technically name your connections whatever you want as well
    # You'll use those connection names in Rules.py
    hollywood = create_region(world, "Hollywood")
    beverlyhills = create_region_and_connect(world, "Beverly Hills", "Hollywood -> Beverly Hills", hollywood)
    skateranch = create_region_and_connect(world, "Skate Ranch", "Beverly Hills -> Skate Ranch", beverlyhills)
    hollywoodstage2 = create_region_and_connect(world, "Hollywood Stage 2", "Skate Ranch -> Hollywood Stage 2", skateranch)
    beverlyhillsstage2 = create_region_and_connect(world, "Beverly Hills Stage 2", "Skate Ranch -> Beverly Hills Stage 2", skateranch)
    downtown = create_region_and_connect(world, "Downtown", "Hollywood Stage 2 -> Downtown", hollywoodstage2)
    vanspark = create_region_and_connect(world, "Vans Park", "Downtown -> Vans Park", downtown)
    santamonica = create_region_and_connect(world, "Santa Monica", "Vans Park -> Santa Monica", vanspark)
    oilrig = create_region_and_connect(world, "Oil Rig", "Santa Monica -> Oil Rig", santamonica)
    eastla = create_region_and_connect(world, "East LA", "Oil Rig -> East LA", oilrig)
    skateranchstage2 = create_region_and_connect(world, "Skate Ranch Stage 2", "East LA -> Skate Ranch Stage 2", eastla)
    beverlyhillsstage3 = create_region_and_connect(world, "Beverly Hills Stage 3", "Skate Ranch Stage 2 -> Beverly Hills Stage 3", skateranchstage2)
    hollywoodstage3 = create_region_and_connect(world, "Hollywood Stage 3", "Skate Ranch Stage 2 -> Hollywood Stage 3", skateranchstage2)
    downtownstage2 = create_region_and_connect(world, "Downtown Stage 2", "Skate Ranch Stage 2 -> Downtown Stage 2", skateranchstage2)
    santamonicastage2 = create_region_and_connect(world, "Santa Monica Stage 2", "Skate Ranch Stage 2 -> Santa Monica Stage 2", skateranchstage2)
    eastlastage2 = create_region_and_connect(world, "East LA Stage 2", "Skate Ranch Stage 2 -> East LA Stage 2", skateranchstage2)
    casino = create_region_and_connect(world, "Casino", "East LA -> Casino", eastlastage2)


def create_region(world: "THAWWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # When we create the region we go through all the locations we made and check if they are in that region
    # If they are and are valid, we attach it to the region
    for (key, data) in location_table.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = THAWLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

# This runs the create region function while also connecting to another region
# Just simplifies process since you woill be connecting a lot of regions
def create_region_and_connect(world: "THAWWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg