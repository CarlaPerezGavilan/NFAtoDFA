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

    print('Alphabet:')
    print(alphabet)
    print('States:')
    print(states)

    # Make NFA delta table
    nfaTable = [ [0 for i in range(0, len(alphabet)) ] for j in range(0, len(states)) ]
    for tupple in nfa:
        tupple = tupple.split(',')
        col = states.index(tupple[1])
        row = alphabet.index(tupple[0])
        
        nfaTable[col][row] = tupple[2] if nfaTable[col][row] == 0 else nfaTable[col][row] + "" + tupple[2]
    print('NFA Table:')
    print(nfaTable)

    # Saves all possible combinations of states into array
    stateCombinations = []
    for i in range(1,len(states)):
      comb = combinations(states, i)
      stateCombinations += [''.join(i) for i in comb]
    stateCombinations.insert(0,'0')
    print('State Combinations:')
    print(stateCombinations)

    # Saves stateCombinations as indexes for usage in dfaTable
    stateCombinationsIndexes = []
    tmpStates = states.copy()
    tmpStates.insert(0,'0')
    for entry in stateCombinations:
        if len(entry) == 1:
            stateCombinationsIndexes.append([tmpStates.index(entry)])
        else:
            tmpArray = []
            i = 0
            while i < len(entry):
                tmpArray.append(tmpStates.index(entry[i]))
                i += 1
            stateCombinationsIndexes.append(tmpArray)
    print('State Combinations Indexes:')
    print(stateCombinationsIndexes)
            
    # Make NFA delta table
    dfaTable = []
    for index, entry in enumerate(stateCombinationsIndexes):
        if len(entry) == 1:
            if entry[0] == 0:
                dfaTable.append([0,0])
            else:
                tmpArray = []
                for alIdx in enumerate(alphabet):
                    tmpArray.append(nfaTable[index-1][alIdx[0]])
                dfaTable.append(tmpArray)
        else:
            tmpArray = []
            for alIdx in enumerate(alphabet):
                tmpString = ""
                for enIndex in entry:
                    if dfaTable[enIndex][alIdx[0]] != 0:
                        tmpString += str(dfaTable[enIndex][alIdx[0]])
                tmpArray.append(tmpString)
            dfaTable.append(tmpArray)
    print('DFA Table:')
    print(dfaTable)


if __name__ == "__main__":
    main()