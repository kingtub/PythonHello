s = '''
这是一段文本
写在文件里
作为测试
'''

f = open('s.txt', 'w')
f.write(s)
f.close()

f = open('s.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break

    print(line, end='')

f.close()
