import re
import json
import numpy as np
import pandas as pd

def int2rom(n):
    '''Convert int to roman numeral str
    Works for under 40 
    (mag not currently used)'''
    mag = len(str(n)) #magnitude
    tens={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
    if n<11: return tens[n]
    else:
        s = str(n)
        tdig = 'X'*int(s[0])
        if s[1] == '0': return f'{tdig}'
        else:           return f'{tdig}{tens[int(s[1])]}'