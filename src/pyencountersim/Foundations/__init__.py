from pydantic import BaseModel, Field
from enum import Enum, auto

class Abilities(Enum):
    Str = "Str"
    Dex = "Dex"
    Int = "Int"
    Con = "Con"
    Wis = "Wis"
    Cha = "Cha"

class AbilityScoresType(BaseModel):
    Str:int = Field(default=10)
    Dex:int = Field(default=10)
    Int:int = Field(default=10)
    Con:int = Field(default=10)
    Wis:int = Field(default=10)
    Cha:int = Field(default=10)

class AbilityModsType(BaseModel):
    Str:int = Field(default=0)
    Dex:int = Field(default=0)
    Int:int = Field(default=0)
    Con:int = Field(default=0)
    Wis:int = Field(default=0)
    Cha:int = Field(default=0)

class SavingModsType(BaseModel):
    Str:int = Field(default=0)
    Dex:int = Field(default=0)
    Int:int = Field(default=0)
    Con:int = Field(default=0)
    Wis:int = Field(default=0)
    Cha:int = Field(default=0)

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
