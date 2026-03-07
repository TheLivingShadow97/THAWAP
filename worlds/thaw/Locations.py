# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData
from .Items import victory_condition

if TYPE_CHECKING:
    from . import THAWWorld

# This is technique in programming to make things more readable for booleans
# A boolean is true or false
#def did_include_extra_locations(world: "THAWWorld") -> bool:
#    return bool(world.options.ExtraLocations)

# This is used by ap and in Items.py
# Theres a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "THAWWorld") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    total = 0
    for name in location_table:
        # If we did not turn on extra locations (see how readable it is with that thing from the top)
        # AND the name of it is found in our extra locations table, then that means we dont want to count it
        # So continue moves onto the next name in the table
        if victory_condition != "Smash the T-Rex" and name in Trex_locations:
            continue

        # If the location is valid though, count it
        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary thats {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

# The check to make sure the location is valid
# I know it looks like the same as when we counted it but thats because this is an example
# Things get complicated fast so having a back up is nice
def is_valid_location(world: "THAWWorld", name) -> bool:
    if victory_condition != "Smash the T-rex" and name in Trex_locations:
        return False
    
    return True

# You might need more functions as well so be liberal with them
# My advice, if you are about to type the same thing in a second time, turn it into a function
# Even if you only do it once you can turn it into a function too for organization

# Heres where you do the next fun part of listing out all those locations
# Its a lot
# My advice, zone out for half an hour listening to music and hope you wake up to a completed list
THAW_locations = {
    # You can take a peak at Types.py for more information but,
    # LocData is code, region in this instance
    # Regions will be explained more in Regions.py
    # But just know that it's mostly about organization
    # Place locations together based on where they are in the game and what is needed to get there
    # Hollywood Stage 1 Missions
    "HW Mission: Change Your Look": LocData(10100001, "Hollywood"),
    "HW Mission: Change Your Clothes": LocData(10100002, "Hollywood"),
    "HW Mission: Learn to Caveman": LocData(10100003, "Hollywood"),
    "HW Mission: Do a Sponsor Challenge": LocData(10100004, "Hollywood"),
    "HW Mission: Kickflip Whofleck": LocData(10100005, "Hollywood"),
    "HW Mission: Learn to Revert": LocData(10100006, "Hollywood"),
    "HW Mission: Get Your Stuff Back": LocData(10100007, "Hollywood"),
    "HW Mission: Get Into Beverly Hills": LocData(10100008, "Hollywood"),
    "HW Mission: First Tagging Mission": LocData(10150001, "Hollywood"),
    "HW Mission: Second Tagging Mission": LocData(10150002, "Hollywood"),
    "HW Mission: Third Tagging Mission": LocData(10150003, "Hollywood"),
    "HW Mission: Fourth Tagging Mission": LocData(10150004, "Hollywood"),
    "HW Mission: Fifth Tagging Mission": LocData(10150005, "Hollywood"),
    # Hollywood Gaps
    "HW Gap: Bench2Bench": LocData(10200001, "Hollywood"),
    "HW Gap: FireEscape Level1": LocData(10200002, "Hollywood"),
    "HW Gap: Hollywood High Steps": LocData(10200003, "Hollywood"),
    "HW Gap: Planter2Planter": LocData(10200004, "Hollywood"),
    "HW Gap: Rail2Bleacher": LocData(10200005, "Hollywood"),
    "HW Gap: Rail2Rail": LocData(10200006, "Hollywood"),
    "HW Gap: Bleacher Hop": LocData(10200007, "Hollywood"),
    "HW Gap: Car Hop": LocData(10200008, "Hollywood"),
    "HW Gap: Chinese Transfer": LocData(10200009, "Hollywood"),
    "HW Gap: El Teniente Spine": LocData(10200010, "Hollywood"),
    "HW Gap: FireEscape Level2": LocData(10200011, "Hollywood"),
    "HW Gap: Hollywood Sign Blast": LocData(10200012, "Hollywood"),
    "HW Gap: Pin Plant": LocData(10200013, "Hollywood"),
    "HW Gap: Planter Pop": LocData(10200014, "Hollywood"),
    "HW Gap: Romperwood Spine": LocData(10200015, "Hollywood"),
    "HW Gap: Romperwood Transfer": LocData(10200016, "Hollywood"),
    "HW Gap: Schools Out": LocData(10200017, "Hollywood"),
    "HW Gap: Tony to Tony": LocData(10200018, "Hollywood"),
    "HW Gap: Velvet Rope": LocData(10200019, "Hollywood"),
    "HW Gap: Voodoo Spine": LocData(10200020, "Hollywood"),
    "HW Gap: Half Moon Grind": LocData(10200021, "Hollywood"),
    "HW Gap: Straight Outta Bronson": LocData(10200022, "Hollywood"),
    "HW Gap: Yellow": LocData(10200023, "Hollywood"),
    "HW Gap: FireEscape Level 3": LocData(10200024, "Hollywood"),
    "HW Gap: Record Deal": LocData(10200025, "Hollywood"),
    "HW Gap: Spinner": LocData(10200026, "Hollywood"),
    "HW Gap: Dump Up": LocData(10200027, "Hollywood"),
    "HW Gap: El Teniente Drop": LocData(10200028, "Hollywood"),
    "HW Gap: Romper Rail": LocData(10200029, "Hollywood"),
    "HW Gap: Bronson Backlog": LocData(10200030, "Hollywood"),
    "HW Gap: Trapdoor": LocData(10200031, "Hollywood"),
    "HW Gap: FireEscape Level4": LocData(10200032, "Hollywood"),
    "HW Gap: Goat Whackin'": LocData(10200033, "Hollywood"),
    "HW Gap: Manual the Stars": LocData(10200034, "Hollywood"),
    "HW Gap: Over vine": LocData(10200035, "Hollywood"),
    "HW Gap: FireEscape Level5": LocData(10200036, "Hollywood"),
    "HW Gap: Hollywood High Line": LocData(10200037, "Hollywood"),
    # Hollywood Buyables
        # Shirts
        "HW Shirt: Tanktop": LocData(10310001, "Hollywood"), 
        "HW Shirt: Sleeveless": LocData(10310002, "Hollywood"),
        "HW Shirt: T-shirt": LocData(10310003, "Hollywood"),
        "HW Shirt: Long Sleeve T": LocData(10310004, "Hollywood"),
        "HW Shirt: Layered T": LocData(10310005, "Hollywood"),  
        "HW Shirt: Military Coat": LocData(10310006, "Hollywood"), 
        "HW Shirt: Sweater": LocData(10310007, "Hollywood"),
        "HW Shirt: Hoody": LocData(10310008, "Hollywood"),
        "HW Shirt: Zip Up Hoody": LocData(10310009, "Hollywood"),
        "HW Shirt: Leather Vest": LocData(10310010, "Hollywood"), 
        "HW Shirt: Leather Jacket 1": LocData(10310011, "Hollywood"), 
        "HW Shirt: Leather Jacket 2": LocData(10310012, "Hollywood"),
        "HW Shirt: Sleeveless Denim": LocData(10310013, "Hollywood"),
        "HW Shirt: Vans Jersey": LocData(10310014, "Hollywood"),
        "HW Shirt: Hawk Hoody": LocData(10310015, "Hollywood"), 
        "HW Shirt: Hawk Thunder": LocData(10310016, "Hollywood"), 
        "HW Shirt: Quiksilver Button-up": LocData(10310017, "Hollywood"),
        "HW Shirt: Quiksilver Hoody 1": LocData(10310018, "Hollywood"),
        "HW Shirt: Electric Corpo": LocData(10310019, "Hollywood"),
        "HW Shirt: Electric Electroseal": LocData(10310020, "Hollywood"), 
        "HW Shirt: Electric Plasma": LocData(10310021, "Hollywood"), 
        "HW Shirt: Blind Bat Reaper Hoody": LocData(10310022, "Hollywood"),
        "HW Shirt: Nixon Shirt 2": LocData(10310023, "Hollywood"),
        "HW Shirt: Independent Stage 9 T": LocData(10310024, "Hollywood"),
        "HW Shirt: Von Zipper Hoody": LocData(10310025, "Hollywood"), 
        "HW Shirt: Sessions Standard Issue Hoody": LocData(10310026, "Hollywood"), 
        "HW Shirt: Volcom Hoody": LocData(10310027, "Hollywood"),
        "HW Shirt: Famous Stars and Straps Shirt 2": LocData(10310028, "Hollywood"),
        # Pants 
        "HW Pants: Jeans": LocData(10320001, "Hollywood"),
        "HW Pants: Tight Jeans": LocData(10320002, "Hollywood"),
        "HW Pants: Jeans Ripped": LocData(10320003, "Hollywood"),
        "HW Pants: Plaid Pants": LocData(10320004, "Hollywood"),
        "HW Pants: Cargo Pants": LocData(10320005, "Hollywood"),
        "HW Pants: Leather Pants": LocData(10320006, "Hollywood"),
        "HW Pants: Plaid Shorts": LocData(10320007, "Hollywood"),
        "HW Pants: Cargo Shorts": LocData(10320008, "Hollywood"),
        "HW Pants: Bunch Shorts": LocData(10320009, "Hollywood"),
        "HW Pants: Camo Shorts": LocData(10320010, "Hollywood"),
        "HW Pants: Quiksilver Jeans": LocData(10320011, "Hollywood"),
        "HW Pants: Baker Jeans": LocData(10320012, "Hollywood"),
        "HW Pants: Hurley Icon Jeans": LocData(10320013, "Hollywood"),
        "HW Pants: DVS Jeans": LocData(10320014, "Hollywood"),
        "HW Pants: DC Aidan DX Jeans": LocData(10320015, "Hollywood"),
        # Deck Graphics
        "HW Deck: Almost Mullen 10 Stair": LocData(10330001, "Hollywood"),
        "HW Deck: Almost Daewon Peace": LocData(10330002, "Hollywood"),
        "HW Deck: Alva Blue Tile": LocData(10330003, "Hollywood"),
        "HW Deck: Alva N": LocData(10330004, "Hollywood"),
        "HW Deck: Antihero Green": LocData(10330005, "Hollywood"),
        "HW Deck: Baker Brand Logo": LocData(10330006, "Hollywood"),
        "HW Deck: Birdhouse Compass": LocData(10330007, "Hollywood"),
        "HW Deck: Birdhouse Falcon Yellow": LocData(10330008, "Hollywood"),
        "HW Deck: Birdhouse Icon": LocData(10330009, "Hollywood"),
        "HW Deck: Blind Original": LocData(10330010, "Hollywood"),
        "HW Deck: 5Boro-Cinco Barrios": LocData(10330011, "Hollywood"),
        "HW Deck: DGK Ultra": LocData(10330012, "Hollywood"),
        "HW Deck: Element Mike v Big Series": LocData(10330013, "Hollywood"),
        "HW Deck: Element Section": LocData(10330014, "Hollywood"),
        "HW Deck: Hook Ups": LocData(10330015, "Hollywood"),
        "HW Deck: World Ind Vallely Animal Man": LocData(10330016, "Hollywood"),
        "HW Deck: World Ind Vallely Snake": LocData(10330017, "Hollywood"),
        "HW Deck: Plan B Team 3-D": LocData(10330018, "Hollywood"),
        "HW Deck: Powell Peralta Cab": LocData(10330019, "Hollywood"),
        "HW Deck: Powell Peralta Mullen": LocData(10330020, "Hollywood"),
        "HW Deck: RDS1": LocData(10330021, "Hollywood"),
        "HW Deck: The Firm Bobs Stencil": LocData(10330022, "Hollywood"),
        "HW Deck: World Industries 1": LocData(10330023, "Hollywood"),
        # Grip Tape
        "HW Grip Tape: Generic Cut": LocData(10340001, "Hollywood"),
        "HW Grip Tape: Solid": LocData(10340002, "Hollywood"),
        "HW Grip Tape: Razor's Edge": LocData(10340003, "Hollywood"),
        "HW Grip Tape: Equal": LocData(10340004, "Hollywood"),
        "HW Grip Tape: Slasher": LocData(10340005, "Hollywood"),
        "HW Grip Tape: Ye Old School": LocData(10340006, "Hollywood"),
        "HW Grip Tape: Hawk": LocData(10340007, "Hollywood"),
        # Elbow Pads
        "HW Elbow Pads: Elbow Pads": LocData(10350001, "Hollywood"),
        "HW Elbow Pads: Left Elbow Pad": LocData(10350002, "Hollywood"),
        "HW Elbow Pads: Right Elbow Pad": LocData(10350003, "Hollywood"),
        # Knee Pads
        "HW Knee Pads: ": LocData(10360001, "Hollywood"),
        # Shoes
        "HW Shoes: Skate Shoe 1": LocData(10370001, "Hollywood"),
        "HW Shoes: Combat Boots": LocData(10370002, "Hollywood"),
        "HW Shoes: Hi Tops": LocData(10370003, "Hollywood"),
        "HW Shoes: Hurley the Crown": LocData(10370004, "Hollywood"),
        "HW Shoes: Hurley Amp": LocData(10370005, "Hollywood"),
        "HW Shoes: Hurley Burnquist": LocData(10370006, "Hollywood"),
        "HW Shoes: DGK Workout Low - White on White": LocData(10370007, "Hollywood"),
        "HW Shoes: DGK Workout Low - Navy": LocData(10370008, "Hollywood"),
        "HW Shoes: DGK Williams": LocData(10370009, "Hollywood"),
        "HW Shoes: Globe Icon": LocData(10370010, "Hollywood"),
        "HW Shoes: Globe Finale": LocData(10370011, "Hollywood"),
        "HW Shoes: Globe Mullen Tensor": LocData(10370012, "Hollywood"),
        "HW Shoes: DVS Milan": LocData(10370013, "Hollywood"),
        "HW Shoes: DVS Kenyan": LocData(10370014, "Hollywood"),
        "HW Shoes: DVS Revival Splat": LocData(10370015, "Hollywood"),
        "HW Shoes: DVS Daewon": LocData(10370016, "Hollywood"),
        "HW Shoes: Vans Tony III TT/Fog": LocData(10370017, "Hollywood"),
        "HW Shoes: Vans Tony III Blk/Wht": LocData(10370018, "Hollywood"),
        "HW Shoes: Vans Tony III Grn/Blk": LocData(10370019, "Hollywood"),
        "HW Shoes: Vans Tony III Garg/Nvy": LocData(10370020, "Hollywood"),
        "HW Shoes: Vans Tony III Gry/Wht": LocData(10370021, "Hollywood"),
        "HW Shoes: Checkered": LocData(10370022, "Hollywood"),
        "HW Shoes: ES Anti-Social": LocData(10370023, "Hollywood"),
        "HW Shoes: ES K7": LocData(10370024, "Hollywood"),
        "HW Shoes: ES Accelerate": LocData(10370025, "Hollywood"),
        "HW Shoes: Emerica Crass": LocData(10370026, "Hollywood"),
        "HW Shoes: Emerica Felt": LocData(10370027, "Hollywood"),
        "HW Shoes: Emerica ReynoldS3": LocData(10370028, "Hollywood"),
        "HW Shoes: Etnies Bastien": LocData(10370029, "Hollywood"),
        "HW Shoes: Etnies Arto": LocData(10370030, "Hollywood"),
        "HW Shoes: Etnies Lo-cal": LocData(10370031, "Hollywood"),
        "HW Shoes: Quiksilver Hawk 1": LocData(10370032, "Hollywood"),
        "HW Shoes: Quiksilver Hawk 2": LocData(10370033, "Hollywood"),
        "HW Shoes: Adio Selego": LocData(10370034, "Hollywood"),
        "HW Shoes: Adio Jeremy Wray": LocData(10370035, "Hollywood"),
        "HW Shoes: Adio Brian Sumner": LocData(10370036, "Hollywood"),
        "HW Shoes: Adio Tony Hawk": LocData(10370037, "Hollywood"),
        "HW Shoes: Adio Viva Bam": LocData(10370038, "Hollywood"),
        "HW Shoes: Nike Airzoom 1": LocData(10370039, "Hollywood"),
        "HW Shoes: Nike Airzoom 2": LocData(10370040, "Hollywood"),
        "HW Shoes: DC Manteca": LocData(10370041, "Hollywood"),
        "HW Shoes: Element Fuji": LocData(10370042, "Hollywood"),
        # Socks
        "HW Socks: Knee High": LocData(10380001, "Hollywood"),
        "HW Socks: Medium": LocData(10380002, "Hollywood"),
        "HW Socks: Low": LocData(10380003, "Hollywood"),
        # Hair
        "HW Hair: Bald": LocData(10390001, "Hollywood"),
        "HW Hair: Buzzed": LocData(10390002, "Hollywood"),
        "HW Hair: Devil Lock": LocData(10390003, "Hollywood"),
        "HW Hair: Dead Guy Doo": LocData(10390004, "Hollywood"),
        "HW Hair: Mullet": LocData(10390005, "Hollywood"),
        "HW Hair: McSqueeb R": LocData(10390006, "Hollywood"),
        "HW Hair: McSqueeb L": LocData(10390007, "Hollywood"),
        "HW Hair: Mohawk A": LocData(10390008, "Hollywood"),
        "HW Hair: Mohawk B": LocData(10390009, "Hollywood"),
        "HW Hair: Liberty Spikes 1": LocData(10390010, "Hollywood"),
        "HW Hair: Liberty Spikes 2": LocData(10390011, "Hollywood"),
        "HW Hair: Spiked 1": LocData(10390012, "Hollywood"),
        "HW Hair: Spiked 2": LocData(10390013, "Hollywood"),
        "HW Hair: Fauxhawk": LocData(10390014, "Hollywood"),
        "HW Hair: Long": LocData(10390015, "Hollywood"),
        "HW Hair: Ponytail": LocData(10390016, "Hollywood"),
        "HW Hair: Afro": LocData(10390017, "Hollywood"),
        "HW Hair: Dreadlocks": LocData(10390018, "Hollywood"),
        "HW Hair: Pompadour": LocData(10390019, "Hollywood"),
        "HW Hair: Flat Top": LocData(10390020, "Hollywood"),
        "HW Hair: Pigtails": LocData(10390021, "Hollywood"),
        "HW Hair: Caesar": LocData(10390022, "Hollywood"),
        "HW Hair: Cornrows": LocData(10390023, "Hollywood"),
        "HW Hair: Medium": LocData(10390024, "Hollywood"),
        "HW Hair: Short": LocData(10390025, "Hollywood"),
}

#extra_locations = {
#    "ml7's house": LocData(20050102, "Sibiu"),
#}

# Like in Items.py, breaking up the different locations to help with organization and if something special needs to happen to them
Trex_locations = {
    "Smash the T-Rex": LocData(20050110, "Hollywood")
}

# Also like in Items.py, this collects all the dictionaries together
# Its important to note that locations MUST be bigger than progressive item count and should be bigger than total item count
# Its not here because this is an example and im not funny enough to think of more locations
# But important to note
location_table = {
    **THAW_locations,
    #**extra_locations,
    **Trex_locations
}