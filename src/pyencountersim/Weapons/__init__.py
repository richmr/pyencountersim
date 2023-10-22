
from enum import Enum, auto
import warnings

from pyencountersim.Creatures import Creature

class DamageTypes(Enum):
    Acid = auto()
    Bludgeoning = auto()
    Cold = auto()
    Fire = auto()
    Force = auto()
    Lightning = auto()
    Necrotic = auto()
    Piercing = auto()
    Poison = auto()
    Psychic = auto()
    Radiant = auto()
    Slashing = auto()
    Thunder = auto()

class WeaponTypes(Enum):
    Normal = auto()
    Magic = auto()
    ColdIron = auto()
    Silver = auto()

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


    
    
