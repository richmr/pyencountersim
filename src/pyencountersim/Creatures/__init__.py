from pydantic import BaseModel, Field
from enum import Enum, auto
import warnings

from pyencountersim.dice import d20result, roll20
from pyencountersim.Weapons import WeaponTypes, DamageTypes

class Abilities(Enum):
    Str = "Str"
    Dex = "Dex"
    Int = "Int"
    Con = "Con"
    Wis = "Wis"
    Cha = "Cha"

class AbilityScoresType(BaseModel):
    Abilities.Str:int = Field(default=10)
    Abilities.Dex:int = Field(default=10)
    Abilities.Int:int = Field(default=10)
    Abilities.Con:int = Field(default=10)
    Abilities.Wis:int = Field(default=10)
    Abilities.Cha:int = Field(default=10)

class AbilityModsType(BaseModel):
    Abilities.Str:int = Field(default=0)
    Abilities.Dex:int = Field(default=0)
    Abilities.Int:int = Field(default=0)
    Abilities.Con:int = Field(default=0)
    Abilities.Wis:int = Field(default=0)
    Abilities.Cha:int = Field(default=0)

class SavingModsType(BaseModel):
    Abilities.Str:int = Field(default=0)
    Abilities.Dex:int = Field(default=0)
    Abilities.Int:int = Field(default=0)
    Abilities.Con:int = Field(default=0)
    Abilities.Wis:int = Field(default=0)
    Abilities.Cha:int = Field(default=0)

class CreatureStats(BaseModel):
    id:int
    name:str = Field(default="Creature")
    level:int = Field(default=1)
    AC:int = Field(default=10)
    HP:int = Field(default=0)
    Abilities:AbilityScoresType = Field(default=AbilityScoresType())
    AbilityMods:AbilityModsType = Field(default=AbilityModsType())
    SavingMods:SavingModsType = Field(default=SavingModsType())
    # Str:int = Field(default=10)
    # Str_mod:int = Field(default=0)
    # Str_savings_mod:int = Field(default=0)
    # Dex:int = Field(default=10)
    # Dex_mod:int = Field(default=0)
    # Dex_savings_mod:int = Field(default=0)
    # Con:int = Field(default=10)
    # Con_mod:int = Field(default=0)
    # Con_savings_mod:int = Field(default=0)
    # Int:int = Field(default=10)
    # Int_mod:int = Field(default=0)
    # Int_savings_mod:int = Field(default=0)
    # Wis:int = Field(default=10)
    # Wis_mod:int = Field(default=0)
    # Wis_savings_mod:int = Field(default=0)
    # Cha:int = Field(default=10)
    # Cha_mod:int = Field(default=0)
    # Cha_savings_mod:int = Field(default=0)


class Creature:

    _currentID = 0

    def __init__(self) -> None:
        self.base_state = CreatureStats(id=self._currentID)
        self.current_state = CreatureStats(id=self.base_state.id)
        self._currentID += 1
        self._startTurnStack = []
        self._endTurnStack = []
        self._target = None
        pass

    def takeTurn(self):
        pass

    def startTurn(self):
        pass

    def action(self):
        pass

    def move(self):
        pass

    def bonusAction(self):
        pass

    def reaction(self):
        pass

    #### Reactions

    """
    How are these going to work?  Many reactions snuff attacks or impose disadvantage or who knows what
    """

    def reactToMovement(self, creatureObj):
        pass

    def reactToMeleeAttack(self, attackerObj, targetObj):
        pass

    def reactToRangedAttack(self, attackerObj, targetObj):
        pass

    def reactToMagicAttack(self, attackerObj, targetObj):
        pass

    def reactToMagicGeneral(self, casterObj):
        pass

    def reactToCriticalHit(self, attackerObj):
        pass

    ####  Attack Success methods ####
    # These return True if the attack lands
    # Can be overridden as needed

    def hitByWeaponMelee(self, roll:d20result, weapon_type:WeaponTypes = WeaponTypes.Normal) -> bool:
        if roll.total >= self.current_state.AC:
            return True
        else:
            return False
        
    def hitByWeaponRanged(self, roll:d20result, weapon_type:WeaponTypes = WeaponTypes.Normal) -> bool:
        if roll.total >= self.current_state.AC:
            return True
        else:
            return False
        
    def hitByMagicAttackRoll(self, roll:d20result) -> bool:
        if roll.total >= self.current_state.AC:
            return True
        else:
            return False
        
    def hitByMagicSpell(self, spell:object) -> bool:
        # Here to allow for the possibility of something preventing it
        # TODO: Need to define the spell object 
        return True
    
    ### Damage receivers
    # Honestly not sure if I need anything else here

    def takeDamage(self, damage_amount:int, damage_type:DamageTypes) -> None:
        self.current_state.HP -= damage_amount

    ### Saving Throw

    def passSavingsThrow(self, saving_throw_type:Abilities, DC:int, allow_mod:bool = True) -> bool:
        result = roll20(self.current_state.SavingMods[saving_throw_type])
        check = result.raw
        if allow_mod:
            check = result.total
        if check >= DC:
            return True
        else:
            return False
    


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
