'''
Created on 15/05/2018
Find the Runner-Up Score!
For a given list of numbers, find the second largest number.
3
1 2 3
'''
if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 10:
        arr = set(map(int, input().split()))
        winner = max(arr)
        runner_up = max(arr.difference({winner}))
        print(runner_up)
