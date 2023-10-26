from pyencountersim.Creatures import CreatureStats
from pyencountersim.Foundations import Abilities

def test_default_stat_load():
    cs = CreatureStats(id=1)
    assert getattr(cs.Abilities, "Str") == 10
    assert getattr(cs.AbilityMods, "Cha") == 0
    assert getattr(cs.SavingMods, "Dex") == 0

