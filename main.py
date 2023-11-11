#task 1

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


for i in range(6):
    if i<2:
        print(f'{RED}{"  "*14}{END}')
    if 2<=i<4:
        print(f'{WHITE}{"  "*14}{END}')
    if i>=4:
        print(f'{BLUE}{"  "*14}{END}')

#task 2

BLACK = '\u001b[30m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
for i in range(1,6):
    if i == 3:
        print(f'{WHITE}{"  "*2}{BLACK}{"  "}{WHITE}{"  "*3}{BLACK}{"  "}{WHITE}{"  "*2}{END}')
    elif i%2==1:
        print(f'{BLACK}{"  "}{WHITE}{"  "*3}{BLACK}{"  "}{WHITE}{"  "*3}{BLACK}{"  "}{END}')
    else:
        print(f'{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{END}')


#task 3

p = [[0 for i in range(10)] for i in range(10)]
r = [0 for i in range(10)]
for i in range(10):
    r[i] = i*2
r = r[::-1]

for i in range(9):
    for j in range(9):
        p[i][8-i] = '*'

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(r[i]) + '\t'
        if p[i][j] == 0:
            line += '--'
        if p[i][j] == "*":
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9 10')

#task 4

k0,k1=0,0
with open('sequence.txt') as f:
    s = []
    for i in f:
        s.append(float(i))
    
    for i in range(len(s)):
        if i%2==0:
            k0 += abs(s[i])
        else:
            k1 += abs(s[i])
    print(k0,k1)

