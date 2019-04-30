#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:43:40 2019

@author: alexiapaige
"""

def check_characters(password, characters):
    '''Put your docstring here'''

    lower_str = string.ascii_lowercase
    upper_str = string.ascii_uppercase
    digits_str = string.digits
    punct_str = string.punctuation
    
    if lower_str in password:
        return True
    elif upper_str in password:
        return True
    elif digits_str in password:
        return True
    elif punct_str in password:
        return True
    else:
        return False
