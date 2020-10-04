"""
Created on Thu Oct  1 19:49:55 2020

@author: Emilio Popovits Blake
@author: Roberto Gervacio 
@author: Carla Perez Gavilan
"""


"""
1. Open file
2. Get string
3. 

"""

from itertools import combinations

def main():
    #file = open('')
    #nfa = file.read()

    nfa = "{(0,p,p),(0,p,q),(1,p,p),(0,q,r),(1,q,r),(0,r,s),(0,s,s),(1,s,s)}"

    # Trim nfa input string onto format: ["0,p,p", "0,p,q",...,"1,s,s"]
    nfa = nfa.replace('{', '').replace('}', '')
    nfa = nfa[1: len(nfa)-1]
    nfa = nfa.split('),(')
    print('Initial String:')
    print(nfa)

    alphabet = set()
    states = set()
    
    # Get complete alphabet and states from nfa string
    for tupple in nfa:
        tupple = tupple.split(',')
        alphabet.add(tupple[0])
        states.add(tupple[1])
        states.add(tupple[2])
    
    alphabet = list(alphabet)
    states = list(states)

    alphabet.sort()
    states.sort()

    # Make NFA delta table
    nfaTable = [ [0 for i in range(0, len(alphabet)) ] for j in range(0, len(states)) ]
    for tupple in nfa:
        tupple = tupple.split(',')
        col = states.index(tupple[1])
        row = alphabet.index(tupple[0])
        
        nfaTable[col][row] = tupple[2] if nfaTable[col][row] == 0 else nfaTable[col][row] + "" + tupple[2]
    print('NFA Table:')
    print(nfaTable)

    # dfaTable = [ [0 for i in range(0, len(alphabet)) ] for j in range(0, len(states)) ]

    # Saves all possible combinations of states into array
    stateCombinations = []
    for i in range(1,len(states)):
      comb = combinations(states, i)
      stateCombinations += [''.join(i) for i in comb]
    print('State Combinations:')
    print(stateCombinations)

    print('test')

if __name__ == "__main__":
    main()