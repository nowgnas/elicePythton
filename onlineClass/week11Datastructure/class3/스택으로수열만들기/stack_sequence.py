'''
is_stack_sequence 함수를 작성하세요.
'''


def is_stack_sequence(nums):
    stack = [1]
    current = 0

    for item in range(2, len(nums)+1):
        while len(stack) > 0 and stack[-1] == nums[current]:
            stack.pop()
            current += 1

        if len(stack) == 0 or stack[-1] < nums[current]:
            stack.append(item)
        else:
            return "NO"

    return "Yes"
