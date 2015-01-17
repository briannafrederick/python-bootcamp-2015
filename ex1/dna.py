dna = 'ATGATTTTTCCATCTTTAAGTGCGATACTGTTTTGT'
dna_bases = ['A', 'C', 'G', 'T']
rna_bases = ['A', 'C', 'G', 'U'] 
basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'} 

def is_dna(dna):
    """
    Checks whether a string is a DNA string.

    Parameters
    ----------
    dna : string
        A string (i.e., you can assume you get a string)

    Returns
    -------
    out : bool
        Returns True, if dna is a valid DNA string (i.e,
        a string composed of the letters 'A', 'C', 'G', or
        'T' (and False otherwise).

    Hint
    ----
    Use the builtin set function and set methods.

    Examples
    --------
    >>> is_dna('ATGATT')
    True
    >>> is_dna('ATGATU')
    False
    >>> is_dna('atgatt')
    False
    >>> is_dna('My grandMa')
    False
    """
    return NotImplemented

def is_rna(rna):
    """
    Checks whether a string is a DNA string.

    Parameters
    ----------
    rna : string
        A valid RNA string

    Returns
    -------
    out : bool
        Returns True, if rna is a valid RNA string (i.e,
        a string composed of the letters 'A', 'C', 'G', or
        'U' (and False otherwise).

    Hint
    ----
    See is_dna above.

    Examples
    --------
    >>> is_rna('ATGATT')
    False
    >>> is_rna('ATGATU')
    False
    >>> is_rna('atgatt')
    False
    >>> is_rna('AUGAUU')
    True
    >>> is_rna('CCCCCC')
    True
    """
    return NotImplemented

def transcribe(dna):
    """
    Transcribes a DNA string into a RNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string
        The RNA string is identical to the DNA string that
        it was transcribed from except all occurrences of
        the letter 'T' are replaced with the letter 'U'

    Hint
    ----
    Use a string method.

    Examples
    --------
    >>> transcribe('ATGATT')
     'AUGAUU'
    """
    return NotImplemented

def reverse(dna):
    """
    Return the DNA string in reverse order.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string

    Examples
    --------
    >>> reverse('ATGATT')
    'TTAGTA'
    """
    return NotImplemented

def complement(dna):
    """
    Return the complementary DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string

    Hint
    ----
    Try using list comprehension.  To join the elements of the list
    into a string try using the construct ''.join().

    Examples
    --------
    >>> complement('ATGATT')
    'TACTAA'
    """
    return NotImplemented

def is_complement(strand1, strand2):
    """
    Return the complementary DNA string.

    Parameters
    ----------
    strand1 : string
        A valid DNA string
    strand2 : string
        A valid DNA string

    Returns
    -------
    out : bool

    Hint
    ----
    You may want to use your complement function.

    Examples
    --------
    >>> is_complement('ATGATT', 'TACTAA')
    True
    >>> is_complement('ATGATT', 'TACTAT')
    False
    """
    return NotImplemented

def reversecomplement(dna):
    """
    Return the complement of the reverse of the DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string

    Hint
    ----
    Use function composition with functions you already defined.

    Examples
    --------
    >>> reversecomplement('TACTAA')
    'TTAGTA'
    """ 
    return NotImplemented

def gc_content(dna):
    """
    Return the proportion of Gs and Cs in the DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : float

    Hint
    ----
    It isn't necesary, but you can use the len function to get
    the length of a string.

    Examples
    --------
    >>> gc_content('TACTAA')
    0.16666666666666666
    """
    return NotImplemented

def get_codons(dna):
    """
    Return list of codons for the DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : list

    Hint
    ----
    You should check that the length of the string is divisible by 3
    (the modulus operator may be helpful).  Then go through the string
    grabbing three characters at time and appending them to a list.    

    Examples
    --------
    >>> get_codons('TACTAA')
    ['TAC', 'TAA']
    >>> get_codons('TACTA')
    Error: the string is not a multiple of 3.
    """
    return NotImplemented

if __name__ == "__main__":
    import doctest
    doctest.testmod()
