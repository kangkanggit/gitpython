for i in range(5):
    if i < 4:
        print(' '*(8-i)+'*'*(i*2+1)+' '*(11-i)+' '*(8-i)+'*'*(i*2+1),end='')
        print()
    else:
        print(' ' * (9 - i) + '*' * (i * 2 )+' ' * (13 - i)+' ' * (7 - i) + '*' * (i * 2 ), end='')
        print()
for i in range(3):
    if i < 2:
        print(' '*(4-i)+'^'*(2*i+9)+'*'*(11-(2*i))+'^'*(2*i+9),end='')
        print()
    else:
        print(' ' * (5 - i) + '^' * (2 * i + 8)+'*' * (11 - (2 * i))+'^' * (2 * i + 8), end='')
        print()
for i in range(2):
    print(' '*(i+7+(i*2))+'^'*(9-(i*2))+'*'*(5-i)+'^'*(9-(i*2)),end='')
    print()
for i in range(2):
    print(' '*(13+i*4)+'^'*(4-(3*i))+'*'*(3-(2*i))+'^'*(4-(3*i)),end='')
    if i == 1:
        print('.')
    else:
        print()
