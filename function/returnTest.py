def tr(i):
    if i < 0:
        return -1
    elif i < 10:
        return 'pos'
    elif i < 20:
        return

    print('end')


a = int(input())
while a != 100:
    print(tr(a))
    a = int(input())
