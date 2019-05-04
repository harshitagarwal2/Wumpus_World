#NAME:  Wumpus_1.py

from logic import *
from agents import *
from utils import *


################################################################################
print("STARTING TEST OF AIMA 3rd Ed LOGIC FUNCTIONS (CHAPS 7 TO 10)")
print()

### PropKB
def wumpus_1():
    kb = PropKB()
    kb.tell(expr("~P11"))
    print(kb.clauses)

    kb.tell(expr('P12 | P21 <=> B11'))
    print(kb.clauses)

    kb.tell(expr('P11 | P22 | P31  <=> B21'))
    print(kb.clauses)

    kb.tell(expr('~B11'))
    print(kb.clauses)

    kb.tell(expr('B21'))
    print(kb.clauses)

    print(tt_entails(expr('P & Q'), expr('Q')))

wumpus_1()