'''
https://jennymunjung.notion.site/bdc4ad3b4a74416380b0487be28cc586
'''


string = input()
depth = 0
stack = []

for ch in string:
    if ch == ')':
        depth = 0
        while True:
            t = stack.pop()
            depth += 1
            if t == '(':
                depth
