from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md

class EndGoal(Choice):
    """
    Determine the goal for the seed

    Smash the T-Rex: Break the T-rex and gain access to Beverly Hills. Should be a faster game suitable for syncs.
    Get to the Skate Ranch: Reach the Skate Ranch to win.
    Win the Skate Competition: Make it to downtown and Vans Park and win the Tony Hawk AMJAM.
    """
    display_name = "Victory Goal"
    option_smash_the_t_rex = 0
    option_get_to_the_skate_ranch = 1
    option_win_the_skate_competition = 2
    default = 0

class Tricks4Cash(DefaultOnToggle):
    """
    Makes the client read any landed combo above 2,000 points, divide it by 2,000, and then give you that much cash in exchange.
    A combo worth 20,000 points will give you 10 bucks, for example.
    I recommend leaving this on to cut down on grinding and give you ways to earn money besides doing tricks for the homeless man."""
    display_name = "Tricks 4 Cash" 

class Shopsanity(Toggle):
    """
    Makes every buyable item in the game a location check.
    If you haven't picked "Win the Skate Competition" or longer as a goal it will be on automatically because the world needs enough locations to give you all the stat items.
    """
    display_name = "Shopsanity" 

class ProgressiveWallet(DefaultOnToggle):
    """
    Adds progressive wallet items to the pool which initially restrict and then each increase how much money you can hold at a time.
    This does affect logic requirements and will often drip feed checks in a way that will make the archipelago multiworld flow more smoothly.
    It will however also mean that you may miss out on money at times or be forced to do more trips back and forth to the shops.
    This requires testing but may be a required feature in future.
    """
    display_name = "Progressive Wallet" 

#class ShopKeys(Toggle):
#    """
#    Adds shop key items to the pool which initially restrict and then allow access to each region's shops.
#    Hollywood does not have a shop key.
#    """
#    display_name = "Shop Keys" 

class IncludeSkateboardInItemPool(Toggle):
    """
    Adds the skateboard to the item pool, meaning if you don't have it you can't use your skateboard.
    Without the skateboard you can only do a few of the missions, mainly spraypainting.
    Turn this on at your own risk, because it may BK you very early and its a required item for most of the game. 
    """
    display_name = "Include Skateboard in Item Pool?"

class EnableDeathlinkOption(Choice):
    """
    Includes Deathlink, but also chooses how many bails it takes to trigger a sent deathlink.
    Keep in mind how fast these may rack up before your choice. It is possible to change this number later in client with "/deathlinksetting5" for example, or just turn it off or on with "/deathlink".
    At present it only sets you to bail or exit green-side balance meters for manuals, grinds, and lips.
    Perhaps later I'll find a way to make you bail no matter what you're doing, but we'll see.
    """
    display_name = "Enable Deathlink"
    option_deathlink_off = 0
    option_deathlink_on_1_bail = 1
    option_deathlink_on_5_bails = 2
    option_deathlink_on_10_bails = 3
    option_deathlink_on_15_bails = 4
    option_deathlink_on_20_bails = 5
    default = 0

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class THAWOptions(PerGameCommonOptions):
    end_goal: EndGoal
    tricks_4_cash: Tricks4Cash
    progressive_wallet: ProgressiveWallet
    shopsanity: Shopsanity
    #shop_keys: ShopKeys
    include_skateboard_in_item_pool: IncludeSkateboardInItemPool
    deathlink_choice: EnableDeathlinkOption

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [EndGoal, 
        Tricks4Cash],
    )
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "Quickplay": {
        "end_goal": EndGoal.option_smash_the_t_rex,
        "tricks_4_cash": True
    },
    #"the true way to play": {
    #    "hard_mode": True,
    #    "hammer": True,
    #    "extra_starting_chest": True,
    #    "start_with_one_confetti_cannon": True,
    #    "trap_chance": 50,
    #    "confetti_explosiveness": ConfettiExplosiveness.range_end,
    #    "player_sprite": PlayerSprite.option_duck,
    #},
}