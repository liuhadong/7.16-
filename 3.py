word = input('请输入一串字符:')
num = 0
for num in word:
    if word.isdigit():
        num += 1
print('字符串中包含的数字的个数为:%s'%num)
