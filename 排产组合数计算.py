# 为了解决排产组合问题，先解决一个近似的问题：
# 如果有n个数组，每个数组中有m[0],m[1],m[2]...m[n]个数，那么，所有可能的从任意个数的
# 数组中取一个数的组合有多少种？ 这是类似于我们的产能模型，在一条生产线上，我们可以排不
# 同的产品，不同的产品有不同的产能。不同的产能就是m，不同的生产线就是n。我可以选择排一
# 条生产线，也可以选择任意排2，3，4，...n条生产线；但在这些生产线里，我只可以选择排m种
# 产品种的一种。

# 由于没有涉及到具体的求解的组合是什么样子，而是求解组合的个数，那么问题求解的思路可使
# 用递推法来实现：
# 设选择n个数组时的方法数是f(n),每个数组中的元素数字个数为m[0],m[1]，...m[n],那么
# f(1)=m[0],只有一个数组，那么数组只有一种选法，就是它自己，它的组合数就是它自己含的
# 元素数。
# f(2)=f(1)+f(1)*m[1]+m[1]=f(1)+m[1]*(f(1)+1),因为加一组数组后，组合数多了两个部分，
# 第一个部分是这组数组本身自己的组合数，另一个部分是这个数组加入到之前的数组组合中产生
# 的组合数。即：
# f[n] = f[n-1] + m[n-1]*(f[n-1]+1)
# 由此递推出问题的解法，代码如下：



def combinenumber(inputarray):
  n = len(inputarray)
  m=[]
  for i in range(0,n):
    m.append(len(inputarray[i]))
  f = len(inputarray[0])
  for i in range(1,n):
    f = f+(f+1)*m[i]
  return f

#各条生产线生产不同种类产品时的不同CRF，来源：capacity review表
crfR1 = [4,5.7,3.8]
crfR2 = [2]
crfR3 = [1.1,1.6]
crfR4 = [1.56]
crfR5 = [0.9]
crfR6 = [1.9]
crfR9 = [0.55]

#将CRF转化为单生产线单日产能
def crftocap(a):
  return 24/a

#将每个釜的单生产线单日产能存为列表
capR1 = list(map(crftocap,crfR1))
capR2 = list(map(crftocap,crfR2))
capR3 = list(map(crftocap,crfR3))
capR4 = list(map(crftocap,crfR4))
capR5 = list(map(crftocap,crfR5))
capR6 = list(map(crftocap,crfR6))
capR9 = list(map(crftocap,crfR9))

#total为全列表，用来供combinations做不同的组合
total = [capR1,capR2,capR3,capR4,capR5,capR6,capR9]
# reactor = len(total)
b = combinenumber(total)
print(b)
