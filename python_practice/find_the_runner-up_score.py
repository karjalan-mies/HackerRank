if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == n:
        arr.sort()
        max_n = arr[-1]
        runner_up = 0
        for el in arr:
            if el < max_n:
                if el < 0:
                    runner_up = el
                elif el > runner_up:
                    runner_up = el
        print(runner_up)