''' this is a module.
'''
def percentGCcontent(nuclStr: str) -> float:
    ''' Given a nucleotide string, return its percent G-G content.
        Example:
        >>>percentGCcontent('GATTACA')
        28.57142857142857
    '''
    # garbage filters
    assert isinstance(nuclStr, str),\
           'input must be a clean nucleotide string'
    badValues = isNucStrClean(nuclStr)
    assert not badValues,\
           f'bad values at:\n{badValues}.\n'
    # initialization
    nuclStr = nuclStr.lower() # lowercase nucleotides
    return 100 * (nuclStr.count('c') + nuclStr.count('g')) / len(nuclStr)
