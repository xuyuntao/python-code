
n = 5
print('*' * 5)
for i in range(n - 2):
    print('*' + ' '*(n - 2) + '*')

print('*' * 5)


n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)
    else:
        print('*' + ' '*(n - 2) + '*' )

