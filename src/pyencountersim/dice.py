
import re
import random

def roll(roll_str:str) -> int:
    """
    Converts roll_str like 2d6+4 to a random roll result
    """
    regex = r"(\d+)d(\d+)((\+|-)(\d+))?"
    roll_match = re.match(regex, roll_str)
    if roll_match is None:
        raise ValueError(f"{roll_str} is not a valid roll string (i.e. 2d6+1)")
    
    qty = int(roll_match.group(1))
    base = int(roll_match.group(2))
    mod = roll_match.group(3)
    result = sum([random.randint(1,base) for i in range(qty)])
    if mod is not None:
        mod = int(mod)
        result = result + mod
    
    return result

def roll20(mod:int = 0) -> tuple:
    """
    Rolls a single d20.
    Returns a tuple with (raw, total) to allow for crit assessment
    """
    raw = random.randint(1,20)
    total = raw+mod
    return (raw, total)





