inputs = input()

hp = 0
for item in inputs:
    if item == '(':
        hp -= 1
    else:
        hp += 1
print("YES" if hp == 0 else"NO")
