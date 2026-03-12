from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from .Options import EndGoal, THAWOptions

if TYPE_CHECKING:
    from .world import THAWWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).

thaw_stage1_regions = [
    "Hollywood",
    "Beverly Hills",
    "Downtown",
    "Santa Monica",
    "East LA"
]

thaw_stage2_regions = [
    "Skate Ranch",
    "Beverly Hills Stage 2",
    "Hollywood Stage 2",
    "Downtown Stage 2",
    "Vans Park"
]

thaw_stage3_regions = [
    "Santa Monica Stage 2"
]

thaw_stage4_regions = [
    "Oil Rig"
]

thaw_stage5_regions = [
    "Downtown Stage 3"
]

thaw_stage6_regions = [
    "East LA Stage 2",
    "Skate Ranch Stage 2"
]

thaw_stage7_regions = [
    "Beverly Hills Stage 3",
    "Hollywood Stage 3",
    "Downtown Stage 4",
    "East LA Stage 3",
]

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

def create_and_connect_regions(world: THAWWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: THAWWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    hollywood = Region("Hollywood", world.player, world.multiworld)
    downtown = Region("Downtown", world.player, world.multiworld)
    santamonica = Region("Santa Monica", world.player, world.multiworld)
    eastla = Region("East LA", world.player, world.multiworld)
    beverlyhills = Region("Beverly Hills", world.player, world.multiworld)
    skateranch = Region("Skate Ranch", world.player, world.multiworld)
    hollywoodstage2 = Region("Hollywood Stage 2", world.player, world.multiworld)
    beverlyhillsstage2 = Region("Beverly Hills Stage 2", world.player, world.multiworld)
    downtownstage2 = Region("Downtown Stage 2", world.player, world.multiworld)
    vanspark = Region("Vans Park", world.player, world.multiworld)
    santamonicastage2 = Region("Santa Monica Stage 2", world.player, world.multiworld)
    eastlastage2 = Region("East LA Stage 2", world.player, world.multiworld)
    oilrig = Region("Oil Rig", world.player, world.multiworld)
    skateranchstage2 = Region("Skate Ranch Stage 2", world.player, world.multiworld)
    beverlyhillsstage3 = Region("Beverly Hills Stage 3", world.player, world.multiworld)
    hollywoodstage3 = Region("Hollywood Stage 3", world.player, world.multiworld)
    downtownstage3 = Region("Downtown Stage 3", world.player, world.multiworld)
    santamonicastage3 = Region("Santa Monica Stage 3", world.player, world.multiworld)
    eastlastage3 = Region("East LA Stage 3", world.player, world.multiworld)
    casino = Region("Casino", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [hollywood, downtown, santamonica, eastla, beverlyhills, skateranch, hollywoodstage2, beverlyhillsstage2, 
               vanspark, oilrig, skateranchstage2, beverlyhillsstage3, hollywoodstage3, downtownstage2, santamonicastage2, 
               eastlastage2, casino, downtownstage3, santamonicastage3, eastlastage3]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    #if world.options.hammer:
    #    top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #    regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: THAWWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    hollywood = world.get_region("Hollywood")
    downtown = world.get_region("Downtown")
    santamonica = world.get_region("Santa Monica")
    beverlyhills = world.get_region("Beverly Hills")
    eastla = world.get_region("East LA")
    skateranch = world.get_region("Skate Ranch")
    hollywoodstage2 = world.get_region("Hollywood Stage 2")
    beverlyhillsstage2 = world.get_region("Beverly Hills Stage 2")
    vanspark = world.get_region("Vans Park")    
    oilrig = world.get_region("Oil Rig")
    skateranchstage2 = world.get_region("Skate Ranch Stage 2")
    beverlyhillsstage3 = world.get_region("Beverly Hills Stage 3")
    hollywoodstage3 = world.get_region("Hollywood Stage 3")
    downtownstage2 = world.get_region("Downtown Stage 2")
    santamonicastage2 = world.get_region("Santa Monica Stage 2")
    eastlastage2 = world.get_region("East LA Stage 2")
    casino = world.get_region("Casino")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    #overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    #overworld.exits.append(overworld_to_bottom_right_room)

    # You can then connect the Entrance to the target region.
    #overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    #overworld.connect(right_room, "Overworld to Right Room")
    #right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    #overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    #if world.options.hammer:
        #top_middle_room = world.get_region("Top Middle Room")
        #overworld.connect(top_middle_room, "Overworld to Top Middle Room")
def create_events(multiworld: THAWWorld)-> None:
    # If your world has events, you can create them here.
    # Events are just like locations, but they don't have an item attached to them and are not part of the item pool.
    # They are used for things like cutscenes, boss fights, or other important milestones that you want to have rules around.
    if THAWOptions().EndGoal == EndGoal.option_smash_the_t_rex:
        "Smash the T-Rex".place_locked_item("Victory")