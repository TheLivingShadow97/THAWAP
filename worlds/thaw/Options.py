from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

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

    Smash the T-Rex: Break the T-rex and gain access to Bevely Hills. Should be a faster game suitable for syncs.
    Get to the Skate Ranch: Reach the Skate Ranch to win. THIS DOES NOT WORK YET! DO NOT USE THIS OPTION!
    """
    display_name = "Victory Goal"
    option_smash_the_t_rex = 0
    option_get_to_the_skate_ranch = 1
    default = 0

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class THAWOptions(PerGameCommonOptions):
    end_goal: EndGoal


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [EndGoal],
    )
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "Quickplay": {
        "end_goal": EndGoal.option_smash_the_t_rex,
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