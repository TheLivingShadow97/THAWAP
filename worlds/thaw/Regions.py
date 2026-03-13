from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, MultiWorld
from .Options import EndGoal, THAWOptions
from .Locations import THAWLocation

#if TYPE_CHECKING:
#    from .world import THAWWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).

#opening regions
thaw_stage1_regions = [
    "Hollywood",
    "Beverly Hills",
    "Downtown",
    "Santa Monica",
    "East LA"
]

#get parts for the skate ranch and win the contest
thaw_stage2_regions = [
    "Skate Ranch",
    "Beverly Hills Stage 2",
    "Hollywood Stage 2",
    "Downtown Stage 2",
    "Vans Park"
]

#go to the beach
thaw_stage3_regions = [
    "Santa Monica Stage 2"
]

#get the crane
thaw_stage4_regions = [
    "Oil Rig"
]

#prove yourself to hector
thaw_stage5_regions = [
    "Downtown Stage 3"
]

#rescue Boone and get some parts
thaw_stage6_regions = [
    "East LA Stage 2",
    "Skate Ranch Stage 2"
]

#gather skaters to save green pipes point
thaw_stage7_regions = [
    "Beverly Hills Stage 3",
    "Hollywood Stage 3",
    "Downtown Stage 4",
    "Santa Monica Stage 3",
    "East LA Stage 3",
]

#get parts for the skate ranch and escape the cops to save gpp 
thaw_stage8_regions = [
    "Casino"
]

thaw_all_regions = [
    *thaw_stage1_regions,
    *thaw_stage2_regions,
    *thaw_stage3_regions,
    *thaw_stage4_regions,
    *thaw_stage5_regions,
    *thaw_stage6_regions,
    *thaw_stage7_regions,
    *thaw_stage8_regions
]


def create_regions(world: MultiWorld, player: int, seed_locations):

    for region in thaw_all_regions:
        create_regions_and_locations(region, player, world, seed_locations)

    connect_regions(world, player, "Hollywood", "Beverly Hills")
    connect_regions(world, player, "Hollywood", "Downtown")
    connect_regions(world, player, "Hollywood", "Santa Monica")
    connect_regions(world, player, "Hollywood", "East LA")
    connect_regions(world, player, "Beverly Hills", "Skate Ranch")
    connect_regions(world, player, "Skate Ranch", "Beverly Hills Stage 2")
    connect_regions(world, player, "Skate Ranch", "Hollywood Stage 2")
    connect_regions(world, player, "Skate Ranch", "Downtown Stage 2")
    connect_regions(world, player, "Downtown Stage 2", "Vans Park")
    connect_regions(world, player, "Vans Park", "Santa Monica Stage 2")
    connect_regions(world, player, "Santa Monica Stage 2", "Oil Rig")
    connect_regions(world, player, "Oil Rig", "Downtown Stage 3")
    connect_regions(world, player, "Downtown Stage 3", "East LA Stage 2")
    connect_regions(world, player, "East LA Stage 2", "Skate Ranch Stage 2")
    connect_regions(world, player, "Skate Ranch Stage 2", "Beverly Hills Stage 3")
    connect_regions(world, player, "Skate Ranch Stage 2", "Hollywood Stage 3")
    connect_regions(world, player, "Skate Ranch Stage 2", "Downtown Stage 4")
    connect_regions(world, player, "Skate Ranch Stage 2", "East LA Stage 3")
    connect_regions(world, player, "Skate Ranch Stage 2", "Santa Monica Stage 3")
    connect_regions(world, player, "East LA Stage 3", "Casino")



def connect_regions(world: MultiWorld, player: int, source: str, target: str) -> Entrance:
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    return source_region.connect(target_region)


def create_regions_and_locations(name: str, player: int, world: MultiWorld, seed_locations) -> Region:
    region = Region(name, player, world)

    for (key, data) in seed_locations.items():
        if data.region == name:
            location = THAWLocation(player, key, data.ap_code, region)
            region.locations.append(location)

    world.regions.append(region)
    return region

def create_events(world: MultiWorld, player: int, options: THAWOptions):
    smashtrex = world.get_location("Smash the T-Rex", player)
    if options.end_goal == EndGoal.option_smash_the_t_rex:
        smashtrex.place_locked_item("Victory")

#def create_events(multiworld: THAWWorld)-> None:
    # If your world has events, you can create them here.
    # Events are just like locations, but they don't have an item attached to them and are not part of the item pool.
    # They are used for things like cutscenes, boss fights, or other important milestones that you want to have rules around.
    #if THAWOptions().EndGoal == EndGoal.option_smash_the_t_rex:
    #    "Smash the T-Rex".place_locked_item("Victory")