"""
In this exercise, you will create a Python class for creating simple
substitution ciphers.   You are free to implement the required functionality
however you would like, but I highly recommend using Python's string
maketrans() method.

Imagine that you want to replace all the lower case letters of the alphabet
with the corresponding letter of the reverse alphabet (i.e, you want to replace
a with z, b with y, c with x, d with w, and so on.)

First let's create a string of the lower case letters:

>>> alphabet = "abcdefghijklmnopqrstuvwxyz"

Now let's reverse the alphabet:

>>> alphabet[::-1]
'zyxwvutsrqponmlkjihgfedcba'
>>> key = alphabet[::-1]

You can now make a little translation table using maketrans by passing it a
string containing the characters you want to replace and anoter string with the
characters you them to be replaced by:

>>> import string
>>> translator = string.maketrans(alphabet, key)

Note that you can give it any characters you want not just letters.  But the
two strings that you call maketrans with must be the same length.

Now you can call the translate method of any string with the translation table
and it will return the translated message.

>>> msg = "hello"
>>> msg.translate(translator)
'svool'
>>> coded = msg.translate(translator)
>>> decoded = coded.translate(translator)
>>> decoded
'hello'
"""

import string

class Cipher(object):
    """
    >>> reverse = Cipher("reverse")
    >>> reverse.encrypt("hello")
    'svool'
    >>> reverse.decrypt("svool")
    'hello'
    >>> rot13 = Cipher("rot13")
    >>> rot13.encrypt("hello")
    'uryyb'
    >>> rot13.encrypt("abcdefghijklmnopqrstuvwxyz")
    'nopqrstuvwxyzabcdefghijklm'
    >>> rot13.isvalid("hello")
    True
    >>> rot13.isvalid("H3aff")
    False
    >>> hybrid = Cipher("hybrid")
    >>> hybrid.encrypt("abcdefghijklmnopqrstuvwxyz")
    'nmlkjihgfedcbazyxwvutsrqpo'
    """

    def __init__(self, mapping):
        """
        The constructor method.
        """
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        a = self.alphabet
        if mapping == "reverse":
            key = a[::-1]
        elif mapping == "rot13":
            key = a[13:] + a[:13]
        elif mapping == "hybrid":
            key = a[13::-1] + a[:13:-1]
        else:
            raise ValueError("Mapping must be 'reverse', 'rot13', or 'hybrid', was %s." % value)
        self.translator = string.maketrans(a, key)

    def isvalid(self, message):
        """
        Checks whether a string is a valid for this class.
    
        Parameters
        ----------
        message : string
            A string (i.e., you can assume you get a string)
    
        Returns
        -------
        out : bool
            Returns True, if message is only composed of letters
            in our alphabet (and False otherwise).
        """
        return set(message).issubset(set(self.alphabet))

    def encrypt(self, message):
        """
        Encrypt the message
    
        Parameters
        ----------
        message: string
            A string (i.e., you can assume you get a string)
    
        Returns
        -------
        out : string
        """
        return message.translate(self.translator)
  
    def decrypt(self, message):
        """
        Decrypt the message
    
        Parameters
        ----------
        message: string
            A string (i.e., you can assume you get a string)
    
        Returns
        -------
        out : string
        """
        return message.translate(self.translator)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
