#! /usr/bin/env python3
# -*- coding: utf-8 -*-

answers = ['a','b','c','d']
allanswers = []
#有10题 先创建所有答案 答案  有 4 _10 个可能结果
#递归方式创建所有答案
def createAnswers(x = 0,tempAn = []):
    if x == 0:
        tempAn = []
    if x == 10:
        return
    for i in range(4):
        tempAn = tempAn[0:x]
        tempAn.append(answers[i])
        createAnswers(x+1,tempAn)
        if x == 9:
            allanswers.append(tempAn)

createAnswers()

print(len(allanswers))
print(pow(4,10))



matchAnswers = []


#获取重复最多的答案的个数
def getmaxCount(an):
    nums = [0,0,0,0]
    for a in an:
        index = abs(ord('a') - ord(a))
        v = nums[index] + 1
        nums[index] = v
    
    return max(nums)
#获取重复最少的答案的个数
def getminCount(an):
    nums = [0,0,0,0]
    for a in an:
        index = abs(ord('a') - ord(a))
        v = nums[index] + 1
        nums[index] = v
    
    return min(nums)

#获取重复最少的答案
def getminZiMu(an):
    nums = [0,0,0,0]
    for a in an:
        index = ord(a) - ord('a')
        nums[index] += 1
    
    return answers[nums.index(min(nums))]


#题2
def func2(an):
    return ( an[4] == 'c' and  an[1] == 'a' ) or (an[4] == 'd' and an[1] == 'b') or \
            (an[4] == 'a' and an[1] == 'c') or (an[4] == 'b' and an[1] == 'd')
#
def func3(an):
    return   ( an[2] == 'a' and  an[5] == an[1] == an[3] !=  an[2] ) or ( an[2] == 'b' and an[2] == an[1] == an[3] !=  an[5] ) \
            or ( an[2] == 'c' and an[5] == an[2] == an[3] !=  an[1]  ) or (an[2] == 'd' and an[5] == an[1] == an[2] !=  an[3])

def func4(an):
    return (an[3]=='a' and an[0] == an[4]) or (an[3]=='b' and an[1] == an[6]) or \
            ( an[3]=='c' and an[0] == an[8]) or (an[3]=='d' and an[5] == an[9])

def func5(an):
    return (an[4] == an[7]  == 'a') or (an[4] == an[3]  == 'b') or \
            (an[4] == an[8]  == 'c') or (an[4] == an[6]  == 'd')

def func6(an):
    return (an[1] == an[3] == an[7] and an[5] == 'a') or (an[0] == an[5] == an[7] and an[5] == 'b') or \
            (an[2] == an[9] == an[7] and an[5] == 'c') or (an[4] == an[8] == an[7] and an[5] == 'd')

def func7(an):
    return (getminZiMu(an) == 'c' and an[6] == 'a') or  (getminZiMu(an) == 'b' and an[6] == 'b') or \
            (getminZiMu(an) == 'a' and an[6] == 'c') or (getminZiMu(an) == 'd' and an[6] == 'd')

def func8(an):
     return (abs(ord(an[0]) - ord(an[6])) != 1 and an[7] == 'a') or (abs(ord(an[0]) - ord(an[4])) != 1 and an[7] == 'b') or \
             (abs(ord(an[0]) - ord(an[1])) != 1 and an[7] == 'c') or (abs(ord(an[0]) - ord(an[9])) != 1 and an[7] == 'd')

def func9(an):
      t1 = (an[0] == an[5])
      equalT1 = lambda x: an[x] != an[4]
      return (an[8] == 'a' and  t1 == equalT1(5)) or (an[8] == 'b' and  t1 == equalT1(9)) or \
              (an[8] == 'a' and  ti == equalT1(1)) or (an[8] == 'a' and  ti == equalT1(8))



def func10(an):
    value = getmaxCount(an) - getminCount(an)
    return ( value == 3) or  (value == 2) or  (value == 4) or  (value == 1)


for an in allanswers:
    #遍历所有答案 满足所有条件
    if func2(an) and func3(an) and func4(an) and  func5(an) and func6(an) and func7(an) and func8(an)   and func9(an) and func10(an):
        matchAnswers.append(an)
    
    

print('可能的结果%d'%len(matchAnswers))
for ans in matchAnswers:
    print(ans)
#['b', 'c', 'a', 'c', 'a', 'c', 'd', 'a', 'b', 'a']

