#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
l = '/123'

def f(x):
    i = ord(x)
    if  i>=ord('0') and i<=ord('9'):
        return int(x)
    else:
        return 0
l = map(f,l)

print(reduce(lambda x,y:10*x + y ,l))
