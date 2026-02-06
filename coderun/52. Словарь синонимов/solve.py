import sys


def main():
    n = int(input())

    sinonims = dict()

    for i in range(n):
        key, value = input().split()
        sinonims[key] = value

    goal = input()

    for key, value in sinonims.items():
        if key == goal:
            print(value)
        elif value == goal:
            print(key)


if __name__ == '__main__':
    main()
