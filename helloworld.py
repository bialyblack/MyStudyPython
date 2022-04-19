
"""
print("hello,world")
for target in range(12):
    print("target")
    #卡了
    """
################################################################
'''
print("a")
print("b")
'''
#求出相对应的asii码
"""
number=int(input("请输入数字："))
while number>0:
    name=input("please input the name:")
    print(name+"asii",ord(name))
    number=number-1

"""
"""
from asyncio.windows_events import NULL
number=0
for i in range(31):
    number2=int(input("请输入数字："))
    name=""
    while number2>0:
        ch=input("please input the ch:") 
        name=name+ch
        print(name) 
        number2=number2-1 
   
    number=number+1
    #print(number)

"""
"""
from asyncio.windows_events import NULL
number=0
for i in range(31):
    number2=int(input("请输入数字："))
    name=""
    while number2>0:
        ch=int(input("请输入字符的值:")) 
        name=name+chr(ch)
        print(name) 
        number2=number2-1 
    print(name)
    number=number+1
    print(number)
"""
"""
print("要么成为巨人，要么卷铺盖回家")
print("                  |")
print("——————————————————")
print("|Go Big Or Go Home|")
print("——————————————————")
love="我爱你一生一世"
print(love)
love=520.1314
print(love)
love=5211314
print(love)


a=input("请输入数字（1-7）")
if a=='1':
    print("今天是星期一")
elif a=='2':
    print("今天是星期二")
elif a=='3':
    print("今天是星期三")
elif a=='4':
    print("今天是星期四")
elif a=='5':
    print("今天是星期五")
elif a=='6':
    print("今天是星期六")
elif a=='7':
    print("今天是星期日 ")
"""

    #输出到指定文件

#fp = open(r'E:\mr.txt','a+')
#print("没有毅力失败",file=fp)
#fp.close()

"""
import datetime
imyear=input("请输入你的年份：")
nowyear=datetime.datetime.now().year
age=nowyear-int(imyear)
print("您的年龄为"+str(age)+"岁")
if age<18:
    print("您现在是未成年人")
if age>=18 and age<= 66:
    print("您现在是青年人")
if age>=66 and age<=80:
    print("您现在是中年人")
if age>=80:
    print("您现在是老年人")
    """
#nickname="我好"#必须在一行
#nickname2='我很好'#必须在一行
#nickname3="""我真的
#很好"""#可以分行
#print(type(nickname))
#print(id(nickname))
#print(nickname)
#print(nickname2)

#print(nickname3)
"""
print("失望之久\x0a希望之本")
print(r"失望之久\x0a希望之歌")
python=95
english=92
c=89
sub=python-english
avg=(python+english+c)/3
print("python和English的差："+str(sub)+"分\n")
print("avg:"+str(avg))"""

#print("12&8=" +str(12&8)) 

'''a=-9
b = a if a>0 else -a
print(b)'''
"""str="不要再说我不能"
for ch in str:
    print(ch)
result =0
for i in range(1,10,2):
    print(i, end=" ")"""
"""for i in range(1,10):
    if i%2==0:
        print(i, end=" ")
    else:
        pass"""
"""arr=[0,1,2,3,4,5,6,7,8,9,10]
brr=["你好","我很好"]
crr=[None]*5
#print(crr)
#print(len(arr))
print(max(arr))
print(min(arr))"""
"""print(arr+brr)
print(arr[1:5])
print(arr[1:5:2])"""
#a=list(range(10,20,2))
#print(a)
arr=[0,1,2,3,4,5,6,7,8,9,10]
#a.append(12)
#a.extend(arr)#将一个列表的元素完全添加到另一个列表
"""arr[1]=10
print(arr)
del arr[-1]
print(arr)
arr.remove(2)
print(arr)"""
"""if arr.count(3)>0:
    arr.remove(3)"""
"""print(arr.count(3))
print(arr.index(3))
arr.sort(reverse=True)
print(arr)"""




"""import random
randomnumber=[random.randint(10,100) for i in range(10)]
print(randomnumber)
newlist=[x*0.5 for x in randomnumber]
newlist=[x for x in newlist if x>30]
print(newlist)
"""
"""for item in a:
    print(item)"""
""""for index,item in enumerate(a):
    print(index,item)"""
from ast import Str
from multiprocessing import Value
import random
from re import I, template

"""a1="1",#元组。只要有小逗号就是元组
b1="1"
print(type(a1))
print(type(b1))"""
"""#空的元组
c1=()"""

#print(tuple(range(10,20,2)))
"""randomnumber=(random.randint(10,100) for i in range(10))
print(tuple(randomnumber))"""
"""number=(i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number=tuple(number)
print(number)"""

''''#dictionary={'a1':'1', 'b1':'2', 'c1':'3'}
brr=['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10']
dictionary=dict(zip(arr,brr))
print(dictionary)'''
'''str1='人生苦短，我学python'
print(len(str1))
#丢出异常
try:
    substr1=str1[12]
except IndexError:
    print('指定超出界限')
list1=str1.split('，')
print(list1)
'''
#find是找出位置索引
"""str2='1@2@3'
print('result:',str2.find("*"))
print('result:',str2.find("@"))
print('result:',"*"in str2)
print('result:',str2.rindex("@"))
print('result:',str2.endswith('@'))
str3=' www.Mingsoft.com'
print('原字符串：',str3)
print('新字符串：',str3.lower())
print('新字符串：',str3.upper())
print(str3.strip())"""

"""template='编号：%09d\t公司名称：%s\t官网:http://www.%s.com'
template1='编号：{:0>9d}\t公司名称：{:s}\t官网:http://www.{:s}.com'
context1=(1,'百度','baidu')
context2=template1.format(1,'百度','baidu')
print(template%context1)
print(context2)"""

'''import re
pattern=r'mr_\w+'
str2='MR_Shorp,mr_shorp'
#match=re.match(pattern,str2,re.I)
match=re.search(pattern,str2,re.I)
print(match)
match1=re.findall(pattern,str2)
print(match1)
pattern2=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str3='127.0.0.1 192.168.1.66'
match2=re.findall(pattern2,str3)
for item in match2:
    print(item[0])'''

'''import re
pattern=r'1[34578]\d{9}'
str4='联系电话：18011544545'
result=re.sub(pattern,'1xxxxxxxxxx',str4)
print(result)'''
'''import re
pattern=r'[?|&]'
url='https://www.baidu.com/s?tn=news&rtt=1&bsst=1&wd=2021%E5%B9%B4%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E6%8E%92%E8%A1%8C%E6%A6%9C&cl=2'
result=re.split(pattern,url)
print(result)'''
'''
'''



"""def filterchar(string):
    '''功能：过滤危险的字符（黑客）并将过滤结果输出，'''
    import re
    pattern=r'(黑客)|(抓包)|(监听)|(Trojan)'
    sub=re.sub(pattern,'@_@',string)
    print(sub)
filterchar('黑客帝国')"""
"""def demo(obj):
    print("原值：",obj)
    obj+=obj
mot="唯有再被追逐的时候，你才能真正奔跑"
print("调用函数前：",mot)
demo(mot)
print("调用函数后：",mot)
list1=['1','2','3']
print("调用函数前：",list1)
demo(list1)
#print("调用函数后：",list1)"""
"""def demo(obj=None): 
    if obj is None:
        obj=[]
    print("obj的值：",obj)
    obj.append(1)
demo()
demo()"""
'''def printcoffe(*coffeenames):
    print('\n我喜欢的咖啡有：')
    for item in coffeenames :
        print(item)
list1=['1','2','3']
printcoffe(*list1)'''
"""def printsign(**sign):
    print()
    for key,value in  sign.items():
        print('['+key+"]的星座是："+value)
printsign(绮梦='aa',冷兴义='bb')"""
'''message='唯有在被追赶的时候,你才能真正地奔跑'
print(message)
def demo():
    global message
    message="希望之光"
    print(message)
demo()
print(message)'''
import math
'''def circlearea(r):
    result=math.pi*r*r
    return result
r=1
print(circlearea(r))'''
''''r2=10
result2=lambda r2:math.pi*r2*r2
print('圆的面积：',result2(r2))'''
"""class Geese:
    '''大雁类'''
    def __init__(self,beak,wing,claw):
        print(beak)
        print(wing)
        print(claw)
beak1='喙'
wing1='翅膀'
claw1='爪子'
wildGoose=Geese(beak1,wing1,claw1)"""


"""class Swan:
    '''天鹅'''
    __neck_swan='天鹅的脖子很长'
    def __init__(self):
        print(Swan.__neck_swan)
swan=Swan()
print(swan._Swan__neck_swan)"""


"""class Rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    @property
    def area(self):
        return self.width*self.height
rect=Rect(8,6)
print(rect.area)
rect=Rect(6,6)
print(rect.area)"""


"""class TVShow:
    def __init__(self,show):
        self.__show=show
    @property
    def show(self):
        return self.__show
tvshow=TVShow("正在播放战狼2")
print(tvshow.show)
tvshow.show="a"
print(tvshow.show)"""

"""class Fruit:
    def __init__(self, color="绿色"):
        Fruit.color=color
    def haverest(self):
        print("\n",Fruit.color)
class Oranges(Fruit):
    def __init__(self):
        print("我是橘子")
        super().__init__()
       

q1=Oranges()
q1.haverest()
"""