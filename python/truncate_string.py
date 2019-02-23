'''

Create a one line function that takes three arguments (txt, txt_length, txt_suffix) and returns a truncated string.

txt: Original string.
txt_length: Truncated length limit.
txt_suffix: Optional suffix string parameter.
Truncated returned string length should adjust to passed length in parameters regardless of length of the suffix.
'''


def truncate(txt, txt_length, txt_suffix=''):
    return txt[:txt_length-len(txt_suffix)]+txt_suffix