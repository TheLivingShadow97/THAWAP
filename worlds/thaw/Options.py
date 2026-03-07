from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

# If youve ever gone to an options page and seen how sometimes options are grouped
# This is that
def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in THAW_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class VictoryCondition(Choice):
    """
    Determines your victory condition.
    When you grab choice you'll get the associated number.
    IE: If the player chooses the sewer then when you go to call StartingChapter you'll get 3
    When displaying the options names on the site, _ will become spaces and the word option will go away.
    """
    display_name = "Victory Condition"
    option_smash_the_t_rex = 1
    # option_get_to_the_skate_ranch = 2
    # option_win_a_skate_competition = 3
    # option_beat_the_game = 4
    default = 1

@dataclass
class THAWOptions(PerGameCommonOptions):
    VictoryCondition:            VictoryCondition

# This is where you organize your options
# Its entirely up to you how you want to organize it
THAW_option_groups: Dict[str, List[Any]] = {
    "Victory Options": [VictoryCondition],
}