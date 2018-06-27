
while True:
    c = input('A char:')
    if c == 'o':
        # 有一点需要尤其注意，如果你 中断 了一个 for 或 while 循环，任何相应循环中的 else
        # 块都将不会被执行。
        break
    print('you enter ', c)
else:
  print('The while loop is over.')