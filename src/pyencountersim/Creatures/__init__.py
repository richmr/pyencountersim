from pydantic import BaseModel

class CreatureState(BaseModel):
    id:int
    name:str
    AC:int
    CurrentHP:int
    MaxHP:int



class Creature:

    _currentID = 1

    def __init__(self) -> None:
        self.state = CreatureState(id=self._currentID)
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



