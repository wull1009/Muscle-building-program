#模型一
dat1=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat1
dat1$时间=c(seq(0,91,by=7))
library(ggplot2)
ggplot(dat1,aes(x=时间))+
  geom_line(y=dat1$X0/7,col="black",size=1)+
  geom_vline(xintercept = 28,col="red",size=1,linetype=2)+
  labs(title="模型I-热量吸收图",x="时间/天",y="每天吸收热量/kcal") +
  theme(plot.title = element_text(hjust = 0.5))+
  ylim(1420,2700)

ggplot(dat1,aes(x=时间))+
  geom_line(y=dat1$X,col="steelblue",size=1)+
  geom_vline(xintercept = 28,col="red",size=1,linetype=2)+
  labs(title="模型I-体重变化图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))+
  ylim(40,60)

#模型二：吃+有氧
dat2=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat2=dat2[,-2]
colnames(dat2)=c("模型II","时间","模型I")
library(reshape2)
data22=melt(dat2,id="时间")
head(data22)
dat3=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat3=dat3[-2,]
dat2[,4]=dat3$X
dat2$时间=c(seq(0,126,by=7))
ggplot(dat2,aes(x=时间))+
  geom_line(y=dat2$X,col="black",size=1)+
  geom_line(y=dat2$V4,col="steelblue",size=1)+
  geom_vline(xintercept = 28,col="red",size=1,linetype=2)+
  geom_vline(xintercept = 81,col="orange",size=1,linetype=2)+
  labs(title="模型I&模型II-体重变化图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))+
  ylim(40,60)+
  scale_fill_discrete(limits=c("steelblue-模型I", "black-模型II"))
#不同运动及时间对比
dat5=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据-模型II.csv",header = T,encoding = "UTF-8")
head(dat5)
colnames(dat5)=c("跳舞12h","跳舞10h","跳舞6h","骑车6h","骑车10h","时间")
library(reshape2)
data55=melt(dat5,id="时间")
colnames(data55)=c("时间","分类","体重")
ggplot(data=data55,aes(x=时间,y=体重,group=分类,color=分类))+
  geom_line(size=1)+
  labs(title="模型II-体重变化图",x="时间/周",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))
ggplot(data=data22,aes(x=时间,y=value,group=variable,color=variable))+
  geom_line(size=1)+
  geom_line(x=dat6$时间,y=dat6$体重)+
  labs(title="模型I&II-体重对比图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))+
  geom_vline(xintercept = 28,col="steelblue",size=1,linetype=2)+
  geom_vline(xintercept = 81,col="black",size=1,linetype=2)


#模型III：吃+有氧+增肌
dat4=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat2
write.csv(yy,file="抽样草稿.csv",row.names=T)
colnames(dat4)[1]="时间"

ggplot(dat4,aes(x=时间))+
  geom_line(y=dat4$X0,col="black",size=1)+
  geom_line(y=dat2$X,col="black",size=1)+
  geom_line(y=dat2$V4,col="steelblue",size=1)
dat6=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat6
ggplot(dat6,aes(x=时间))+
  geom_line(y=dat6$体重,col="black",size=1)+
  geom_vline(xintercept = 21,col="red",size=1,linetype=2)+
  geom_vline(xintercept = 45,col="red",size=1,linetype=2)+
  geom_hline(yintercept = 50,col="orange",size=1,linetype=2)+
  labs(title="模型III-体重变化图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))+
  ylim(40,60)

# 对比
dat7=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/对比.csv",header = T,encoding = "UTF-8")
dat7
ncol(dat7)
colnames(dat7)[1]=c("时间")
dat77=melt(dat7,id="时间")
head(dat77)
ggplot(data=dat77,aes(x=时间,y=value,group=variable,color=variable))+
  geom_line(size=1)+
  labs(title="模型I&II&III-体重对比图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))

#敏感度分析
dat8=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat9=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat10=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
dat11=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
data88=matrix(c(dat8$X,dat9$X,dat10$X,dat11$X),ncol=4,byrow=F)
data88=data88[-1,]
data88=as.data.frame(data88)
data88$时间=seq(0,126,by=7)
colnames(data88)=c("45","47","49","51","时间")
data88
dat888=melt(data88,id="时间")
ggplot(data=dat888,aes(x=时间,y=value,group=variable,color=variable))+
  geom_line(size=1)+
  labs(title="w[0]-体重对比图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))


d1=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
colnames(d1)=c("时间","gamma=4.5,h=10","gamma=5.9,h=10","gamma=7.9,h=10","gamma=5.9,h=8","gamma=5.9,h=12")
d1=d1[-c(1,2,3),]
d11=melt(d1,id="时间")
ggplot(data=d11,aes(x=时间,y=value,group=variable,color=variable))+
  geom_line(size=1)+
  labs(title="gamma-体重对比图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))
d2=d1=read.csv("C:/Users/wulinlin/Desktop/数学模型期末报告/数据.csv",header = T)
head(d2)
d2=d2[-c(1:8),]
colnames(d2)=c("时间","x=2","x=2.5","x=3","x=3.5","x=4")
d22=melt(d2,id="时间")
ggplot(data=d22,aes(x=时间,y=value,group=variable,color=variable))+
  geom_line(size=1)+
  labs(title="x-体重对比图",x="时间/天",y="体重/kg") +
  theme(plot.title = element_text(hjust = 0.5))+
  scale_color_manual(values = c("#0073C2FF", "#EFC000FF", "#868686FF","yellow","grey"))
