#! /usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

__author__ = 'predor'

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1,2)
   
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odds = itertools.takewhile(lambda x: x <= 2*N - 1,natuals)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    zf = itertools.cycle([1,-1])
    mapOdds = map(lambda x: 4.0/x*next(zf) , odds)
    # step 4: 求和:
    result = reduce(lambda x,y : x + y , mapOdds)
    return result

