#输出素数
def primeNum(min,max):
    """求[min,max)区间范围内的素数,返回列表。"""
    prime = []
    for n in range(min,max+1):
        for x in range(2,n):
            if n%x == 0:
                # print(n,'equals',x,'*',n//x)
                break
        else:
            # print(n,"is a prime number")
            prime.append(n)
    return prime
  

#乱序字符检查        
def anagramCheck1(s1,s2):
    """判断s1是否是s2的乱序字符。

    把s2变成列表，依次判断s1中的字符是否在s2中，若在，则将该字符删除"""

    lists2 = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(lists2) and not found:
            if s1[pos1] == lists2[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            lists2.pop(pos2)
        else:
            stillOK = False
        pos1 += 1
    return stillOK


#乱序字符检查
def anagramCheck2(s1,s2):
    """判断s1是否是s2的乱序字符。

    利用排序后两者比较来判断"""

    lists1 = list(s1)
    lists2 = list(s2)
    sorts1 = lists1.sort()
    sorts2 = lists2.sort()
    if sorts1 == sorts2:
        match = True
    else:
        match = False
    return match








