

#求100以内的能被3 整除的数字
#
# for y in range (1,100):
#     if (y % 3 !=0):
#         continue
#     print(y)





# # 求两数字的商和余
# def j (b,f):
#     if (f==0):
#         print ("error")
#     else:
#         print(b % f,b // f)
#
# y = j(20,90)
# if y is None:
#     print ("error")
# else :
#     print("商为",[0],"余为",[1])
#


#九九乘法表
# for j in range (1,10):
#     for k in range (1,j+1):
#         print(j,"X",k,"=",j*k,end = "\t")
#     print()


#冒泡排序
# l=[31,545,76,87,8,54,2557,417,876,74,54]
# length = len(l)
# for k in range (length-1,0,-1):
#     for g in range (k): #本来是k+1，但是右边要交换两位元素
#         if l[g] > l[g+1]:
#             l[g],l[g+1] = l[g+1],l[g]
# print(l)


#不知道有多少参数，求传的参数的和
# def p (*args):
#     k=0
#     for s in (args):
#         k+=s
#     return k
# print(p(12,78,5,45))





  # class 用途
# class option():#定义类的名
#     a=None
#     b=None
#     res=None

#     def input(self,a,b):   #创建类，并调用
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
#
# c = option()  #实例调用类
# c.input(50,80)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()





#
# class option():
#     res=None
#
#     def __init__(self,a,b):   #魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
#
#
# c = option(98,45)
# c.sum()
# c.get_result()
#




# 冒泡排序
# l=[53,5,2,6,45,76,2,978,98,43,63]
#
# length = len(l)
# for h in range (length-1,0,-1):                 #外层循环确定排好序的数据下标
#     for g in range (h):                           #遍历未排好的列表
#         if (l[g] > l[g+1]):                         #判断相邻两个数据，前边的如果大于后边的，则交换两个数据的位置
#             l[g],l[g+1] = l[g+1],l[g]
# print(l)
#

# from dior.day01 import a,name,Test
#
# print(a)
# a="我是变量2的变量"
# def name():
#     print("我是变量2的变量")
# class test():
#     print("我是模块2中的类")
    # name = "我是模块2中的类"
# print(2006A.day1,2)
# print(Test.name)




果然是他是任何一条具有亏