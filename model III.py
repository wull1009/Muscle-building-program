import matplotlib.pyplot as plt

# 定义model变量
w = [45]
min = 10000
max = 18550  # 18-29岁最大2650kcal每天，即18550每周
c = [0]
alpha = 1/8000  # 每8000kcal增加体重1kg
c[0] = 10000  # 成年人每周需要摄入12600-14000卡,即1800-2000每天
beta = alpha*c[0]/w[0] # c[0]/w[0]是每周每公斤；那每天的基本代谢速率就是c[0]/w[0] *45/7
a = (beta/alpha) * w[0] + 1/alpha
for k in range(1,15):
    c.append( a + beta/alpha * k)
    w.append(w[0]+k)
    if c[k] > max : break
    beta = alpha*(c[0]/w[0]+10*k) # 体重每增加1kg 基础代谢速率增加70kcal（每周）


print("第一阶段用时：" + str(k) + "周,第"+ str(k)+"周周末体重"+str(w[k]))
print(k)
print(c)
print(beta)
print(w)



print("第一阶段用时：" + str(k) + "周,第"+ str(k)+"周周末体重"+str(w[k]))
print(k)
print(c)
print(max)
print(w)
# #第一阶段定制菜谱
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
#     if ( sum < c[i]-100):
#         print("这些食物摄入总量为"+str(sum)+"kcal，和第"+str(i+1)+"天的标准还差"+str(round(c[i]-sum,3))+"kcal，您可以继续选择")
#     elif (c[i]-100<=sum & sum <= c[i]+100):
#         print("您选择的食物的摄入总卡数正好等于第"+str(i+1)+"天应有的摄入量！")
#     else:
#         print("这些食物摄入总量为"+str(sum)+"kcal，超出第"+str(i+1)+"天应有摄入量"+str(round(sum-c[i],3))+"kcal，您可以选择少吃一些哦")



# 根据第一阶段可知，第一阶段持续了2周，体重有45增加到了47kg
# 第二阶段 每周保持最大的热量吸收（）调整后的，每周加一个定值，同时进行运动，会消耗热量
#运动过渡期
w_2 = [48]
u = [0]
gamma = 0
sport = input("输入你想选择的运动：")
time = input("输入每周运动的时间：")
if (sport == "跳舞"):
    gamma = 4.5
if (sport== "健身操"):
    gamma = 5.9
if (sport == "骑车"):
    gamma = 7.9
t = int(time)
gamma = float(gamma)
beta2 = beta + alpha * gamma * t
k = 1
if (gamma == 0):
    print("此项目不属于我为您量身定做的有氧运动~")
while(gamma != 0):
    w_2.append(w_2[k-1] + alpha * max - beta2 * w_2[k-1])
    u.append((w_2[k] - alpha * max / beta2) / (47 - alpha * max / beta2))
    if w_2[k]<48:
        print("运动过多，不能增重啦！请减少运动时间或选择更加吻合的运动")
        break
    if w_2[k]>50:
        n=w_2[k]-48
        print(str(k) + "周后，在每周" + str(sport) + str(t) + "小时的情况下，体重增重到了" + str(round(48 + n, 3)) + "kg")
        break
    if (k > 20):
        print("此阶段运动时间超过5个月，建议缩短每周运动时间")
        break
    k = k + 1

# 第三阶段 增肌
# 由于保持了最大食量每周18550卡，因此第三阶段我的食量是每天2650卡。其中1695.5用于基本的新陈代谢。
# 在健身中，每公斤体重所消耗的热量大约是16卡/天。那么随着体重增长，大概800卡每天。16*(w[k])
# 设以脂肪形式储存的热量100%有效，且1kg蛋白质含热量6000卡，1kg肌肉大概2000-3500卡，分析这个人的体重变化。
# 假设摄入的高蛋白食物和肌肉的转换比为1：3
# 体重随时间的变化w[t]
from scipy.integrate import odeint
import numpy as np
take = 18550/7  # 每天食量保持最大值2650卡
basic = beta/alpha*50/7  # 设置基础代谢卡数每天 1730卡
print(basic)

w_3 = [w_2[len(w_2)-1]]
u = [0]
i = 0  # i是一天
print(w_3[0])
while(i<120):
    i = i + 1
    u.append((take - basic -16*w_3[i-1])/6000 * 3)  # 增肌的重量，单位：kg
    w_3.append(w_3[i-1] + alpha * (take - basic )+  u[i]  )# w[i]是第i天开始的体重
    if(w_3[i]>55):break
print(i)
print(w_3)
# ii=list(range(110))
# del(u[0])
# del(w_3[0])
# plt.plot(ii, u, '-', color='cornflowerblue', label='增肌的重量')
# plt.xlabel('time/day')
# plt.ylabel('increincreased weight of muscle/kg')
# plt.title('u(t)-III')
# plt.plot(ii, w_3, '-', color='cadetblue', label='增肌的重量')
# # plt.legend(loc = 'upper right')
# plt.show()
# 关于增肌训练，我更希望着重练的是肩膀、胳膊、腹肌，因此会针对这三个方面进行增肌训练,下列运动视频是我在keep里已经选好的，并且有卡数标识
# 假设每天只练一个部位
# a=input("请输入你今天想训练的部位:")
# if(a == "肩膀"):
#     dl=int(input("选择1.开肩美背 2.紧致上背"))
#     if (dl == 1): b1 = 15
#     else: b1 = 25
# if(a == "胳膊"):
#     dl=int(input("选择1.告别摆摆肉 2.手臂增肌"))
#     if (dl == 1): b1 = 20
#     else: b1 = 15
# if(a == "腰腹"):
#     dl=int(input("选择1.核心训练 2.暴爽虐腹"))
#     if (dl == 1): b1 = 30
#     else: b1 = 40
# #输入你想选择的训练，算法会根据你每天用于增肌的卡数输出你锻炼的组数。
# x = [0]
# y = [0]
# n = int(input("输入你想查看的训练日期："))
# for m in range(1,len(u)):
#     x.append(u[m]*2000) # 因为我们前边假设1kg肌肉2000卡,x便是每天用于增肌的卡数
#     y.append(x[m]/b1)
#
# print("第"+str(n)+"天你需要练习"+str(a)+str(round(y[n],2))+"组")
# import pandas as pd
# print(w)
# print(w_2)
# print(w_3)
#
del(w_2[0])
del(w_3[0])
w.extend(w_2)
w.extend(w_3)
print("0")
print(w)
import pandas as pd
# test=pd.DataFrame(w)
# test.to_csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv")