import pandas as pd

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
    if c[k] > max :
        c[k]=18550
        break
    beta = alpha*(c[0]/w[0]+10*k) # 体重每增加1kg 基础代谢速率增加70kcal（每周）


print("第一阶段用时：" + str(k) + "周,第"+ str(k)+"周周末体重"+str(w[k]))
print(k)
print(c)
print(beta)
print(w)

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
print(beta2)
k = 1
if (gamma == 0):
    print("此项目不属于我为您量身定做的有氧运动~")
while(k<150):
    w_2.append(w_2[k-1] + alpha * max - beta2 * w_2[k-1])
    u.append((w_2[k] - alpha * max / beta2) / (48 - alpha * max / beta2))
    if w_2[k]<48:
        print("运动过多，不能增重啦！请减少运动时间或选择更加吻合的运动")
        break
    if w_2[k]>55:
        n=w_2[k]-48
        print(str(k) + "周后，在每周" + str(sport) + str(t) + "小时的情况下，体重增重到了" + str(round(48 + n, 3)) + "kg")
        break
    if (k > 20):
        print("此阶段运动时间超过5个月，建议缩短每周运动时间")
        break
    k = k + 1
del(w_2[0])
w.extend(w_2)
print(w)
c += k*[(18550)]
print(c)
test=pd.DataFrame(w)
test.to_csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv")