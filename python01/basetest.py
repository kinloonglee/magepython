import datetime
start = datetime.datetime.now()
count = 1
for x in range(3, 100000, 2):  # 舍弃掉所有偶数
    if x > 10 and x % 10 == 5: # 所有大于10的质数中，个位数只有1,3,7,9。意思就是大于5，结尾是5就能被5整除了
        continue
    for i in range(3, int(x ** 0.5) + 1, 2): # 为什么从3开始，且step为2？
        if x % i == 0:
            break
    else:
        count += 1
        # print(x, count)
        pass

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("~~~~~~~~~~~~~~")

start = datetime.datetime.now()
number = 100000
count = 2
for num in range(4, number):
    if num%6 != 1 and num%6 != 5:
        continue
    else:
        snum = int(num**0.5+1)
        for i in range(5, snum, 2):
            if not num%i:
                break
        else:
            count += 1
            pass
#print(count)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)

print("~~~~~~~~~~~~~~")

# 23-邢龙 18:07:09
# 大于等于5的质数一定和6的倍数相邻。
start = datetime.datetime.now()
n = 100000
#print(2, '\t', 3)
n = n - n % 6
for num in range(5, n, 6):
    k = int(num ** 0.5)
    for j in range(2, k + 1):
        if num % j == 0:
            break
    else:
        #print(num, end='\t')
        pass

    n = num + 2
    k = int(n ** 0.5)
    for j in range(2, k + 1):
        if n % j == 0:
            break
    else:
        #print(n, end='\t')
        pass

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)

print("~~~~~~~~~~~~~~")

