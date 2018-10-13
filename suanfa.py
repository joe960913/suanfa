#递归
'''递归：汉诺塔游戏'''
def hanoi(x,a,b,c):#所有盘子从a移到c
    if x > 0:
        hanoi(x-1,a,c,b)#step1：除了下面最大的，剩余的盘子从a移到n
        print('%s->%s'%(a,c))#step2：最大的盘子从a移到c
        hanoi(x-1,b,a,c)#step3：把剩余的盘子从b移到c
hanoi(3,'a','b','c')

def h(x):#计算次数
    num = 1
    for i in range(x-1):
        num = 2*num+1

    print(num)
h(3)

'''递归：斐波那契数列'''
def fi(n):
    a,b = 0,1
    for i in range(0,n):
        yield b
        a,b = b,a+b

for i in fi(10):
    print(i)

#查找
'''顺序查找，时间复杂度O(n)'''
def linearsearch(dataset,val):
    for i in range(len(dataset)):
        if dataset[i] == val:
            return i
    return

'''二分查找，时间复杂度O(logn)'''
#必须是顺序存储结构，必须按关键字大小有序排列。将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
def binsearch(dataset,val):
    low = 0                           #最小数下标
    high = len(dataset) - 1           #最大数下标
    while high >= low:
        mid = (high+low) // 2         #中间数下标
        if dataset[mid] == val:       #如果中间数下标等于val, 返回
            return  mid
        if dataset[mid] > val:        #如果val在中间数左边, 向左移动high下标
            high = mid - 1
        if dataset[mid] < val:        #如果val在中间数右边, 向右移动low下标
            low = mid + 1
    return
ret = binsearch([1,2,3,4,5,6,7,8,9,10],7)
print(ret)

#排序 速度慢的三个
'''冒泡排序，时间复杂度最好情况O(n)，最坏情况O(n^2)'''
#列表相邻的两个数，如果前边的比后边的小，那么交换顺序，经过一次排序后，最大的数就到了列表最前面
def bubblesort(li):
    for j in range(len(li)-1):
        for i in range(len(li)):
            if li[i]>li[i-1]:
                li[i],li[i-1] = li[i-1],li[i]
    return li

'''插入排序，时间复杂度O(n^2)'''
#把列表分为有序区和无序区两个部分。最初有序区只有一个元素。然后每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
def insertsort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp <li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
    return li

'''选择排序，时间复杂度O(n^2)，最稳定的排序算法之一'''
#遍历列表一遍，拿到最小的值放到列表第一个位置，再找到剩余列表中最小的值，放到第二个位置
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i  # 假设当前最小的值的索引就是i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:  # min_loc 值如果发生过交换，表示最小的值的下标不是i,而是min_loc
            li[i], li[min_loc] = li[min_loc], li[i]

    return li

#速度快的排序
'''快速排序，时间复杂度O(nlogn)，最坏情况O(n^2)'''
#让指定的元素归位，所谓归位，就是放到他应该放的位置（左变的元素比他小，右边的元素比他大），然后对每个元素归位，就完成了排序
def quicksort(data):
    if len(data)<=1:
        return data
    less = []
    more = []
    base = data.pop(0)
    for x in data:
        if x < base:
            less.append(x)
        else:
            more.append(x)
    return quicksort(less)+[base]+quicksort(more) #递归调用

zzz= quicksort([1,7,9,2,4,5])
print(zzz)

'''归并排序，时间复杂度O(nlogn)，特殊的，归并排序还有一个O(n)的空间复杂度，稳定'''
#列表分成两段有序，然后分解成每个元素后，再合并成一个有序列表，这种操作就叫做一次归并。应用到排序就是，把列表分成一个元素一个元素的，一个元素当然是有序的，将有序列表一个一个合并，最终合并成一个有序的列表

'''堆排序，时间复杂度O(nlogn)'''
'''希尔排序，O(nlogn)'''