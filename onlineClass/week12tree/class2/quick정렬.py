def quickSort(arr):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quickSort(lesser_arr) + equal_arr + quickSort(greater_arr)


def main():
    line = [int(x) for x in input(
        "정렬할 수를 입력하세요 (예시:10 2 3 4 5 6 9 7 8 1): ").split()]

    print('정렬 결과:', *quickSort(line))


if __name__ == "__main__":
    main()
