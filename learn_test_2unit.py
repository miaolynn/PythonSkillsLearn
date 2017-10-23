#-*- coding:utf-8 -*-

from random import randint
import timeit
#data = [randint(-10,10) for _ in xrange(10)]
###1.filter data
# first method
x="""
from random import randint
data = [randint(-10,10) for _ in xrange(10)]
filter(lambda x:x>=0,data)
"""
print timeit.timeit(stmt=x,number=1)

# second method
d = {x :randint(0,100) for x in xrange(1,21)}
d_new={k:v for k,v in d.iteritems() if v>=90}
print d_new

# third method
data = [randint(-10,10) for _ in xrange(10)]
s = set(data)
s_filter = {x for x in s if x%3==0}
print  s_filter

####2. named tuple
student = ('Jim',17,'male','jim@gmail.com')
NAME,AGE,SEX,EAMIL=xrange(4)
print student[NAME]

##### second method
from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
s=Student('jim',16,'male','jim@gmail.com')

###统计序列中元素的个数
data = [randint(0,20) for _ in xrange(30)]
c=dict.fromkeys(data,0)
for x in data:
    c[x]+=1
print c

from collections import Counter
text='''i am a clever girl, i like staying alone,i don't feel lonely,it can't be known by someone,but i don't want to change,i know who i am.'''
import re
text_s = re.split('\W+',text)
c2 =Counter(text_s)
c2.most_common(3)
###取出频次前三的词

####如何根据字典中值的大小对字典中的项进行排序
####第一种方法
from random import randint
data ={ x:randint(60,100) for x in 'abcxyz'}
t = zip(data.itervalues(),data.iterkeys())
###可以使用values或者keys
sorted(t)
#####第二种方法
sorted(data.items(),key=lambda x:x[1])


####如何快速找到多个字典中的公共key
####x第一种方法
from random import sample
s1={ x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2={ x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3={ x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s1.viewkeys()&s2.viewkeys()&s3.viewkeys()

###第二种方法
s= reduce(lambda  a,b:a&b,map(dict.viewkeys,[s1,s2,s3]))
print s


###如何使字典有序
###############method
from collections import OrderedDict
from random import  randint
from time import time

######create palyers
players = list('ABCDEFGH')
d = OrderedDict()
start = time()

for i in xrange(8):
    raw_input()
    p=players.pop(randint(0,7-i))
    end=time()
    print i+1,p,end-start,
    d[p]=(i+1,end-start)
print
print '-'*20
for k in d:
    print k,d[k]


########how to record a history
############method
from random import  randint
from collections import deque
import pickle
N=randint(0,100)
d=deque([],5)

def guess(k):
    if k==N:
        print "right"
        return  True
    elif k>N:
        print "greater than N"
    else:
        print "less than N"
    return False

while True:
    line=raw_input("please input a number: ")
    if line.isdigit():
        k=int(line)
        d.append(k)
        if guess(k):
            break
    elif line=="history" or line=="h?":
        print list(d)

pickle.dump(d,open('history','w'))
q_history=pickle.load(open('history'))
print list(q_history)


