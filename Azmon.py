x_str=input()
length=len(x_str)
#print(length)
l_x_str=x_str[0:length]
print('saratanı' if any(c.isdigit() for c in x_str) else 'salem')