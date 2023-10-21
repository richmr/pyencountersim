from pydantic import BaseModel, Field

class CreatureStats(BaseModel):
    id:int
    name:str = Field(default="Creature")
    level:int = Field(default=1)
    AC:int = Field(default=10)
    HP:int = Field(default=0)
    Str:int = Field(default=10)
    Str_mod:int = Field(default=0)
    Str_savings_mod:int = Field(default=0)
    Dex:int = Field(default=10)
    Dex_mod:int = Field(default=0)
    Dex_savings_mod:int = Field(default=0)
    Con:int = Field(default=10)
    Con_mod:int = Field(default=0)
    Con_savings_mod:int = Field(default=0)
    Int:int = Field(default=10)
    Int_mod:int = Field(default=0)
    Int_savings_mod:int = Field(default=0)
    Wis:int = Field(default=10)
    Wis_mod:int = Field(default=0)
    Wis_savings_mod:int = Field(default=0)
    Cha:int = Field(default=10)
    Cha_mod:int = Field(default=0)
    Cha_savings_mod:int = Field(default=0)
    

class Creature:

    _currentID = 1

    def __init__(self) -> None:
        self.state = CreatureStats(id=self._currentID)
        self._currentID += 1
        self._startTurnStack = []
        self._endTurnStack = []
        self._target = None
        pass

    def takeTurn(self):
        pass

    def startTurn(self):
        pass

    def takeDamage(self, dmg_object):
        pass

    def action(self):
        pass

    def move(self):
        pass

    def bonusAction(self):
        pass

    def reaction(self):
        pass



