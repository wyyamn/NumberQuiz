# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:53:18 2020

@author: natuk
"""

minimum = int(input('最小值：'))
maximum = int(input('最大值：'))
if minimum > maximum:
    print('玩不下去了！重新来')
    minimum = int(input('最小值：'))
    maximum = int(input('最大值：'))
    
else:   
    print('本游戏在' + str(minimum) + '到' + str(maximum) + '之间进行')
    
goal = int(input('玩家1,请决定一个数字: '))
print('不能告诉别人哦！')

p = int(input('玩家2,请猜数字: '))

while True:
    if minimum <= p < goal:
        print('数字在' + str(p) + '到' + str(maximum) + '之间')
        minimum = p
        p = int(input('再猜一个数字:'))
        
    elif goal < p <= maximum:
        print('数字在' + str(minimum) + '到' + str(p) + '之间')
        maximum = p
        p = int(input('再猜一个数字:'))
      
    elif p == goal:
        print('你输了,真心话还是大冒险？')
        break
    else:
        print('玩不下去了！')
        p = input('请输入' + str(minimum) + '到' + str(maximum) + '之间的数字:')