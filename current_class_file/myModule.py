'''
'''

def isNuclStrClean(nuclStr: str) -> dict:
    ''' Given a nucleotide string, returns a dictionary of non-nucleotides and their positions in index:symbol pairs.
        An empty return dictionary means the string is clean.
        >>>isNuclStrClean('gattaxa')
        {5: 'x'}
    '''
    badValues = {}
    for index in range(len(nuclStr)):
        if nuclStr[index] not in 'ACGTacgt':
            badValues[index] = nuclStr[index]
    return badValues

def getGCcont(nuclStr: str) -> float:
    ''' Given a clean nucleotide string as input, returns the percent gc content.
        >>>getGCcont('gattaca')
        28.571428571428573
    '''
    nuclStr = nuclStr.lower()
    badValues = isNuclStrClean(nuclStr)
    assert not badValues, f"Non-nucleotide(s) found at index: value {badValues}"
    assert isinstance(nuclStr, str), "Input must be a clean nucleotide string."
    return 100 * (nuclStr.count('c') + nuclStr.count('g'))/ len(nuclStr)

def euclidGCD(natA: int, natB: int) -> int:
    ''' Returns the greatest common divisor of two natural numbers.
        >>>euclidGCD(53667, 25527)
        201
    '''
    assert (isinstance(natA, int) and natA > 0)\
       and (isinstance(natB, int) and natB > 0), "Input must be two natural numbers."
    while natB:
        natA, natB = natB, natA % natB
    return natA