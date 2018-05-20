# import keyword
import sys


# 第一个注释
print ("Hello, Python!") # 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

#行与缩进
#python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
#缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数

print("hello")
if True:
    {
        print("true")
    }
else:
    print("false")
print("-----")

str="tking.cn"
print(str)
print(str[0])
print(str[0:-1])
print(str[2:5])
print(str * 2)
print(str+"hello")
print("this " "is" " test")
print("hello\nnoob")
print(r"hello\nnoob")
print("------")

# input("\n\n按下enter后退出")
print("---")

x = "runoobqqqqq"; sys.stdout.write(x+"\n");

print("---")

print("不换行", end=" ")
print("yes")