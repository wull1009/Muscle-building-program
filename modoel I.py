import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
#模型一
# 定义model变量
w = [45]
min = 10000
max = 18550  # 18-29岁最大2650kcal每天，即18550每周
c = [0]
alpha = 1/8000  # 每8000kcal增加体重1kg
c[0] = 10000  # 成年人每周需要摄入12600-14000卡,即1800-2000每天
beta = alpha*c[0]/w[0] # c[0]/w[0]是每周每公斤；那每天的基本代谢速率就是c[0]/w[0] *45/7
a = (beta/alpha) * w[0] + 1/alpha
k=0
while (w[k]<55):
    if(c[k]<18550):
        x = a + beta/alpha * k
        if(x>18550):
            c.append(18550)
            print("18500le")

            w.append(w[k] + alpha * c[k + 1] - beta * w[k])
            k = k + 1
            continue
        c.append(x)
        w.append(w[0]+k)
        beta = alpha * (c[0] / w[0] + 10 * k)  # 体重每增加1kg 基础代谢速率增加70kcal（每周）
    if (c[k] == 18550) :
        c.append(18550)
        w.append(w[k]+alpha*c[k+1]-beta*w[k])
        beta=alpha * (c[0] / w[0] + 10 * (w[k+1]-w[k]))
    k=k+1

print("第一阶段用时：" + str(k) + "周,第"+ str(k)+"周周末体重"+str(w[k]))
print(k)
print(c)
print(w)
# test=pd.DataFrame(c,w)
# test.to_csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv")

import pandas as pd
#模型一
# 定义model变量
w = [45]
min = 10000
max = 18550  # 18-29岁最大2650kcal每天，即18550每周
c = [0]
alpha = 1/8000  # 每8000kcal增加体重1kg
c[0] = 10000  # 成年人每周需要摄入12600-14000卡,即1800-2000每天
beta = alpha*c[0]/w[0] # c[0]/w[0]是每周每公斤；那每天的基本代谢速率就是c[0]/w[0] *45/7
a = (beta/alpha) * w[0] + 1/alpha
k=0
while (k<19):
    if(c[k]<18550):
        x = a + beta/alpha * k
        if(x>18550):
            c.append(18550)
            w.append(w[k] + alpha * c[k + 1] - beta * w[k])
            k = k + 1
            continue
        c.append(x)
        w.append(w[0]+k)
        beta = alpha * (c[0] / w[0] + 10 * k)  # 体重每增加1kg 基础代谢速率增加70kcal（每周）
    if (c[k] == 18550) :
        c.append(18550)
        w.append(w[k]+alpha*c[k+1]-beta*w[k])
        beta=alpha * (c[0] / w[0] + 10 * (w[k+1]-w[k]))
    k=k+1

print("第一阶段用时：" + str(k) + "周,第"+ str(k)+"周周末体重"+str(w[k]))
print(k)
print(c)
print(w)
test=pd.DataFrame(c,w)
test.to_csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv")

#第一阶段定制菜谱
# print("菜单如下(每100g食物的kcal)：")
# print("肉类：猪肉、牛肉、羊肉、鸡肉")
# print("豆制品：豆腐、豆浆、豆奶、鸡蛋")
# print("奶类：酸奶、牛奶")
# print("水果：苹果、香蕉、牛油果")
# # 每天从各类中选一个食物吃
# a1=input("请输入今天想吃的肉类:")
# a2=input("请输入今天想吃的豆制品：")
# a3=input("请输入今天想吃的奶类:")
# a4=input("请输入今天想吃的水果:")
# b1,b2,b3,b4=input("输入你选择的数量，单位为100g，用空格隔开:").split()
# b1 = int(b1)
# b2 = int(b2)
# b3 = int(b3)
# b4 = int(b4)
# a11 = 0
# a22 = 0
# a33 = 0
# a44 = 0
# if (a1=="牛肉"): a11 = 107
# if (a1=="羊肉"): a11 = 203
# if (a1=="鸡肉"): a11 = 191
# if (a2=="豆腐"): a22 = 81
# if (a2=="豆浆"): a22 = 14
# if (a2=="豆奶"): a22 = 30
# if (a2=="鸡蛋"): a22 = 144
# if (a3=="酸奶"): a33 = 72
# if (a3=="牛奶"): a33 = 54
# if (a4=="苹果"): a44 = 50
# if (a4=="香蕉"): a44=46
# if (a4=="牛油果"): a44=60
# sum = 0
# for i in range(k):
#     sum = a11 * b1 + a22 * b2 + a33 * b3 + a44 * b4
#     if ( sum < c[i]/7-100):
#         print("这些食物摄入总量为"+str(sum)+"kcal，和第"+str(i+1)+"天的标准还差"+str(round(c[i]/7-sum,3))+"kcal，您可以继续选择")
#     elif (c[i]/7-100<=sum & sum <= c[i]/7+100):
#         print("您选择的食物的摄入总卡数正好等于第"+str(i+1)+"天应有的摄入量！")
#     else:
#         print("这些食物摄入总量为"+str(sum)+"kcal，超出第"+str(i+1)+"天应有摄入量"+str(round(sum-c[i]/7,3))+"kcal，您可以选择少吃一些哦")
