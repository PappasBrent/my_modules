traits = dict(name='Brent', age=19)

print(*traits.items(), sep='\n')

for i in range(ord('A'), ord('Z')+1):
    print(chr(i),end=' ')
