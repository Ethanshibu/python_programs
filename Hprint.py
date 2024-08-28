# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

#top cone
for i in range(n):
    h = 'H'*(i*2+1)
    print(h.center(n*2-1,' '))

for i in range(n+1):
    print(' '*(n//2)+("H"*n).ljust(n*5//2),("H"*n).rjust(n*5//2))
    
for i in range(3):
    print(' '*(n//2)+"H"*n*5)

for i in range(n+1):
    print(' '*(n//2)+("H"*n).ljust(n*5//2),("H"*n).rjust(n*5//2))

for i in range(n,0,-1):
    h = 'H'*(i*2-1)
    print(' '*(n*4)+h.center(n*2-1,' '))
