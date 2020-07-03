# 使用python代码解决生产中排产的可能组合的问题。该问题先以没有人员约束为起点，为任意数量
# 的釜来排产，举例来说排两个釜，可选择不同产品种类组合，每个釜只可以选择一个种类。起始版
# 本为列表版，后续版本课更新为字典版更为易读。

import itertools

#各个釜生产不同种类产品时的不同CRF，来源：capacity review表
crfR1 = [4,5.7,3.8]
crfR2 = [2]
crfR3 = [1.1,1.6]
crfR4 = [1.56]
crfR5 = [0.9]
crfR6 = [1.9]
crfR9 = [0.55]

#将CRF转化为单釜单日产能
def crftocap(a):
  return 24/a

#将每个釜的单釜单日产能存为列表
capR1 = list(map(crftocap,crfR1))
capR2 = list(map(crftocap,crfR2))
capR3 = list(map(crftocap,crfR3))
capR4 = list(map(crftocap,crfR4))
capR5 = list(map(crftocap,crfR5))
capR6 = list(map(crftocap,crfR6))
capR9 = list(map(crftocap,crfR9))

#total为全列表，用来供combinations做不同的组合，reactor为想开几个釜，zuhe为该情况下的开釜组合情况
total = [capR1,capR2,capR3,capR4,capR5,capR6,capR9]
reactor = int(input(print('请输入想排几个釜：')))
zuhe = itertools.combinations(total,reactor)

#根据开釜的组合，再从每个釜可以选择的产品种类来排列，算出每种组合的总产能
zuhecount = 0
capacity = []
for c in zuhe:
    d = itertools.product(*c)
    zuhecount+=1
    for i in d:
      sum = sumoftuple(i)
      print('以下为开',reactor,'个釜不同组合的第',zuhecount,'种反应釜组合的单日产能：','%.2f'%sum)
      capacity.append(sum)
print('单日产能介于%.2f和%.2f之间。'%(min(capacity),max(capacity)))



def sumoftuple(tuple):
  sum = 0
  for i in tuple:
    sum = sum + i
  return sum

 
