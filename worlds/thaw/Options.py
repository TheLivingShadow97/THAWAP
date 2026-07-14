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
    """
    display_name = "Victory Goal"
    option_smash_the_t_rex = 0
    option_get_to_the_skate_ranch = 1
    default = 0

class Tricks4Cash(DefaultOnToggle):
    """
    Makes the client read any landed combo above 4,000 points, divide it by 4,000, and then give you that much cash in exchange.
    A combo worth 20,000 points will give you 5 bucks, for example.
    I recommend leaving this on to cut down on grinding and give you ways to earn money besides doing tricks for the homeless man."""
    display_name = "Tricks 4 Cash" 

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class THAWOptions(PerGameCommonOptions):
    end_goal: EndGoal
    tricks_4_cash: Tricks4Cash

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