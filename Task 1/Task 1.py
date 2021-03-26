import time
def itoBase(N,b):
    l = len(b)
    if (N == 0) or (l < 2):
        return 'usage'
    s = ""
    while (N > 0):
        x = N % l
        N = N // l
        s = b[x] + s
    return s   
    
a, b = int(input('Введите десятичное число: ')), (input('Введите систему счисления: ')) 
print(itoBase(a, b))

print('Консоль закроется через 20 секунд...')
time.sleep(20)