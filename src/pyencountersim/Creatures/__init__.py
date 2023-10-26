from pydantic import BaseModel, Field
from enum import Enum, auto
import warnings

from pyencountersim.dice import d20result, roll20
from pyencountersim.Foundations import Abilities, AbilityModsType, AbilityScoresType, SavingModsType, WeaponTypes, DamageTypes


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
        self.initiative = 0
        pass

    def rollInitiative(self, addl_modifier:int = 0) -> int:
        total_mod = self.current_state.AbilityMods.Dex + addl_modifier
        roll_result = roll20(mod=total_mod)
        self.initiative = roll_result.total
        return roll_result.total
    
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
        result = roll20(getattr(self.current_state.SavingMods, saving_throw_type.value))
        check = result.raw
        if allow_mod:
            check = result.total
        if check >= DC:
            return True
        else:
            return False
    


