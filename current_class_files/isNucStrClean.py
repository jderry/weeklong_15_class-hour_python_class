''' isNucStrClean development file
'''

def isNucStrClean(nuclStr: str) -> dict:
    ''' Returns bad values in dictionary as index:value pairs if they exist.
        Returns empty dictionary if nucleotide string is clean.
        Example:
        >>>isNucStrClean('gattaca')
        {}
        >>>isNucStrClean('gxttkca')
        {1: 'x', 4: 'k'}
    '''
    # garbage filter
    assert isinstance(nuclStr, str),\
           'input must be a string.'
    nuclStr = nuclStr.lower() # initialization
    badValues = {}
    # implementation of the algorithm
    for index, value in enumerate(nuclStr):
        if value not in 'acgt':
            badValues[index] = value
    return badValues
