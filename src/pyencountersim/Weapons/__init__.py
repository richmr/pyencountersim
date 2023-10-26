
from enum import Enum, auto
import warnings

from pyencountersim.Creatures import Creature 



"""
10/21/2023
Thoughts on attack objects
{
    "AttackType":[ WeaponMelee, WeaponRanged, MagicAuto, MagicTouch, MagicRanged, MagicSave ]
    "Save": [ None, Saving Type ]
    "SuccessfulSave": <callable object that takes 
}

Or not..  Leaning towards weapons, spells, etc having a method "attack" that takes as input the Creature object of the target
Then that attack method calls various methods on the Creature object to see if it hits, apply damage, and apply effects
The Creature object itself handles the logic of how it actually lands or effects.

Otherwise that attack object can get hopelessly confusing
"""


class TargetAffector:
    """
    All things that affect Creatures should use this as base class
    These can be attacks, heals, banes, boons
    """

    def __init__(self) -> None:
        # placeholder
        pass

    def affect(self, targetObj:Creature) -> None:
        """
        This method is intended to be overridden by spells or other things that affect Creatures
        The various methods of the Creature are called to apply effects
        """
        warnings.warn("Base 'TargetAffector.affect()' called.  This does nothing.", RuntimeWarning)
        return
    
    def attack(self, targetObj:Creature) -> None:
        """
        This method is intended to be overridden by weapons, spells, or other things that damage Creatures
        The various methods of the Creature are called to apply damage and effects

        Really no difference between this and 'affect' but called 'attack' for clarity of intent
        """
        warnings.warn("Base 'TargetAffector.attack()' called.  This does nothing.", RuntimeWarning)
        return    
    
