''' revComp development file
'''

def revComp(nuclStr: str) -> str:
    ''' Given a nucleotide string as input, returns its reverse complement.
        >>>revComp('gattaca')
        'tgtaatc'
    '''
    # garbage filters
    assert isinstance(nuclStr, str),\
           'input must be a clean nucleotide string'
    badValues = isNucStrClean(nuclStr)
    assert not badValues,\
           f'bad values at:\n{badValues}.\n'
    # initialization
    outputStr, nuclStr = '', nuclStr.lower()
    complDict = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
    # implementation of algorithm
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    return outputStr
