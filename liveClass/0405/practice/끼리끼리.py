def solve_dodo(word_input):

    stack = []

    for char in word_input:
        if stack is None:  # stack 에 들어간 값이 0개면 append
            stack.append(char)
        else:
            if char == stack[-1]:  # stack의 마지막 값이랑 char 랑 같으면 stack을 pop
                stack.pop()
            else:
                stack.append(char)
                # 아니면 push
    if not stack:
        return True
    else:
        return False


N = int(input())  # 받을 단어의 수

answer = 0

for i in range(N):
    word = input()
    if solve_dodo(word):
        answer += 1
print(answer)
