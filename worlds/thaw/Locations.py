from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple, Optional

from BaseClasses import ItemClassification, Location

from .Options import EndGoal, THAWOptions

class THAWLocation(Location):
    game = "Tony Hawk's American Wasteland"

class THAWLocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]

THAW_hollywood_locations = {
    # You can take a peak at Types.py for more information but,
    # THAWLocData is code, region in this instance
    # Regions will be explained more in Regions.py
    # But just know that it's mostly about organization
    # Place locations together based on where they are in the game and what is needed to get there
    # Hollywood Stage 1 Missions
    "HW Mission: Change Your Look": THAWLocData(10100001, "Hollywood"),
    "HW Mission: Change Your Clothes": THAWLocData(10100002, "Hollywood"),
    "HW Mission: Learn to Caveman": THAWLocData(10100003, "Hollywood"),
    "HW Mission: Do a Sponsor Challenge": THAWLocData(10100004, "Hollywood"),
    "HW Mission: Kickflip Whofleck": THAWLocData(10100005, "Hollywood"),
    "HW Mission: Learn to Revert": THAWLocData(10100006, "Hollywood"),
    "HW Mission: Get Your Stuff Back": THAWLocData(10100007, "Hollywood"),
    "HW Mission: Get Into Beverly Hills": THAWLocData(10100008, "Hollywood"),
    "HW Mission: First Tagging Mission": THAWLocData(10150001, "Hollywood"),
    "HW Mission: Second Tagging Mission": THAWLocData(10150002, "Hollywood"),
    "HW Mission: Third Tagging Mission": THAWLocData(10150003, "Hollywood"),
    "HW Mission: Fourth Tagging Mission": THAWLocData(10150004, "Hollywood"),
    "HW Mission: Fifth Tagging Mission": THAWLocData(10150005, "Hollywood"),
    # Hollywood Gaps
    "HW Gap: Bench2Bench": THAWLocData(10200001, "Hollywood"),
    "HW Gap: FireEscape Level1": THAWLocData(10200002, "Hollywood"),
    "HW Gap: Hollywood High Steps": THAWLocData(10200003, "Hollywood"),
    "HW Gap: Planter2Planter": THAWLocData(10200004, "Hollywood"),
    "HW Gap: Rail2Bleacher": THAWLocData(10200005, "Hollywood"),
    "HW Gap: Rail2Rail": THAWLocData(10200006, "Hollywood"),
    "HW Gap: Bleacher Hop": THAWLocData(10200007, "Hollywood"),
    "HW Gap: Car Hop": THAWLocData(10200008, "Hollywood"),
    "HW Gap: Chinese Transfer": THAWLocData(10200009, "Hollywood"),
    "HW Gap: El Teniente Spine": THAWLocData(10200010, "Hollywood"),
    "HW Gap: FireEscape Level2": THAWLocData(10200011, "Hollywood"),
    "HW Gap: Hollywood Sign Blast": THAWLocData(10200012, "Hollywood"),
    "HW Gap: Pin Plant": THAWLocData(10200013, "Hollywood"),
    "HW Gap: Planter Pop": THAWLocData(10200014, "Hollywood"),
    "HW Gap: Romperwood Spine": THAWLocData(10200015, "Hollywood"),
    "HW Gap: Romperwood Transfer": THAWLocData(10200016, "Hollywood"),
    "HW Gap: Schools Out": THAWLocData(10200017, "Hollywood"),
    "HW Gap: Tony to Tony": THAWLocData(10200018, "Hollywood"),
    "HW Gap: Velvet Rope": THAWLocData(10200019, "Hollywood"),
    "HW Gap: Voodoo Spine": THAWLocData(10200020, "Hollywood"),
    "HW Gap: Half Moon Grind": THAWLocData(10200021, "Hollywood"),
    "HW Gap: Straight Outta Bronson": THAWLocData(10200022, "Hollywood"),
    "HW Gap: Yellow": THAWLocData(10200023, "Hollywood"),
    "HW Gap: FireEscape Level 3": THAWLocData(10200024, "Hollywood"),
    "HW Gap: Record Deal": THAWLocData(10200025, "Hollywood"),
    "HW Gap: Spinner": THAWLocData(10200026, "Hollywood"),
    "HW Gap: Dump Up": THAWLocData(10200027, "Hollywood"),
    "HW Gap: El Teniente Drop": THAWLocData(10200028, "Hollywood"),
    "HW Gap: Romper Rail": THAWLocData(10200029, "Hollywood"),
    "HW Gap: Bronson Backlog": THAWLocData(10200030, "Hollywood"),
    "HW Gap: Trapdoor": THAWLocData(10200031, "Hollywood"),
    "HW Gap: FireEscape Level4": THAWLocData(10200032, "Hollywood"),
    "HW Gap: Goat Whackin'": THAWLocData(10200033, "Hollywood"),
    "HW Gap: Manual the Stars": THAWLocData(10200034, "Hollywood"),
    "HW Gap: Over vine": THAWLocData(10200035, "Hollywood"),
    "HW Gap: FireEscape Level5": THAWLocData(10200036, "Hollywood"),
    "HW Gap: Hollywood High Line": THAWLocData(10200037, "Hollywood"),
    # Hollywood Buyables
        # Shirts
        "HW Shirt: Tanktop": THAWLocData(10310001, "Hollywood"), 
        "HW Shirt: Sleeveless": THAWLocData(10310002, "Hollywood"),
        "HW Shirt: T-shirt": THAWLocData(10310003, "Hollywood"),
        "HW Shirt: Long Sleeve T": THAWLocData(10310004, "Hollywood"),
        "HW Shirt: Layered T": THAWLocData(10310005, "Hollywood"),  
        "HW Shirt: Military Coat": THAWLocData(10310006, "Hollywood"), 
        "HW Shirt: Sweater": THAWLocData(10310007, "Hollywood"),
        "HW Shirt: Hoody": THAWLocData(10310008, "Hollywood"),
        "HW Shirt: Zip Up Hoody": THAWLocData(10310009, "Hollywood"),
        "HW Shirt: Leather Vest": THAWLocData(10310010, "Hollywood"), 
        "HW Shirt: Leather Jacket 1": THAWLocData(10310011, "Hollywood"), 
        "HW Shirt: Leather Jacket 2": THAWLocData(10310012, "Hollywood"),
        "HW Shirt: Sleeveless Denim": THAWLocData(10310013, "Hollywood"),
        "HW Shirt: Vans Jersey": THAWLocData(10310014, "Hollywood"),
        "HW Shirt: Hawk Hoody": THAWLocData(10310015, "Hollywood"), 
        "HW Shirt: Hawk Thunder": THAWLocData(10310016, "Hollywood"), 
        "HW Shirt: Quiksilver Button-up": THAWLocData(10310017, "Hollywood"),
        "HW Shirt: Quiksilver Hoody 1": THAWLocData(10310018, "Hollywood"),
        "HW Shirt: Electric Corpo": THAWLocData(10310019, "Hollywood"),
        "HW Shirt: Electric Electroseal": THAWLocData(10310020, "Hollywood"), 
        "HW Shirt: Electric Plasma": THAWLocData(10310021, "Hollywood"), 
        "HW Shirt: Blind Bat Reaper Hoody": THAWLocData(10310022, "Hollywood"),
        "HW Shirt: Nixon Shirt 2": THAWLocData(10310023, "Hollywood"),
        "HW Shirt: Independent Stage 9 T": THAWLocData(10310024, "Hollywood"),
        "HW Shirt: Von Zipper Hoody": THAWLocData(10310025, "Hollywood"), 
        "HW Shirt: Sessions Standard Issue Hoody": THAWLocData(10310026, "Hollywood"), 
        "HW Shirt: Volcom Hoody": THAWLocData(10310027, "Hollywood"),
        "HW Shirt: Famous Stars and Straps Shirt 2": THAWLocData(10310028, "Hollywood"),
        # Pants 
        "HW Pants: Jeans": THAWLocData(10320001, "Hollywood"),
        "HW Pants: Tight Jeans": THAWLocData(10320002, "Hollywood"),
        "HW Pants: Jeans Ripped": THAWLocData(10320003, "Hollywood"),
        "HW Pants: Plaid Pants": THAWLocData(10320004, "Hollywood"),
        "HW Pants: Cargo Pants": THAWLocData(10320005, "Hollywood"),
        "HW Pants: Leather Pants": THAWLocData(10320006, "Hollywood"),
        "HW Pants: Plaid Shorts": THAWLocData(10320007, "Hollywood"),
        "HW Pants: Cargo Shorts": THAWLocData(10320008, "Hollywood"),
        "HW Pants: Bunch Shorts": THAWLocData(10320009, "Hollywood"),
        "HW Pants: Camo Shorts": THAWLocData(10320010, "Hollywood"),
        "HW Pants: Quiksilver Jeans": THAWLocData(10320011, "Hollywood"),
        "HW Pants: Baker Jeans": THAWLocData(10320012, "Hollywood"),
        "HW Pants: Hurley Icon Jeans": THAWLocData(10320013, "Hollywood"),
        "HW Pants: DVS Jeans": THAWLocData(10320014, "Hollywood"),
        "HW Pants: DC Aidan DX Jeans": THAWLocData(10320015, "Hollywood"),
        # Deck Graphics
        "HW Deck: Almost Mullen 10 Stair": THAWLocData(10330001, "Hollywood"),
        "HW Deck: Almost Daewon Peace": THAWLocData(10330002, "Hollywood"),
        "HW Deck: Alva Blue Tile": THAWLocData(10330003, "Hollywood"),
        "HW Deck: Alva N": THAWLocData(10330004, "Hollywood"),
        "HW Deck: Antihero Green": THAWLocData(10330005, "Hollywood"),
        "HW Deck: Baker Brand Logo": THAWLocData(10330006, "Hollywood"),
        "HW Deck: Birdhouse Compass": THAWLocData(10330007, "Hollywood"),
        "HW Deck: Birdhouse Falcon Yellow": THAWLocData(10330008, "Hollywood"),
        "HW Deck: Birdhouse Icon": THAWLocData(10330009, "Hollywood"),
        "HW Deck: Blind Original": THAWLocData(10330010, "Hollywood"),
        "HW Deck: 5Boro-Cinco Barrios": THAWLocData(10330011, "Hollywood"),
        "HW Deck: DGK Ultra": THAWLocData(10330012, "Hollywood"),
        "HW Deck: Element Mike v Big Series": THAWLocData(10330013, "Hollywood"),
        "HW Deck: Element Section": THAWLocData(10330014, "Hollywood"),
        "HW Deck: Hook Ups": THAWLocData(10330015, "Hollywood"),
        "HW Deck: World Ind Vallely Animal Man": THAWLocData(10330016, "Hollywood"),
        "HW Deck: World Ind Vallely Snake": THAWLocData(10330017, "Hollywood"),
        "HW Deck: Plan B Team 3-D": THAWLocData(10330018, "Hollywood"),
        "HW Deck: Powell Peralta Cab": THAWLocData(10330019, "Hollywood"),
        "HW Deck: Powell Peralta Mullen": THAWLocData(10330020, "Hollywood"),
        "HW Deck: RDS1": THAWLocData(10330021, "Hollywood"),
        "HW Deck: The Firm Bobs Stencil": THAWLocData(10330022, "Hollywood"),
        "HW Deck: World Industries 1": THAWLocData(10330023, "Hollywood"),
        # Grip Tape
        "HW Grip Tape: Generic Cut": THAWLocData(10340001, "Hollywood"),
        "HW Grip Tape: Solid": THAWLocData(10340002, "Hollywood"),
        "HW Grip Tape: Razor's Edge": THAWLocData(10340003, "Hollywood"),
        "HW Grip Tape: Equal": THAWLocData(10340004, "Hollywood"),
        "HW Grip Tape: Slasher": THAWLocData(10340005, "Hollywood"),
        "HW Grip Tape: Ye Old School": THAWLocData(10340006, "Hollywood"),
        "HW Grip Tape: Hawk": THAWLocData(10340007, "Hollywood"),
        # Elbow Pads
        "HW Elbow Pads: Elbow Pads": THAWLocData(10350001, "Hollywood"),
        "HW Elbow Pads: Left Elbow Pad": THAWLocData(10350002, "Hollywood"),
        "HW Elbow Pads: Right Elbow Pad": THAWLocData(10350003, "Hollywood"),
        # Knee Pads
        "HW Knee Pads: ": THAWLocData(10360001, "Hollywood"),
        # Shoes
        "HW Shoes: Skate Shoe 1": THAWLocData(10370001, "Hollywood"),
        "HW Shoes: Combat Boots": THAWLocData(10370002, "Hollywood"),
        "HW Shoes: Hi Tops": THAWLocData(10370003, "Hollywood"),
        "HW Shoes: Hurley the Crown": THAWLocData(10370004, "Hollywood"),
        "HW Shoes: Hurley Amp": THAWLocData(10370005, "Hollywood"),
        "HW Shoes: Hurley Burnquist": THAWLocData(10370006, "Hollywood"),
        "HW Shoes: DGK Workout Low - White on White": THAWLocData(10370007, "Hollywood"),
        "HW Shoes: DGK Workout Low - Navy": THAWLocData(10370008, "Hollywood"),
        "HW Shoes: DGK Williams": THAWLocData(10370009, "Hollywood"),
        "HW Shoes: Globe Icon": THAWLocData(10370010, "Hollywood"),
        "HW Shoes: Globe Finale": THAWLocData(10370011, "Hollywood"),
        "HW Shoes: Globe Mullen Tensor": THAWLocData(10370012, "Hollywood"),
        "HW Shoes: DVS Milan": THAWLocData(10370013, "Hollywood"),
        "HW Shoes: DVS Kenyan": THAWLocData(10370014, "Hollywood"),
        "HW Shoes: DVS Revival Splat": THAWLocData(10370015, "Hollywood"),
        "HW Shoes: DVS Daewon": THAWLocData(10370016, "Hollywood"),
        "HW Shoes: Vans Tony III TT/Fog": THAWLocData(10370017, "Hollywood"),
        "HW Shoes: Vans Tony III Blk/Wht": THAWLocData(10370018, "Hollywood"),
        "HW Shoes: Vans Tony III Grn/Blk": THAWLocData(10370019, "Hollywood"),
        "HW Shoes: Vans Tony III Garg/Nvy": THAWLocData(10370020, "Hollywood"),
        "HW Shoes: Vans Tony III Gry/Wht": THAWLocData(10370021, "Hollywood"),
        "HW Shoes: Checkered": THAWLocData(10370022, "Hollywood"),
        "HW Shoes: ES Anti-Social": THAWLocData(10370023, "Hollywood"),
        "HW Shoes: ES K7": THAWLocData(10370024, "Hollywood"),
        "HW Shoes: ES Accelerate": THAWLocData(10370025, "Hollywood"),
        "HW Shoes: Emerica Crass": THAWLocData(10370026, "Hollywood"),
        "HW Shoes: Emerica Felt": THAWLocData(10370027, "Hollywood"),
        "HW Shoes: Emerica ReynoldS3": THAWLocData(10370028, "Hollywood"),
        "HW Shoes: Etnies Bastien": THAWLocData(10370029, "Hollywood"),
        "HW Shoes: Etnies Arto": THAWLocData(10370030, "Hollywood"),
        "HW Shoes: Etnies Lo-cal": THAWLocData(10370031, "Hollywood"),
        "HW Shoes: Quiksilver Hawk 1": THAWLocData(10370032, "Hollywood"),
        "HW Shoes: Quiksilver Hawk 2": THAWLocData(10370033, "Hollywood"),
        "HW Shoes: Adio Selego": THAWLocData(10370034, "Hollywood"),
        "HW Shoes: Adio Jeremy Wray": THAWLocData(10370035, "Hollywood"),
        "HW Shoes: Adio Brian Sumner": THAWLocData(10370036, "Hollywood"),
        "HW Shoes: Adio Tony Hawk": THAWLocData(10370037, "Hollywood"),
        "HW Shoes: Adio Viva Bam": THAWLocData(10370038, "Hollywood"),
        "HW Shoes: Nike Airzoom 1": THAWLocData(10370039, "Hollywood"),
        "HW Shoes: Nike Airzoom 2": THAWLocData(10370040, "Hollywood"),
        "HW Shoes: DC Manteca": THAWLocData(10370041, "Hollywood"),
        "HW Shoes: Element Fuji": THAWLocData(10370042, "Hollywood"),
        # Socks
        "HW Socks: Knee High": THAWLocData(10380001, "Hollywood"),
        "HW Socks: Medium": THAWLocData(10380002, "Hollywood"),
        "HW Socks: Low": THAWLocData(10380003, "Hollywood"),
        # Hair
        "HW Hair: Bald": THAWLocData(10390001, "Hollywood"),
        "HW Hair: Buzzed": THAWLocData(10390002, "Hollywood"),
        "HW Hair: Devil Lock": THAWLocData(10390003, "Hollywood"),
        "HW Hair: Dead Guy Doo": THAWLocData(10390004, "Hollywood"),
        "HW Hair: Mullet": THAWLocData(10390005, "Hollywood"),
        "HW Hair: McSqueeb R": THAWLocData(10390006, "Hollywood"),
        "HW Hair: McSqueeb L": THAWLocData(10390007, "Hollywood"),
        "HW Hair: Mohawk A": THAWLocData(10390008, "Hollywood"),
        "HW Hair: Mohawk B": THAWLocData(10390009, "Hollywood"),
        "HW Hair: Liberty Spikes 1": THAWLocData(10390010, "Hollywood"),
        "HW Hair: Liberty Spikes 2": THAWLocData(10390011, "Hollywood"),
        "HW Hair: Spiked 1": THAWLocData(10390012, "Hollywood"),
        "HW Hair: Spiked 2": THAWLocData(10390013, "Hollywood"),
        "HW Hair: Fauxhawk": THAWLocData(10390014, "Hollywood"),
        "HW Hair: Long": THAWLocData(10390015, "Hollywood"),
        "HW Hair: Ponytail": THAWLocData(10390016, "Hollywood"),
        "HW Hair: Afro": THAWLocData(10390017, "Hollywood"),
        "HW Hair: Dreadlocks": THAWLocData(10390018, "Hollywood"),
        "HW Hair: Pompadour": THAWLocData(10390019, "Hollywood"),
        "HW Hair: Flat Top": THAWLocData(10390020, "Hollywood"),
        "HW Hair: Pigtails": THAWLocData(10390021, "Hollywood"),
        "HW Hair: Caesar": THAWLocData(10390022, "Hollywood"),
        "HW Hair: Cornrows": THAWLocData(10390023, "Hollywood"),
        "HW Hair: Medium": THAWLocData(10390024, "Hollywood"),
        "HW Hair: Short": THAWLocData(10390025, "Hollywood"),
}

endgoal_t_rex_locations = {
    "Smash the T-Rex": THAWLocData(None, "Hollywood")
}

all_location_table = {
    **THAW_hollywood_locations,
    **endgoal_t_rex_locations
}

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
# Location IDs don't need to be sequential, as long as they're unique and greater than 0.

def setup_locations(options: THAWOptions):
    temp_location_table = {}
    if options.EndGoal == EndGoal.option_smash_the_t_rex:
        temp_location_table.update({**endgoal_t_rex_locations})
    temp_location_table.update({**THAW_hollywood_locations})
    return temp_location_table