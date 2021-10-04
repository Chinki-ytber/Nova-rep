import random
cap = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i' 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z','1','2','3','4','5','6','7','8','9','0']


output = f'{random.choice(cap)}{random.choice(cap)}{random.choice(cap)}{random.choice(cap)}'

print(output)
inp=input('Enter the capta: ')

if inp == output:
    print("verified")

else:
    print('no')
